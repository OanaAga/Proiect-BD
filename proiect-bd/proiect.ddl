-- Generated by Oracle SQL Developer Data Modeler 20.3.0.283.0710
--   at:        2022-12-15 09:39:13 EET
--   site:      Oracle Database 11g
--   type:      Oracle Database 11g



-- predefined type, no DDL - MDSYS.SDO_GEOMETRY

-- predefined type, no DDL - XMLTYPE

CREATE TABLE ambalaje (
    esenta_id_parfum  NUMBER(4) NOT NULL,
    id_ambalaj        NUMBER(4) NOT NULL,
    stoc              NUMBER(4),
    pret              NUMBER(4) NOT NULL,
    gramaj            NUMBER(3) NOT NULL
);

ALTER TABLE ambalaje ADD CONSTRAINT ambalaje_pk PRIMARY KEY ( id_ambalaj );

ALTER TABLE ambalaje ADD CONSTRAINT ambalaje_id_parfum_gramaj_un UNIQUE ( esenta_id_parfum,
                                                                          gramaj );

CREATE TABLE cereri (
    nr_comanda                    NUMBER(4) NOT NULL,
    distribuitor_id_distribuitor  NUMBER(4) NOT NULL,
    ambalaje_id_ambalaj           NUMBER(4) NOT NULL,
    nr_bucati                     NUMBER(4) NOT NULL,
    data                          DATE NOT NULL
);

CREATE TABLE distribuitor (
    id_distribuitor  NUMBER(4) NOT NULL,
    nume_distr       VARCHAR2(30) NOT NULL
);

ALTER TABLE distribuitor
    ADD CONSTRAINT distribuitor_nume_distr CHECK ( REGEXP_LIKE ( nume_distr,
                                                                 '^[A-Za-z]+((\s)?([A-Za-z])+)*$' ) );

ALTER TABLE distribuitor ADD CONSTRAINT distribuitor_pk PRIMARY KEY ( id_distribuitor );

ALTER TABLE distribuitor ADD CONSTRAINT distribuitor_nume_distr_un UNIQUE ( nume_distr );

CREATE TABLE esenta (
    id_parfum    NUMBER(4) NOT NULL,
    nume_parfum  VARCHAR2(30) NOT NULL
);

ALTER TABLE esenta
    ADD CONSTRAINT "produs final_Nume_parfum_ck" CHECK ( REGEXP_LIKE ( nume_parfum,
                                                                       '^[A-Za-z]+((\s)?([a-z])+)*$' ) );

ALTER TABLE esenta ADD CONSTRAINT esenta_pk PRIMARY KEY ( id_parfum );

ALTER TABLE esenta ADD CONSTRAINT esenta_nume_parfum_un UNIQUE ( nume_parfum );

CREATE TABLE formula (
    esenta_id_parfum           NUMBER(4) NOT NULL,
    ingrediente_id_ingredient  NUMBER(4) NOT NULL,
    procent                    NUMBER(2) NOT NULL
);

ALTER TABLE formula ADD CONSTRAINT formula_pk PRIMARY KEY ( esenta_id_parfum,
                                                            ingrediente_id_ingredient );

CREATE TABLE info (
    esenta_id_parfum  NUMBER(4) NOT NULL,
    gen               VARCHAR2(10) NOT NULL,
    tip               VARCHAR2(15) NOT NULL,
    link_poza         VARCHAR2(100) NOT NULL
);

ALTER TABLE info
    ADD CONSTRAINT info_gen_ck CHECK ( REGEXP_LIKE ( gen,
                                                     '^[A-Za-z]+$' ) );

ALTER TABLE info
    ADD CONSTRAINT info_tip_ck CHECK ( REGEXP_LIKE ( tip,
                                                     '^[A-Za-z]+$' ) );

ALTER TABLE info
    ADD CONSTRAINT info_link_poza CHECK ( REGEXP_LIKE ( link_poza,
                                                        '^(http:\/\/www\.|https:\/\/www\.|http:\/\/|https:\/\/)?[a-z0-9]+([\-\.]{1}[a-z0-9]+)*\.[a-z]{2,5}(:[0-9]{1,5})?(\/.*)?$' ) );

ALTER TABLE info ADD CONSTRAINT info_id_parfum_un UNIQUE ( esenta_id_parfum );

CREATE TABLE ingrediente (
    id_ingredient    NUMBER(4) NOT NULL,
    nume_ingredient  VARCHAR2(30) NOT NULL,
    cantitate        NUMBER(6)
);

ALTER TABLE ingrediente
    ADD CONSTRAINT ingrediente_nume_ingredient_ck CHECK ( REGEXP_LIKE ( nume_ingredient,
                                                                        '^[A-Za-z]+((\s)?([a-z])+)*$' ) );

ALTER TABLE ingrediente ADD CONSTRAINT ingrediente_pk PRIMARY KEY ( id_ingredient );

ALTER TABLE ingrediente ADD CONSTRAINT ingrediente_nume_ingredient_un UNIQUE ( nume_ingredient );

ALTER TABLE ambalaje
    ADD CONSTRAINT ambalaje_esenta_fk FOREIGN KEY ( esenta_id_parfum )
        REFERENCES esenta ( id_parfum );

ALTER TABLE cereri
    ADD CONSTRAINT cereri_ambalaje_fk FOREIGN KEY ( ambalaje_id_ambalaj )
        REFERENCES ambalaje ( id_ambalaj );

ALTER TABLE cereri
    ADD CONSTRAINT cereri_distribuitor_fk FOREIGN KEY ( distribuitor_id_distribuitor )
        REFERENCES distribuitor ( id_distribuitor );

ALTER TABLE formula
    ADD CONSTRAINT formula_esenta_fk FOREIGN KEY ( esenta_id_parfum )
        REFERENCES esenta ( id_parfum );

ALTER TABLE formula
    ADD CONSTRAINT formula_ingrediente_fk FOREIGN KEY ( ingrediente_id_ingredient )
        REFERENCES ingrediente ( id_ingredient );

ALTER TABLE info
    ADD CONSTRAINT info_esenta_fk FOREIGN KEY ( esenta_id_parfum )
        REFERENCES esenta ( id_parfum );

CREATE SEQUENCE ambalaje_id_ambalaj_seq START WITH 1000 NOCACHE ORDER;

CREATE OR REPLACE TRIGGER ambalaje_id_ambalaj_trg BEFORE
    INSERT ON ambalaje
    FOR EACH ROW
    WHEN ( new.id_ambalaj IS NULL )
BEGIN
    :new.id_ambalaj := ambalaje_id_ambalaj_seq.nextval;
END;
/

CREATE SEQUENCE distribuitor_id_distribuitor START WITH 100 NOCACHE ORDER;

CREATE OR REPLACE TRIGGER distribuitor_id_distribuitor BEFORE
    INSERT ON distribuitor
    FOR EACH ROW
    WHEN ( new.id_distribuitor IS NULL )
BEGIN
    :new.id_distribuitor := distribuitor_id_distribuitor.nextval;
END;
/

CREATE SEQUENCE esenta_id_parfum_seq START WITH 2000 NOCACHE ORDER;

CREATE OR REPLACE TRIGGER esenta_id_parfum_trg BEFORE
    INSERT ON esenta
    FOR EACH ROW
    WHEN ( new.id_parfum IS NULL )
BEGIN
    :new.id_parfum := esenta_id_parfum_seq.nextval;
END;
/

CREATE SEQUENCE ingrediente_id_ingredient_seq START WITH 3000 NOCACHE ORDER;

CREATE OR REPLACE TRIGGER ingrediente_id_ingredient_trg BEFORE
    INSERT ON ingrediente
    FOR EACH ROW
    WHEN ( new.id_ingredient IS NULL )
BEGIN
    :new.id_ingredient := ingrediente_id_ingredient_seq.nextval;
END;
/



-- Oracle SQL Developer Data Modeler Summary Report: 
-- 
-- CREATE TABLE                             7
-- CREATE INDEX                             0
-- ALTER TABLE                             22
-- CREATE VIEW                              0
-- ALTER VIEW                               0
-- CREATE PACKAGE                           0
-- CREATE PACKAGE BODY                      0
-- CREATE PROCEDURE                         0
-- CREATE FUNCTION                          0
-- CREATE TRIGGER                           4
-- ALTER TRIGGER                            0
-- CREATE COLLECTION TYPE                   0
-- CREATE STRUCTURED TYPE                   0
-- CREATE STRUCTURED TYPE BODY              0
-- CREATE CLUSTER                           0
-- CREATE CONTEXT                           0
-- CREATE DATABASE                          0
-- CREATE DIMENSION                         0
-- CREATE DIRECTORY                         0
-- CREATE DISK GROUP                        0
-- CREATE ROLE                              0
-- CREATE ROLLBACK SEGMENT                  0
-- CREATE SEQUENCE                          4
-- CREATE MATERIALIZED VIEW                 0
-- CREATE MATERIALIZED VIEW LOG             0
-- CREATE SYNONYM                           0
-- CREATE TABLESPACE                        0
-- CREATE USER                              0
-- 
-- DROP TABLESPACE                          0
-- DROP DATABASE                            0
-- 
-- REDACTION POLICY                         0
-- 
-- ORDS DROP SCHEMA                         0
-- ORDS ENABLE SCHEMA                       0
-- ORDS ENABLE OBJECT                       0
-- 
-- ERRORS                                   0
-- WARNINGS                                 0
