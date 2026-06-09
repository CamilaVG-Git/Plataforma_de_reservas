
-- BASE DE DATOS: TureservaBD_db


CREATE DATABASE IF NOT EXISTS TureservaBD_db
    CHARACTER SET utf8mb4
    COLLATE utf8mb4_unicode_ci;

USE TureservaBD_db;

-- TABLA 1: tours

CREATE TABLE IF NOT EXISTS tours (
    id           INT            NOT NULL AUTO_INCREMENT,
    nombre       VARCHAR(200)   NOT NULL,
    descripcion  TEXT           DEFAULT NULL,
    precio       DECIMAL(10,2)  NOT NULL COMMENT 'Precio por persona en USD',
    activo       TINYINT(1)     NOT NULL DEFAULT 1,
    creado_en    DATETIME       DEFAULT CURRENT_TIMESTAMP,

    PRIMARY KEY (id)
);


-- TABLA 2: clientes

CREATE TABLE IF NOT EXISTS clientes (
    id               INT          NOT NULL AUTO_INCREMENT,
    nombre_completo  VARCHAR(150) NOT NULL,
    correo           VARCHAR(150) NOT NULL UNIQUE,
    telefono         VARCHAR(20)  NOT NULL,
    nacionalidad     VARCHAR(100) DEFAULT NULL,
    creado_en        DATETIME     DEFAULT CURRENT_TIMESTAMP,

    PRIMARY KEY (id)
);

-- TABLA 3: reservas
CREATE TABLE IF NOT EXISTS reservas (
    id                  INT           NOT NULL AUTO_INCREMENT,
    cliente_id          INT           NOT NULL,
    tour_id             INT           NOT NULL,
    fecha_tour          DATE          NOT NULL,
    num_personas        INT           NOT NULL DEFAULT 1,
    solicitud_especial  TEXT          DEFAULT NULL COMMENT 'Alergias, cumpleaños, necesidades especiales',
    metodo_pago         ENUM(
                            'tarjeta',
                            'transferencia',
                            'efectivo'
                        ) NOT NULL,
    total               DECIMAL(10,2) DEFAULT NULL COMMENT 'precio_tour x num_personas',
    estado              ENUM('pendiente', 'confirmada', 'cancelada') NOT NULL DEFAULT 'pendiente',
    creado_en           DATETIME      DEFAULT CURRENT_TIMESTAMP,

    PRIMARY KEY (id),
    CONSTRAINT fk_reserva_cliente
        FOREIGN KEY (cliente_id) REFERENCES clientes(id) ON DELETE CASCADE,
    CONSTRAINT fk_reserva_tour
        FOREIGN KEY (tour_id)    REFERENCES tours(id)    ON DELETE CASCADE
);

-- DATOS 


INSERT INTO tours (nombre, descripcion, precio) VALUES
('Ciudad Colonial',         'Recorrido por la Zona Colonial de Santo Domingo, Patrimonio de la Humanidad.', 30.00),
('Isla Saona',              'Excursión en catamarán a la paradisíaca Isla Saona con almuerzo incluido.',    85.00),
('Cuevas de las Maravillas','Tour a las cuevas con pinturas rupinas taínas en La Romana.',                  45.00);

INSERT INTO clientes (nombre_completo, correo, telefono, nacionalidad) VALUES
('Pedro Perez',  'pedroperez@gmail.com',  '8096677777', 'Dominicano'),
('Maria García', 'maria.garcia@gmail.com', '8291234567', 'Colombiana');

INSERT INTO reservas (cliente_id, tour_id, fecha_tour, num_personas, metodo_pago, total, estado) VALUES
(1, 1, '2026-06-09', 1, 'efectivo',  30.00, 'confirmada'),
(2, 2, '2026-06-15', 3, 'tarjeta',  255.00, 'pendiente');