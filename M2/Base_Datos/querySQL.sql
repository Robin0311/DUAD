-- SQLite
-- SQLite

-- TABLA DE producto y Datos de ejemplo

-- CREATE TABLE producto (
--     id INTEGER PRIMARY KEY AUTOINCREMENT,
--     nombre VARCHAR(25) NOT NULL,
--     precio REAL NOT NULL,
--     fecha_ingreso DATE NOT NULL,
--     marca VARCHAR(25) NOT NULL
--     );

-- INSERT INTO producto (nombre, precio, fecha_ingreso, marca) VALUES
-- ('Laptop', 1200.00, '2024-01-15', 'Dell'),
-- ('Smartphone', 800.00, '2024-02-20', 'Samsung'),
-- ('Headphones', 150.00, '2024-03-10', 'Sony'),
-- ('Smartwatch', 250.00, '2024-04-05', 'Apple'),
-- ('Smartwatch', 300.00, '2024-04-07', 'Apple'),
-- ('Tablet', 500.00, '2024-05-12', 'Microsoft');


-- TABLA DE facturas y Datos de ejemplo

-- CREATE TABLE facturas (
--     id INTEGER PRIMARY KEY AUTOINCREMENT,
--     codigo_vendedor INTEGER NOT NULL,
--     correo_comprador VARCHAR(35) NOT NULL,
--     fecha_compra DATE NOT NULL,
--     monto_total REAL NOT NULL,
--     telefono_comprador BIGINT NOT NULL
--     );

-- INSERT INTO facturas (codigo_vendedor, correo_comprador, fecha_compra, monto_total, telefono_comprador) VALUES
-- ('1', 'john.doe@example.com', '2024-06-01', 1200.00, 1234567890),
-- ('2', 'robinson@gmail.com', '2024-06-02', 800.00, 9876543210),
-- ('3', 'maria.gonzalez@ehotmail.com', '2024-06-03', 500.00, 5555555555),
-- ('4', 'bryan@gmail.com', '2024-06-04', 250.00, 1111111111),
-- ('5', 'tabata@gmail.com', '2024-06-05', 300.00, 2222222222);


-- TABLA DE factura producto y Datos de ejemplo

-- CREATE TABLE factura_producto(
--     id INTEGER PRIMARY KEY AUTOINCREMENT,
--     id_factura INTEGER NOT NULL REFERENCES facturas(id),
--     id_producto INTEGER NOT NULL REFERENCES producto(id),
--     cantidad_comprada INTEGER NOT NULL,
--     monto_total REAL NOT NULL
--     );

-- INSERT INTO factura_producto (id_factura, id_producto, cantidad_comprada, monto_total) VALUES
-- (1, 1, 2, 2400.00),
-- (2, 2, 1, 800.00),
-- (3, 6, 1, 500.00),
-- (4, 4, 4, 1000.00),
-- (5, 5, 3, 900.00),
-- (1, 3, 2, 300.00),
-- (2, 4, 3, 750.00),
-- (3, 5, 1, 300.00),
-- (4, 6, 4, 2000.00),
-- (5, 1, 6, 7200.00);


-- TABLA DE CARRITO DE COMPRAS y Datos de ejemplo

-- CREATE TABLE carrito_compras (
--     id INTEGER PRIMARY KEY AUTOINCREMENT,
--     email_usuario VARCHAR(35) UNIQUE NOT NULL
--     );

-- INSERT INTO carrito_compras(email_usuario) VALUES
-- ('john.doe@example.com'),
-- ('robinson@gmail.com'),
-- ('maria.gonzalez@ehotmail.com'),
-- ('bryan@gmail.com'),
-- ('tabata@gmail.com');


-- TABLA DE CARRITO DE COMPRAS y Datos de ejemplo

-- CREATE TABLE carrito_producto (
--     id INTEGER PRIMARY KEY AUTOINCREMENT,
--     id_carrito INTEGER NOT NULL REFERENCES carrito_compras(id),
--     id_producto INTEGER NOT NULL REFERENCES producto(id)
--     );

-- INSERT INTO carrito_producto (id_carrito, id_producto) VALUES
-- (1, 1),
-- (1, 3),
-- (2, 2),
-- (2, 4),
-- (3, 6),
-- (4, 4),
-- (5, 5),
-- (5, 1),
-- (5, 3);

--- 4- Realice los siguientes SELECT:

---Obtenga todos los productos almacenados
-- SELECT * FROM producto;

--Obtenga todos los productos que tengan un precio mayor a 50000 (modifico a 500 porque no coloque nada mayor a 5000)
-- SELECT * FROM producto WHERE precio > 500.00;

-- Obtenga todas las compras de un mismo producto por id.
-- SELECT id_producto, SUM(cantidad_comprada) AS total_comprado
-- FROM factura_producto
-- GROUP BY id_producto;

--Obtenga todas las compras agrupadas por producto, donde se muestre el total comprado entre todas las compras.
-- SELECT nombre, SUM(cantidad_comprada) AS total_comprado  FROM factura_producto
-- JOIN producto ON factura_producto.id_producto = producto.id
-- GROUP BY producto.nombre;

--Obtenga todas las facturas realizadas por el mismo comprador
-- SELECT correo_comprador, SUM(cantidad_comprada) AS cantidad_comprada FROM factura_producto
-- JOIN facturas ON factura_producto.id_factura = facturas.id
-- GROUP BY facturas.correo_comprador;

-- Obtenga todas las facturas ordenadas por monto total de forma descendente
-- SELECT correo_comprador, SUM(cantidad_comprada) AS cantidad_comprada  FROM factura_producto
-- JOIN facturas ON factura_producto.id_factura = facturas.id
-- GROUP BY  facturas.correo_comprador
-- ORDER BY cantidad_comprada DESC;

--Obtenga una sola factura por número de factura.
-- SELECT *
-- FROM facturas
-- WHERE id = 3;