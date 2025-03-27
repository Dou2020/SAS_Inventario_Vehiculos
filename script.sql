CREATE DATABASE Practica1;
USE Practica1;

-- Crear tabla
CREATE TABLE vehiculo (
    id INT IDENTITY(1,1) PRIMARY KEY,
    marca VARCHAR(50) NOT NULL,
    modelo VARCHAR(50) NOT NULL,
    anio INT NOT NULL,
    precio DECIMAL(10, 2) NOT NULL,
    disponibilidad BIT NOT NULL
);

INSERT INTO vehiculo (marca, modelo, anio, precio, disponibilidad) VALUES 
('Toyota', 'Corolla', 2019, 25000.00, 1), 
('Honda', 'Civic', 2018, 20000.00, 1), 
('Nissan', 'Sentra', 2017, 15000.00, 1), 
('Mazda', '3', 2016, 18000.00, 1), 
('Hyundai', 'Elantra', 2015, 17000.00, 1);

CREATE TABLE clientes (
    id INT IDENTITY(1,1) PRIMARY KEY,
    DPI VARCHAR(13) NOT NULL UNIQUE,
    nombre VARCHAR(50) NOT NULL,
    email VARCHAR(50) NOT NULL UNIQUE,
    telefono VARCHAR(50) NOT NULL
);

INSERT INTO clientes (DPI, nombre, email, telefono) VALUES 
('1234567890101', 'Juan Perez', 'd@gmail', '12345678'), 
('1234567890102', 'Maria Lopez', 'm@gmail', '12345679'), 
('1234567890103', 'Pedro Ramirez', 'p@gmail', '12345680'), 
('1234567890104', 'Josefina Garcia', 'j@gmail', '12345681'), 
('1234567890105', 'Carlos Soto', 'c@gmail', '12345682');

CREATE TABLE ventas (
    id INT IDENTITY(1,1) PRIMARY KEY,
    id_vehiculo INT NOT NULL,
    id_cliente INT NOT NULL,
    fecha DATE NOT NULL,
    FOREIGN KEY (id_vehiculo) REFERENCES vehiculo(id),
    FOREIGN KEY (id_cliente) REFERENCES clientes(id)
);

INSERT INTO ventas (id_vehiculo, id_cliente, fecha) VALUES 
(1, 1, '2020-01-01'), 
(2, 2, '2020-01-02'), 
(3, 3, '2020-01-03'), 
(4, 4, '2020-01-04'), 
(5, 5, '2020-01-05');