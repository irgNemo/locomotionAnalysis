create table if not exist segment(id integer, segmento text, CONSTRAINT pk PRIMARY KEY(id));
create table if not exist subject(id integer, subject text, CONSTRAINT pk PRIMARY KEY(id));
create table if not exist treatment(id integer, treatment_abv text, treatment_description text, CONSTRAINT pk PRIMARY KEY(id));
create table if not exist step(segment integer, subject integer, treatment integer, time integer, angle numeric, CONSTRAINT fk_segment FOREIGN KEY(segment), CONSTRAINT fk_subject FOREING KEY(subject), CONSTRAINT fk_treatment FOREIGN KEY(treatment));

insert into table segment(1, 'rodilla izquierda');
insert into table segment(2, 'rodilla derecha');
insert into table segment(3, 'cadera izquierda');
insert into table segment(4, 'cadera derecha');
insert into table segment(5, 'pendulo izquierdo');
insert into table segment(6, 'pendulo derecho');
insert into table segment(7, 'tobillo izquierdo');
insert into table segment(8, 'tobillo derecho');

insert into table subject(1, 'R1');
insert into table subject(2, 'R2');
insert into table subject(3, 'R3');
insert into table subject(4, 'R4');
insert into table subject(5, 'R5');
insert into table subject(6, 'R6');

insert into table treatment(1, 'ST', '');
insert into table treatment(2, 'TMX', '');
insert into table treatment(3, 'EJE', '');
insert into table treatment(4, 'TE', '');
insert into table treatment(5, 'VH', '');
insert into table treatment(6, 'CT', '');
