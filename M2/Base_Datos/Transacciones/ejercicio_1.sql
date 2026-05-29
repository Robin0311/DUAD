-- Ejercicio 1: Creación de la Base de Datos
-- Plantee una base de datos simple que incluya las siguientes entidades:
-- Products
-- Users
-- Bills

DROP TABLE IF EXISTS bill_items;
DROP TABLE IF EXISTS bills;
DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS users;

CREATE TABLE users (
    user_id   VARCHAR(50)   PRIMARY KEY,
    name      VARCHAR(100)  NOT NULL,
    email     VARCHAR(150)  NOT NULL UNIQUE,
    status    VARCHAR(20)   NOT NULL DEFAULT 'active'
);

CREATE TABLE products (
    product_id   VARCHAR(50)    PRIMARY KEY,
    product_name VARCHAR(150)   NOT NULL,
    price        DECIMAL(10,2)  NOT NULL CHECK (price >= 0),
    stock        INTEGER        NOT NULL CHECK (stock >= 0)
);

CREATE TABLE bills (
    bill_id    VARCHAR(50)    PRIMARY KEY,
    user_id    VARCHAR(50)    NOT NULL REFERENCES users(user_id),
    total      DECIMAL(10,2)  NOT NULL DEFAULT 0,
    status     VARCHAR(20)    NOT NULL DEFAULT 'active' CHECK (status IN ('active', 'returned')),
    created_at TIMESTAMP      NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE bill_items (
    item_id    SERIAL         PRIMARY KEY,
    bill_id    VARCHAR(50)    NOT NULL REFERENCES bills(bill_id),
    product_id VARCHAR(50)    NOT NULL REFERENCES products(product_id),
    quantity   INTEGER        NOT NULL CHECK (quantity > 0),
    unit_price DECIMAL(10,2)  NOT NULL CHECK (unit_price >= 0)
);

-- Datos de prueba
INSERT INTO users (user_id, name, email) VALUES
    ('U001', 'Ana Lopez',    'ana.lopez@email.com'),
    ('U002', 'Carlos Ruiz',  'carlos.ruiz@email.com'),
    ('U003', 'Maria Torres', 'maria.torres@email.com');

INSERT INTO products (product_id, product_name, price, stock) VALUES
    ('P001', 'Laptop Gamer',      1200.00, 5),
    ('P002', 'Mouse Inalambrico',   25.00, 20),
    ('P003', 'Teclado Mecanico',    80.00, 10),
    ('P004', 'Monitor 27"',        350.00,  3);