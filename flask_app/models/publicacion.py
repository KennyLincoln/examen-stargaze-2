from flask import flash
from flask_app.config.mysqlconnection import     connectToMySQL

class Publicacion:
    def __init__(self, data):
        self.id = data['id']
        self.nombre = data['nombre']
        self.lugar = data['lugar']
        self.fecha = data['fecha']
        self.descripcion = data['descripcion']
        self.usuario_id = data['usuario_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.nombre_usuario = data.get('nombre_usuario', '')
        self.total_likes = data.get('total_likes', 0)
        self.user_liked = data.get('user_liked', False)

    @classmethod
    def guardar(cls, datos):
        query = """
            INSERT INTO publicaciones (nombre, lugar, fecha, descripcion, usuario_id)
            VALUES (%(nombre)s, %(lugar)s, %(fecha)s, %(descripcion)s, %(usuario_id)s);
        """
        return connectToMySQL('esquema_publicaciones').query_db(query, datos)

    @classmethod
    def obtener_publicaciones(cls, usuario_id):
        query = """
            SELECT p.*, u.nombre AS nombre_usuario,
                   COUNT(DISTINCT mg.usuario_id) AS total_likes,
                   SUM(CASE WHEN mg.usuario_id = %(usuario_id)s THEN 1 ELSE 0 END) AS user_liked
            FROM publicaciones p
            JOIN usuarios u ON p.usuario_id = u.id
            LEFT JOIN me_gustas mg ON p.id = mg.publicacion_id
            GROUP BY p.id
            ORDER BY p.fecha ASC;
        """
        resultados = connectToMySQL('esquema_publicaciones').query_db(query, {'usuario_id': usuario_id})
        publicaciones = []
        if resultados:
            for fila in resultados:
                pub = cls(fila)
                pub.total_likes = fila['total_likes']
                pub.user_liked = True if fila['user_liked'] > 0 else False
                publicaciones.append(pub)
        return publicaciones

    @classmethod
    def get_by_id(cls, datos):
        query = """
            SELECT p.*, u.nombre AS nombre_usuario 
            FROM publicaciones p 
            JOIN usuarios u ON p.usuario_id = u.id 
            WHERE p.id = %(id)s;
        """
        resultados = connectToMySQL('esquema_publicaciones').query_db(query, datos)
        if resultados:
            return cls(resultados[0])
        return None

    @classmethod
    def buscar_por_nombre(cls, datos):
        query = "SELECT * FROM publicaciones WHERE nombre = %(nombre)s;"
        resultados = connectToMySQL('esquema_publicaciones').query_db(query, datos)
        if resultados:
            return cls(resultados[0])
        return None

    @classmethod
    def actualizar(cls, datos):
        query = """
            UPDATE publicaciones 
            SET nombre = %(nombre)s, lugar = %(lugar)s, fecha = %(fecha)s, descripcion = %(descripcion)s
            WHERE id = %(id)s;
        """
        return connectToMySQL('esquema_publicaciones').query_db(query, datos)

    @classmethod
    def borrar(cls, datos):
        query = "DELETE FROM publicaciones WHERE id = %(id)s;"
        return connectToMySQL('esquema_publicaciones').query_db(query, datos)

    @classmethod
    def agregar_me_gusta(cls, datos):
        query = "INSERT IGNORE INTO me_gustas (usuario_id, publicacion_id) VALUES (%(usuario_id)s, %(publicacion_id)s);"
        return connectToMySQL('esquema_publicaciones').query_db(query, datos)

    @staticmethod
    def validar_publicacion(formulario, publicacion=None):
        es_valido = True
        nombre = formulario.get('nombre', '').strip()
        lugar = formulario.get('lugar', '').strip()
        fecha = formulario.get('fecha', '').strip()
        descripcion = formulario.get('descripcion', '').strip()

        if not nombre:
            flash("El nombre es obligatorio", "publicacion")
            es_valido = False
        else:
            existente = Publicacion.buscar_por_nombre({'nombre': nombre})
            if existente and not publicacion:
                flash("El nombre ya está registrado. Debe ser único.", "publicacion")
                es_valido = False
            if publicacion and publicacion.nombre != nombre:
                flash("El nombre no puede modificarse.", "publicacion")
                es_valido = False
        if not lugar:
            flash("El lugar es obligatorio", "publicacion")
            es_valido = False

        if not fecha:
            flash("La fecha es obligatoria", "publicacion")
            es_valido = False

        if not descripcion:
            flash("La descripción no puede estar vacía", "publicacion")
            es_valido = False

        return es_valido