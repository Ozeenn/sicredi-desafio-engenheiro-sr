CREATE SCHEMA IF NOT EXISTS engsr_desafio;

CREATE TABLE IF NOT EXISTS engsr_desafio.associado
(
    id integer NOT NULL,
    nome character varying(100) COLLATE pg_catalog."default",
    sobrenome character varying(100) COLLATE pg_catalog."default",
    idade integer,
    email character varying(100) COLLATE pg_catalog."default",
    CONSTRAINT associado_pkey PRIMARY KEY (id)
);
	
CREATE TABLE IF NOT EXISTS engsr_desafio.conta
(
    id integer NOT NULL,
    tpo_conta character varying(100) COLLATE pg_catalog."default",
    data_criacao timestamp with time zone,
    id_associado integer,
    CONSTRAINT conta_pkey PRIMARY KEY (id),
    CONSTRAINT fk_associado FOREIGN KEY (id_associado)
        REFERENCES engsr_desafio.associado (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
);

	
CREATE TABLE IF NOT EXISTS engsr_desafio.cartao
(
    id integer NOT NULL,
    num_cartao bigint,
    nom_impresso character varying(100) COLLATE pg_catalog."default",
    id_conta integer,
    id_associado integer,
    CONSTRAINT cartao_pkey PRIMARY KEY (id),
    CONSTRAINT cartao_id_associado_fkey FOREIGN KEY (id_associado)
        REFERENCES engsr_desafio.associado (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT cartao_id_conta_fkey FOREIGN KEY (id_conta)
        REFERENCES engsr_desafio.conta (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
);
	
CREATE TABLE IF NOT EXISTS engsr_desafio.movimento
(
    id integer NOT NULL,
    vlr_transacao numeric(10,2),
    des_transacao character varying(100) COLLATE pg_catalog."default",
    dat_movimento timestamp with time zone,
    id_cartao integer,
    CONSTRAINT movimento_pkey PRIMARY KEY (id),
    CONSTRAINT fk_cartao FOREIGN KEY (id_cartao)
        REFERENCES engsr_desafio.cartao (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
);

	
insert into engsr_desafio.associado(id, nome, sobrenome, idade, email)
values
	(32,'Roberto','Carlos',43,'roberto_carlos@gmail.com'),
	(4,'Michael','Jackson',23,'michael_jackson@gmail.com'),
	(5,'Rodrigo','Faro',45,'rodrigo_faro@gmail.com'),
	(2,'Xuxa','Meneghel',67,'xuxa_meneghel@gmail.com'),
	(12,'Ivete','Sangalo',24,'ivete_sangalo@gmail.com'),
	(8,'Evandro','Gonzales',31,'evandro_gonzales@gmail.com'),
	(1,'Aldair','Faustino',19,'aldair_faustino@gmail.com'),
	(6,'Andre','Vitor',24,'andre_vitor@gmail.com');
	
insert into engsr_desafio.conta(id, tpo_conta, data_criacao, id_associado)
values
	(5,	'Corrente'	,'2001-01-04 10:27:03',	32),
	(3	,'Corrente'	,'2004-01-23 05:27:14',	4),
	(7	,'Poupanca'	,'2006-11-20 11:26:20',	5),
	(66	,'Poupanca'	,'2000-12-17 21:37:02',	2),
	(2	,'Corrente'	,'2009-06-27 15:10:10',	12),
	(11	,'Corrente'	,'2004-11-02 06:15:24',	8),
	(4	,'Corrente'	,'2000-10-09 03:12:55',	1),
	(1	,'Corrente'	,'2013-07-31 20:23:50',	6);
	
insert into engsr_desafio.cartao(id, num_cartao, nom_impresso, id_conta, id_associado)
values
	(2,	5557291447147510	,'Roberto Carlos'	,5	,32),
	(3	,5377600436389940	,'Michael Jackson',	3,	4),
	(5	,4485617103568280	,'Rodrigo Faro'	,7	,5),
	(9	,5182059291395190	,'Xuxa Meneghel'	,66	,2),
	(7	,4539337001555730	,'Ivete Sangalo'	,2	,12),
	(1	,5498244324705310	,'Evandro Gonzales',	11	,8),
	(96	,4916111159632360	,'Aldair Faustino'	,4	,1),
	(6	,4929384070267770	,'Andre Vitor'	,1	,6);
	
insert into engsr_desafio.movimento(id, vlr_transacao, des_transacao, dat_movimento, id_cartao)
values
	(1,	200,	'Credito',	'2001-08-04 01:57:36'	,2),
	(2,	195.4,	'Debito'	,'2014-10-23 07:40:12'	,3),
	(3,	10,	'Debito'	,'2018-09-23 10:34:24'	,5),
	(4,	54,	'Debito'	,'2002-03-26 09:19:01'	,9),
	(5,	1945.67,	'Credito',	'2024-07-09 22:03:41'	,7),
	(6,	753,	'Credito'	,'2005-01-07 02:04:18'	,1),
	(7,	43,	'Debito'	,'2004-11-19 09:35:08'	,96),
	(8,	839,	'Credito',	'2023-10-30 03:30:03'	,6);