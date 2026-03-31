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
--     correo_comprador VARCHAR(35) NOT NULL,
--     fecha_compra DATE NOT NULL,
--     monto_total REAL NOT NULL
--     );

-- INSERT INTO facturas (codigo_vendedor, correo_comprador, fecha_compra, monto_total, telefono_comprador) VALUES
-- (101, 'john.doe@example.com', '2024-06-01', 1200.00, '+34 657655231'),
-- (102, 'robinson@gmail.com', '2024-06-02', 800.00, '+506 987654321'),
-- (103, 'tabata@gmail.com', '2024-06-01', 1200.00, '+360 1234567'),
-- (104, 'bryan@gmail.com', '2024-06-02', 800.00, '+516 9876543'),
-- (105, 'alex@gmail.com', '2024-06-01', 1200.00, '+43 12345678'),
-- (106, 'Isabel@gmail.com', '2024-06-02', 800.00, '+88 9876543210');



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

--3-Utilizando el comando ALTER, modifique la tabla de Facturas y agregue una columna para almacenar también el número de teléfono del comprador, y otra para el código de empleado del cajero que realizó la venta.

-- ALTER TABLE facturas
-- ADD COLUMN codigo_vendedor INTEGER NOT NULL DEFAULT '0';

-- ALTER TABLE facturas
-- ADD COLUMN telefono_comprador TEXT NOT NULL DEFAULT 'NO REGISTRADO';


--- 4- Realice los siguientes SELECT:

---1- Obtenga todos los productos almacenados
-- SELECT * FROM producto;

--2- Obtenga todos los productos que tengan un precio mayor a 50000 (modifico a 500 porque no coloque nada mayor a 5000)
-- SELECT * FROM producto WHERE precio > 500.00;

--3- Obtenga todas las compras de un mismo producto por id.
-- SELECT id_producto, SUM(cantidad_comprada) AS total_comprado
-- FROM factura_producto
-- WHERE id_producto = 4
-- GROUP BY id_producto;

--4- Obtenga todas las compras agrupadas por producto, donde se muestre el total comprado entre todas las compras.
-- SELECT nombre, SUM(cantidad_comprada) AS total_comprado  FROM factura_producto
-- JOIN producto ON factura_producto.id_producto = producto.id
-- GROUP BY producto.nombre;

--5- Obtenga todas las facturas realizadas por el mismo comprador
-- SELECT facturas.id, facturas.correo_comprador, SUM(factura_producto.cantidad_comprada) AS total_cantidad_comprada
-- FROM facturas
-- INNER JOIN factura_producto
-- ON facturas.id = factura_producto.id_factura
-- WHERE facturas.id = 4
-- GROUP BY facturas.id, facturas.correo_comprador;

--6- Obtenga todas las facturas ordenadas por monto total de forma descendente
-- SELECT correo_comprador, SUM(cantidad_comprada) AS cantidad_comprada  FROM factura_producto
-- JOIN facturas ON factura_producto.id_factura = facturas.id
-- GROUP BY  facturas.correo_comprador
-- ORDER BY cantidad_comprada DESC;

--7- Obtenga una sola factura por número de factura.
-- SELECT *
-- FROM facturas
-- WHERE id = 3; 



