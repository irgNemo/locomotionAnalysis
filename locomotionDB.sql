create table if not exists segment(id integer, segmento text, CONSTRAINT pk PRIMARY KEY(id));
create table if not exists subject(id integer, subject text, CONSTRAINT pk PRIMARY KEY(id));
create table if not exists treatment(id integer, treatment_abv text, treatment_description text, CONSTRAINT pk PRIMARY KEY(id));
create table if not exists step(id_segment integer, id_subject integer, id_treatment integer, time_elapsed integer, step_number integer, angle numeric, status text, CONSTRAINT pk PRIMARY KEY(id_segment, id_subject, id_treatment, time_elapsed, step_number), CONSTRAINT fk_segment FOREIGN KEY(id_segment) REFERENCES segment(id), CONSTRAINT fk_subject FOREIGN KEY(id_subject) REFERENCES subject(id), CONSTRAINT fk_treatment FOREIGN KEY(id_treatment) REFERENCES treatment(id));

insert into segment values(1, 'rodilla izquierda');
insert into segment values(2, 'rodilla derecha');
insert into segment values(3, 'cadera izquierda');
insert into segment values(4, 'cadera derecha');
insert into segment values(5, 'pendulo izquierdo');
insert into segment values(6, 'pendulo derecho');
insert into segment values(7, 'tobillo izquierdo');
insert into segment values(8, 'tobillo derecho');

insert into subject values(1, 'R1');
insert into subject values(2, 'R2');
insert into subject values(3, 'R3');
insert into subject values(4, 'R4');
insert into subject values(5, 'R5');
insert into subject values(6, 'R6');

insert into treatment values(1, 'ST', '');
insert into treatment values(2, 'TMX', '');
insert into treatment values(3, 'EJE', 'Ejercicio');
insert into treatment values(4, 'TE', '');
insert into treatment values(5, 'VH', '');
insert into treatment values(6, 'CT', 'Control');
