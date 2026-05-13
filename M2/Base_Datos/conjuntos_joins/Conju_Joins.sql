-- SQLite

-- CREATE TABLE books (
--     id INTEGER PRIMARY KEY AUTOINCREMENT,
--     Name TEXT NOT NULL,
--     Author TEXT 
-- );

-- INSERT INTO books (id, name, author) VALUES
-- (1, 'Don Quijote', 1),
-- (2, 'La Divina Comedia', 2),
-- (3, 'Vagabond 1-3', 3),
-- (4, 'Dragon Ball 1', 4),
-- (5, 'The Book of the 5 Rings', NULL);

-- CREATE TABLE Authors (
--     id INTEGER PRIMARY KEY AUTOINCREMENT,
--     Name TEXT NOT NULL
-- );

-- INSERT INTO Authors (id, name) VALUES
-- (1, 'Miguel de Cervantes'),
-- (2, 'Dante Alighieri'),
-- (3, 'Takehiko Inoue'),
-- (4, 'Akira Toriyama'),
-- (5, 'Walt Disney');

-- CREATE TABLE Customers (
--     id INTEGER PRIMARY KEY AUTOINCREMENT,
--     Name TEXT NOT NULL,
--     Email TEXT NOT NULL
-- );

-- INSERT INTO Customers (id, name, email) VALUES
-- (1, 'John Doe', 'j.doe@email.com'),
-- (2, 'Jane Doe', 'jane@doe.com'),
-- (3, 'Luke Skywalker', 'darth.son@email.com');


-- CREATE TABLE Rents (
--     id INTEGER PRIMARY KEY AUTOINCREMENT,
--     BookId INTEGER NOT NULL,
--     CustomerId INTEGER NOT NULL,
--     State TEXT NOT NULL
-- );


-- INSERT INTO Rents (id, BookID, CustomerId, State) VALUES
-- (1, 1, 2, 'Returned'),
-- (2, 2, 2, 'Returned'),
-- (3, 1, 1, 'On time'),
-- (4, 3, 1, 'On time'),
-- (5, 2, 2, 'Overdue');

-- -- 1- Obtenga todos los libros y sus autores
SELECT books.Name AS book, authors.Name AS author
FROM Books AS books
LEFT JOIN Authors AS authors
ON books.Author = authors.ID;

-- -- 2- Obtenga todos los libros que no tienen autor
SELECT   books.Name AS book, books.Author FROM     Books AS books
LEFT JOIN Authors AS authors
ON books.Author = authors.ID
WHERE    authors.ID IS NULL;

-- -- 3- Obtenga todos los autores que no tienen libros
SELECT authors.Name AS author FROM Authors AS authors
LEFT JOIN Books AS books
ON books.Author = authors.ID
WHERE books.ID IS NULL;

-- -- 4- Obtenga todos los libros que han sido rentados en algún momento
SELECT   DISTINCT books.Name AS book FROM     Books AS books
INNER JOIN Rents AS rents
ON books.ID = rents.BookID;

-- -- 5- Obtenga todos los libros que nunca han sido rentados
SELECT   books.Name AS book FROM     Books AS books
LEFT JOIN Rents AS rents
ON books.ID = rents.BookID
WHERE    rents.ID IS NULL;

-- -- 6- Obtenga todos los clientes que nunca han rentado un libro
SELECT   customers.Name AS customer FROM     Customers AS customers
LEFT JOIN Rents AS rents
ON customers.ID = rents.CustomerID
WHERE    rents.ID IS NULL;

-- -- 7- Obtenga todos los libros que han sido rentados y están en estado “Overdue”
SELECT   DISTINCT books.Name AS book, rents.State FROM     Books AS books
INNER JOIN Rents AS rents
ON books.ID = rents.BookID
WHERE    rents.State = 'Overdue';