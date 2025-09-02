CREATE DATABASE Titulacion_2025
USE Titulacion_2025

-- TABLA MODALIDAD
CREATE TABLE Modalidad
(
    Id_modalidad CHAR(3) PRIMARY KEY,
    Nombre_modalidad VARCHAR(50) NOT NULL
);

-- TABLA PROFESOR
CREATE TABLE Profesor
(
    Id_profesor CHAR(6) PRIMARY KEY,
    Nombre_profesor VARCHAR(80) NOT NULL
);

-- TABLA FACULTAD
CREATE TABLE Facultad
(
    Id_facultad CHAR(6) PRIMARY KEY,
    Nombre_facultad VARCHAR(80) NOT NULL
);

-- TABLA CARRERA
CREATE TABLE Carrera
(
    Id_carrera CHAR(6) PRIMARY KEY,
    Nombre_carrera VARCHAR(80) NOT NULL,
    Id_facultad CHAR(6) NOT NULL,
    CONSTRAINT FK_Carrera_Facultad FOREIGN KEY (Id_facultad) 
        REFERENCES Facultad(Id_facultad)
);

-- TABLA ESTUDIANTE
CREATE TABLE Estudiante
(
    Id_estudiante CHAR(6) PRIMARY KEY,
    Nombre_estudiante VARCHAR(80) NOT NULL,
    Generacion CHAR(9) NOT NULL,
    Id_carrera CHAR(6) NOT NULL,
    CONSTRAINT FK_Estudiante_Carrera FOREIGN KEY (Id_carrera) 
        REFERENCES Carrera(Id_carrera)
);

-- TABLA TITULACION
CREATE TABLE Titulacion
(
    Id_titulacion CHAR(6) PRIMARY KEY,
    Id_estudiante CHAR(6) UNIQUE NOT NULL,
    Id_modalidad CHAR(3) NOT NULL,
    Nombre_proyecto VARCHAR(100) NULL,
    Fecha_titulacion DATE NOT NULL,
    CONSTRAINT FK_Titulacion_Estudiante FOREIGN KEY (Id_estudiante) 
        REFERENCES Estudiante(Id_estudiante),
    CONSTRAINT FK_Titulacion_Modalidad FOREIGN KEY (Id_modalidad) 
        REFERENCES Modalidad(Id_modalidad)
);

-- TABLA TITULACION_PROFESOR
CREATE TABLE Titulacion_Profesor
(
    Id_titulacion CHAR(6) NOT NULL,
    Id_profesor CHAR(6) NOT NULL,
    Rol VARCHAR(30) NOT NULL,
    CONSTRAINT PK_TitulacionProfesor PRIMARY KEY (Id_titulacion, Id_profesor, Rol),
    CONSTRAINT FK_TitulacionProfesor_Titulacion FOREIGN KEY (Id_titulacion) 
        REFERENCES Titulacion(Id_titulacion),
    CONSTRAINT FK_TitulacionProfesor_Profesor FOREIGN KEY (Id_profesor) 
        REFERENCES Profesor(Id_profesor)
);