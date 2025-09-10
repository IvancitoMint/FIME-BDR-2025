SELECT * FROM Estudiante
SELECT * FROM Titulacion
SELECT * FROM Titulacion_Profesor

SELECT * FROM Profesor

DELETE FROM Titulacion_Profesor
WHERE Id_titulacion = '202104'

DELETE FROM Titulacion
WHERE Id_titulacion = '202104'

DELETE FROM Estudiante
WHERE Id_estudiante = '202104'