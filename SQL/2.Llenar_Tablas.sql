INSERT INTO Modalidad (Id_modalidad, nombre_modalidad)
VALUES
	('MD1', 'Tesis'),
	('MD2', 'Tesisina'),
	('MD3', 'Articulo de investigacion'),
	('MD4', 'Obra artistica'),
	('MD5', 'Sistematizacion de experiencia laboral'),
	('MD6', 'Examen general de egreso'),
	('MD7', 'Desempeno academico soresaliente'),
	('MD8', 'Certificacion profesional'),
	('MD9', 'Actualizacion de conocimientos');

INSERT INTO Profesor (Id_profesor, Nombre_profesor)
VALUES
	('PRF001', 'Gaytan Lugo Laura Sanely'),
	('PRF002', 'Castillo Topete Visctor Hugo'),
	('PRF003', 'Carrillo Zepeda Oswaldo'),
	('PRF004', 'Evangekista Salazar Martha Elizabeth'),
	('PRF005', 'Gonzalez Potes Apolinar'),
	('PRF006', 'Benavides Sanchez Luis Daniel'),
	('PRF007', 'Martinez Camarena Edgar'),
	('PRF008', 'Velazquez Gonzalez Cruz Ernesto'),
	('PRF009', 'Mata Lopez Walter Alexander'),
	('PRF010', 'Soto Ochoa Francisco Manuel'),
	('PRF011', 'Diaz Hernandez Juan Antonio'),
	('PRF012', 'Bricio Chapula Carlos Adrian'),
	('PRF013', 'Santiago Hernandez Elizabeth'),
	('PRF014', 'Cardenas Rodriguez Selene'),
	('PRF015', 'Nava Bautista Martha Xochitl');

INSERT INTO Facultad (Id_facultad, Nombre_facultad)
VALUES
	('FCD001', 'Facultad de Ciencias de la educacion'),
	('FCD002', 'Facultad de Telematica'),
	('FCD003', 'Facultad de Contabilidad y Administracion'),
	('FCD004', 'Facultad de Derecho'),
	('FCD005', 'Facultad de Enfermeria'),
	('FCD006', 'Facultad de Medicina'),
	('FCD007', 'Facultad de Arquitectura y Diseño'),
	('FCD008', 'Facultad de Ciencias Quimicas'),
	('FCD009', 'Facultad de Ingenieria Civil'),
	('FCD010', 'Facultad de Ingenieria Mecanica y Electrica');

INSERT INTO Carrera (Id_carrera, Nombre_carrera, Id_facultad)
VALUES
	('CRR001', 'Licenciatura en Enseñanza de las Matematicas', 'FCD001'),
	('CRR002', 'Licenciatura en Educacion Especial', 'FCD001'),
	('CRR003', 'Ingenieria de Software', 'FCD002'),
	('CRR004', 'Ingenieria en Tecnologias de Internet', 'FCD002'),
	('CRR005', 'Licenciatura en Contador Publico', 'FCD003'),
	('CRR006', 'Licenciatura en Administracion', 'FCD003'),
	('CRR007', 'Licenciatura en Derecho', 'FCD004'),
	('CRR008', 'Licenciatura en Enfermeria', 'FCD005'),
	('CRR009', 'Licenciatura en Nutricion', 'FCD006'),
	('CRR010', 'Licenciatura en Medico Cirujano y Partero', 'FCD006'),
	('CRR011', 'Licenciatura en Arquitectura', 'FCD007'),
	('CRR012', 'Licenciatura en Diseño Grafico', 'FCD007'),
	('CRR013', 'Licenciatura en Diseño Industrial', 'FCD007'),
	('CRR014', 'Ingenieria Quimica Metalurgica', 'FCD008'),
	('CRR015', 'Ingeniero Quimico en Alimentos', 'FCD008'),
	('CRR016', 'Licenciatura en Quimico Farmaceutico Biologo', 'FCD008'),
	('CRR017', 'Ingenieria Civil', 'FCD009'),
	('CRR018', 'Ingenieria en Computacion Inteligente', 'FCD010'),
	('CRR019', 'Ingenieria en Mecatronica', 'FCD010'),
	('CRR020', 'Ingeniero Mecanico Electrico', 'FCD010');