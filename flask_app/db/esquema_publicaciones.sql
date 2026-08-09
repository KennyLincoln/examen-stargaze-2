-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema esquema_publicaciones
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema esquema_publicaciones
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `esquema_publicaciones` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci ;
USE `esquema_publicaciones` ;

-- -----------------------------------------------------
-- Table `esquema_publicaciones`.`usuarios`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `esquema_publicaciones`.`usuarios` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(255) NOT NULL,
  `apellido` VARCHAR(255) NOT NULL,
  `email` VARCHAR(255) NOT NULL,
  `password` VARCHAR(255) NOT NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `esquema_publicaciones`.`publicaciones`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `esquema_publicaciones`.`publicaciones` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(255) NOT NULL,
  `lugar` VARCHAR(255) NOT NULL,
  `fecha` DATE NOT NULL,
  `descripcion` TEXT NOT NULL,
  `usuario_id` INT NOT NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  INDEX `fk_publicaciones_usuarios_idx` (`usuario_id` ASC) VISIBLE,
  CONSTRAINT `fk_publicaciones_usuarios`
    FOREIGN KEY (`usuario_id`)
    REFERENCES `esquema_publicaciones`.`usuarios` (`id`)
    ON DELETE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `esquema_publicaciones`.`me_gustas`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `esquema_publicaciones`.`me_gustas` (
  `usuario_id` INT NOT NULL,
  `publicacion_id` INT NOT NULL,
  PRIMARY KEY (`usuario_id`, `publicacion_id`),
  INDEX `fk_me_gustas_publicaciones1_idx` (`publicacion_id` ASC) VISIBLE,
  INDEX `fk_me_gustas_usuarios1_idx` (`usuario_id` ASC) VISIBLE,
  CONSTRAINT `fk_me_gustas_publicaciones1`
    FOREIGN KEY (`publicacion_id`)
    REFERENCES `esquema_publicaciones`.`publicaciones` (`id`)
    ON DELETE CASCADE,
  CONSTRAINT `fk_me_gustas_usuarios1`
    FOREIGN KEY (`usuario_id`)
    REFERENCES `esquema_publicaciones`.`usuarios` (`id`)
    ON DELETE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
