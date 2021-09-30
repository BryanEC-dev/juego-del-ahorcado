create database words;
use words;

create table words(word varchar(100) unique, first_track varchar(200), second_track varchar(200), third_track varchar(200));
insert into words  values('deporte', 'Se puede realizar al aire libre o en interiores', 'Tiene un conjunto de normas','Se puede usar los músculos o el cerebro');
insert into words  values('isquiotibial', 'Es un músculo', 'Se encuentra en el tren inferior','Facilita la extensión de la pierna');
insert into words  values('meditar', 'produce un estado de relajamiento', 'Contribuye al bienestar físico','Interviene la mente y el cuerpo');
insert into words  values('asana', 'palabra usada en el yoga', 'es el nombre de las posturas corporales','Fortalece las extremidades');
insert into words  values('keratina', 'Es una proteína que genera nuestro cuerpo', 'Nutre nuestro cabello','Repara nuestro cabello');
insert into words  values('arena', 'conjunto de fracmentos sueltos de roca', 'la particula individual se llama grano','se encuentran en las costas');
insert into words  values('dormir', 'Se puede hacer parado', 'Se puede hacer en la cama','es uno de los placeres de la vida');
insert into words  values('tablet', 'dispositivo electronico', 'su pantalla es más grande que la de los teléfonos','perfecto para leer');
insert into words  values('baloncesto', 'uno de los deportes más practicados del mundo', 'tiene cuatro periodos','puedes anotar 1,2 o 3 puntos');

create table points(first_name varchar(100),score numeric, creation_date TIMESTAMP default CURRENT_TIMESTAMP);

