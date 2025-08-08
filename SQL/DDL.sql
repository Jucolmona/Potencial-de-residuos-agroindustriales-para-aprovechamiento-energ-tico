CREATE DATABASE aprovechamiento_energia;
USE aprovechamiento_energia;

-- CREACIÓN DE TABLA DE DEPARTAMENTOS
CREATE TABLE departamentos(
	id_departamento INT PRIMARY KEY AUTO_INCREMENT,
	nombre_departamento VARCHAR(100) NOT NULL, 
	codigo_departamento INT NOT NULL UNIQUE
);

-- CREACIÓN DE TABLA MUNICIPIOS
CREATE TABLE municipios(
	id_municipio INT PRIMARY KEY AUTO_INCREMENT,
	id_departamento INT NOT NULL,
	nombre_municipio VARCHAR(100) NOT NULL,
	codigo_municipio INT NOT NULL UNIQUE,
	FOREIGN KEY (id_departamento) REFERENCES departamentos(id_departamento)
);

-- CREACION DE TABLA GRUPO DE CULTIVOS
CREATE TABLE grupo_cultivo(
	id_grupo_cultivo INT PRIMARY KEY AUTO_INCREMENT,
	grupo_cultivo VARCHAR(100) NOT NULL
);

-- CREACION DE TABLA CULTIVO
CREATE TABLE cultivo(
	id_cultivo INT PRIMARY KEY AUTO_INCREMENT,
	id_grupo_cultivo INT NOT NULL,
	nombre_cultivo VARCHAR(100) NOT NULL,
	FOREIGN KEY (id_grupo_cultivo) REFERENCES grupo_cultivo(id_grupo_cultivo)
);

-- TABLA CULTIVO PERIODO
CREATE TABLE cultivo_periodo(
	id_cultivo_periodo INT PRIMARY KEY AUTO_INCREMENT,
	id_cultivo INT NOT NULL,
	id_municipio INT NOT NULL,
	periodo VARCHAR(50) NOT NULL,
	area_sembrada DECIMAL(10, 2) NOT NULL,
	area_cosechada DECIMAL(10,2) NOT NULL,
	produccion DECIMAL(10, 2) NOT NULL,
	rendimiento DECIMAL(10, 2) NOT NULL,
	ciclo_cultivo VARCHAR(50),
	FOREIGN KEY (id_cultivo) REFERENCES cultivo(id_cultivo),
	FOREIGN KEY (id_municipio) REFERENCES municipios(id_municipio)
);

-- TABLA TIPO OPERACION PLANTA ELECTRICA
CREATE TABLE tipo_operacion(
	id_tipo_operacion INT PRIMARY KEY AUTO_INCREMENT,
	nombre_tipo_operacion VARCHAR(100) NOT NULL
);

-- TABLA OPERADOR
CREATE TABLE operador(
	id_operador INT PRIMARY KEY AUTO_INCREMENT,
	nombre_operador VARCHAR(100) NOT NULL
);

-- TABLA SUBAREA
CREATE TABLE sub_area (
    id_sub_area INT PRIMARY KEY AUTO_INCREMENT,
    nombre_sub_area VARCHAR(100) NOT NULL
);

-- PLANTA DE GENERACION
CREATE TABLE planta_generacion (
    id_planta INT PRIMARY KEY AUTO_INCREMENT,
    id_tipo_operacion INT NOT NULL,
    id_operador INT NOT NULL,
    id_sub_area INT NOT NULL,
    id_municipio INT NOT NULL,
    nombre_planta VARCHAR(100) NOT NULL,
    capacidad_neta DECIMAL(10,2) NOT NULL,
    inicio_operacion DATE,
    FOREIGN KEY (id_tipo_operacion) REFERENCES tipo_operacion(id_tipo_operacion),
    FOREIGN KEY (id_operador) REFERENCES operador(id_operador),
    FOREIGN KEY (id_sub_area) REFERENCES sub_area(id_sub_area),
    FOREIGN KEY (id_municipio) REFERENCES municipios(id_municipio)
);

-- TABLA FUENTE DE BIOMASA
CREATE TABLE fuente_biomasa (
    id_fuente_biomasa INT PRIMARY KEY AUTO_INCREMENT,
    nombre_fuente_biomasa VARCHAR(100) NOT NULL
);

-- TABLA TIPO DE RESIDUO
CREATE TABLE tipo_residuo (
    id_tipo_residuo INT PRIMARY KEY AUTO_INCREMENT,
    id_fuente_biomasa INT NOT NULL,
    nombre_tipo_residuo VARCHAR(100) NOT NULL,
    FOREIGN KEY (id_fuente_biomasa) REFERENCES fuente_biomasa(id_fuente_biomasa)
);

-- TABLA PARAMETROS DE BIOMASA
CREATE TABLE parametros_biomasa (
    id_parametros_biomasa INT PRIMARY KEY AUTO_INCREMENT,
    id_fuente_biomasa INT NOT NULL,
    id_tipo_residuo INT NOT NULL,
    factor_residuo DECIMAL(10,4) NOT NULL,
    fraccion_residuo DECIMAL(10,4) NOT NULL,
    pci DECIMAL(10,2) NOT NULL,
    yrs DECIMAL(10,2) NOT NULL,
    FOREIGN KEY (id_fuente_biomasa) REFERENCES fuente_biomasa(id_fuente_biomasa),
    FOREIGN KEY (id_tipo_residuo) REFERENCES tipo_residuo(id_tipo_residuo)
);

