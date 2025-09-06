USE Titulacion_2025

-- 1. Obtén la informacion de los estudiantes que se encuentran en la carrera de Licenciatura en Diseño Grafico
-- y que tienen fecha de titulacion del 2026-05-15
SELECT DISTINCT Estudiante.Id_estudiante, Estudiante.Nombre_estudiante, Facultad.Nombre_facultad, Carrera.Nombre_carrera, Titulacion.Fecha_titulacion 
FROM Estudiante, Carrera, Facultad, Profesor, Modalidad, Titulacion, Titulacion_Profesor
WHERE Estudiante.Id_estudiante = Titulacion.Id_estudiante
AND Carrera.Id_carrera = Estudiante.Id_carrera
AND Carrera.Id_facultad = Facultad.Id_facultad
AND Modalidad.Id_modalidad = Titulacion.Id_modalidad
AND Titulacion_Profesor.Id_titulacion = Titulacion.Id_titulacion
AND Titulacion_Profesor.Id_profesor = Profesor.Id_profesor
AND Titulacion.Fecha_titulacion = '2026-05-15'
AND Carrera.Nombre_carrera = 'Licenciatura en Diseño Grafico'

-- 2. Selecciona Los maestros que tienen el rol de co-asesor en titulaciones con modalidad "Tesis"
SELECT DISTINCT Profesor.Nombre_profesor, Titulacion_Profesor.Rol, Titulacion.Nombre_proyecto, Modalidad.Nombre_modalidad
FROM Estudiante, Carrera, Facultad, Profesor, Modalidad, Titulacion, Titulacion_Profesor
WHERE Estudiante.Id_estudiante = Titulacion.Id_estudiante
AND Carrera.Id_carrera = Estudiante.Id_carrera
AND Carrera.Id_facultad = Facultad.Id_facultad
AND Modalidad.Id_modalidad = Titulacion.Id_modalidad
AND Titulacion_Profesor.Id_titulacion = Titulacion.Id_titulacion
AND Titulacion_Profesor.Id_profesor = Profesor.Id_profesor
AND Titulacion_Profesor.Rol = 'Co-asesor'
AND Modalidad.Nombre_modalidad = 'Tesis'

-- 3. Selecciona la facultad con mayor numero de titulados por Articulo de investigacion
SELECT TOP 1 Facultad.Nombre_facultad, COUNT(Modalidad.Nombre_modalidad) as Total
FROM Estudiante, Carrera, Facultad, Profesor, Modalidad, Titulacion, Titulacion_Profesor
WHERE Estudiante.Id_estudiante = Titulacion.Id_estudiante
AND Carrera.Id_carrera = Estudiante.Id_carrera
AND Carrera.Id_facultad = Facultad.Id_facultad
AND Modalidad.Id_modalidad = Titulacion.Id_modalidad
AND Titulacion_Profesor.Id_titulacion = Titulacion.Id_titulacion
AND Titulacion_Profesor.Id_profesor = Profesor.Id_profesor
AND Modalidad.Nombre_modalidad = 'Articulo de investigacion'
GROUP BY Facultad.Nombre_facultad
ORDER BY COUNT(Modalidad.Nombre_modalidad) DESC

-- 4. Selecciona La carrera que tenga mas titulados por Obra artistica
SELECT TOP 1 Facultad.Nombre_facultad, COUNT(Modalidad.Nombre_modalidad) as Total
FROM Estudiante, Carrera, Facultad, Profesor, Modalidad, Titulacion, Titulacion_Profesor
WHERE Estudiante.Id_estudiante = Titulacion.Id_estudiante
AND Carrera.Id_carrera = Estudiante.Id_carrera
AND Carrera.Id_facultad = Facultad.Id_facultad
AND Modalidad.Id_modalidad = Titulacion.Id_modalidad
AND Titulacion_Profesor.Id_titulacion = Titulacion.Id_titulacion
AND Titulacion_Profesor.Id_profesor = Profesor.Id_profesor
AND Modalidad.Nombre_modalidad = 'Obra artistica'
GROUP BY Facultad.Nombre_facultad
ORDER BY COUNT(Modalidad.Nombre_modalidad) DESC

-- 5. Selecciona las titulaciones de la Fecha "2025-07-19" donde el maestro "Benavides Sanchez Luis Daniel" haya participado como "asesor"
SELECT DISTINCT Profesor.Nombre_profesor, Titulacion_Profesor.Rol, Titulacion.Nombre_proyecto, Titulacion.Fecha_titulacion 
FROM Estudiante, Carrera, Facultad, Profesor, Modalidad, Titulacion, Titulacion_Profesor
WHERE Estudiante.Id_estudiante = Titulacion.Id_estudiante
AND Carrera.Id_carrera = Estudiante.Id_carrera
AND Carrera.Id_facultad = Facultad.Id_facultad
AND Modalidad.Id_modalidad = Titulacion.Id_modalidad
AND Titulacion_Profesor.Id_titulacion = Titulacion.Id_titulacion
AND Titulacion_Profesor.Id_profesor = Profesor.Id_profesor
AND Titulacion.Fecha_titulacion = '2025-07-19'
AND Profesor.Nombre_profesor = 'Benavides Sanchez Luis Daniel'
AND Titulacion_Profesor.Rol = 'Asesor'