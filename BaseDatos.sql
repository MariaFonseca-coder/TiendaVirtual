-- QUITAR COMENTARIO EN CASO DE NO TENER CREADA LA BASE DE DATOS
-- CREATE DATABASE IF NOT EXISTS proyectoFinal;


--cambiar nombre si quiere usar uno distinto lo puse por poner
USE proyectoFinal;


-- Drop tables en caso de ser necesario

/*
DROP TABLE cliente;
DROP TABLE direccion;
DROP TABLE usuario;
DROP TABLE pedido;
DROP TABLE pago;
DROP TABLE proveedor;
DROP TABLE categoria;
DROP TABLE producto;
DROP TABLE inventario;
DROP TABLE detallepedido;
*/


CREATE TABLE cliente (
  ID_cliente INT PRIMARY KEY,
  Nombre VARCHAR(25),
  Apellido VARCHAR(50),
  Correo VARCHAR(100),
  contrasena VARCHAR(50),
  Telefono VARCHAR(15),
  Fecha_Registro  TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE direccion (
  ID_direccion INT PRIMARY KEY,
  ID_cliente INT,
  direccion_Linea1 VARCHAR(200),
  Ciudad VARCHAR(60),
  Pais VARCHAR(60),
  FOREIGN KEY (ID_cliente) REFERENCES cliente(ID_cliente)
);

CREATE TABLE usuario (
  ID_Usuario INT PRIMARY KEY,
  Nombre_Usuario VARCHAR(30),
  contrasena VARCHAR(50),
  Rol VARCHAR(30),
  Fecha_Creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE pedido (
  ID_pedido INT PRIMARY KEY,
  ID_cliente INT,
  Fecha_pedido TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  Estado VARCHAR(50),
  Total DECIMAL(10,2),
  FOREIGN KEY (ID_cliente) REFERENCES cliente(ID_cliente)
);

CREATE TABLE pago (
  ID_pago INT PRIMARY KEY,
  ID_pedido INT,
  Monto DECIMAL(10,2),
  Metodo_pago VARCHAR(150),
  FOREIGN KEY (ID_pedido) REFERENCES pedido(ID_pedido)
);

CREATE TABLE proveedor (
  ID_proveedor INT PRIMARY KEY,
  Nombre VARCHAR(60),
  Contacto VARCHAR(100),
  Telefono VARCHAR(20)
);

CREATE TABLE categoria (
  ID_categoria INT PRIMARY KEY,
  Nombre VARCHAR(100),
  Descripcion TEXT
);

CREATE TABLE producto (
  ID_producto INT PRIMARY KEY,
  Nombre VARCHAR(100),
  Descripcion TEXT,
  Precio DECIMAL(10,2),
  Color VARCHAR(50),
  ID_categoria INT,
  ID_proveedor INT,
  FOREIGN KEY (ID_categoria) REFERENCES categoria(ID_categoria),
  FOREIGN KEY (ID_proveedor) REFERENCES proveedor(ID_proveedor)
);

CREATE TABLE inventario (
  ID_inventario INT PRIMARY KEY,
  ID_producto INT,
  Cantidad_Disponible INT,
  Campo VARCHAR(50),
  FOREIGN KEY (ID_producto) REFERENCES producto(ID_producto)
);

CREATE TABLE detallepedido (
  ID_detallepedido INT PRIMARY KEY,
  ID_pedido INT,
  ID_producto INT,
  Cantidad INT,
  Precio_Unitario DECIMAL(10,2),
  FOREIGN KEY (ID_pedido) REFERENCES pedido(ID_pedido),
  FOREIGN KEY (ID_producto) REFERENCES producto(ID_producto)
);



-- Inserts ----------------------------------
INSERT INTO cliente (ID_cliente, Nombre, Apellido, Correo, contrasena, Telefono) VALUES
(1, 'Kevin', 'Franco', 'kevin@mail.com', 'contrasena123', '1234567890'),
(2, 'Maria', 'Fonseca', 'maria@mail.com', 'contrasena456', '9876543210'),
(3, 'Satiago', 'Perez', 'santiago@mail.com', 'contrasena789', '3211234567');

INSERT INTO direccion (ID_direccion, ID_cliente, direccion_Linea1, Ciudad, Pais) VALUES
(1, 1, 'calle prueba', 'Ciudad de prueba', 'Costa Rica'),
(2, 2, 'Avenida prueba', 'Ciudad de prueba 2', 'Costa Rica'),
(3, 3, 'Calle prueba2', 'Ciudad de prueba 3', 'Costa Rica');

INSERT INTO Usuario (ID_Usuario, Nombre_Usuario, contrasena, Rol) VALUES
(1, 'admin', 'admin123', 'Administrador'),
(2, 'usuario1', 'user123', 'Usuario'),
(3, 'usuario2', 'user321', 'Usuario');

INSERT INTO pedido (ID_pedido, ID_cliente, Estado, Total)VALUES
(1, 1, 'Pendiente', 100.00),
(2, 2, 'Enviado', 200.00),
(3, 3, 'Entregado', 300.00);

INSERT INTO pago (ID_pago, ID_pedido, Monto, Metodo_pago)VALUES
(1, 1, 100.00, 'Tarjeta'),
(2, 2, 200.00, 'PayPal'),
(3, 3, 300.00, 'Sinpe');

INSERT INTO proveedor (ID_proveedor, Nombre, Contacto, Telefono)VALUES
(1, 'Proveedor prueba1', 'proveedor1@email.com', '1234567890'),
(2, 'Proveedor prueba2', 'proveedor2@mail.com', '9876543210'),
(3, 'proveedor prueba3', 'proveedor3@gmail.com', '5551234567');

INSERT INTO categoria (ID_categoria, Nombre, Descripcion)VALUES
(1, 'Prendas', 'Todas las prendas disponibles'),
(2, 'Accesorios', 'Sombreros, collares, etc.'),
(3, 'Calzado', 'Tenis, sandalias, botas, etc.');

INSERT INTO producto (ID_producto, Nombre, Descripcion, Precio, Color, ID_categoria, ID_proveedor)VALUES
(1, 'Camiseta', 'Camisa blanca sencilla', 15.00, 'Blanca', 1, 1),
(2, 'Bulto sencillo', 'Bulto color negro', 20.00, 'Negro', 2, 2),
(3, 'Zapatos de vestir', 'Zapatos de cuero', 70.00, 'Negro', 3, 3);

INSERT INTO inventario (ID_inventario, ID_producto, Cantidad_Disponible, Campo)VALUES
(1, 1, 10, 'Almacen 1'),
(2, 2, 20, 'Almacen 2'),
(3, 3, 30, 'Almacen 3');

INSERT INTO detallepedido (ID_detallepedido, ID_Pedido, ID_Producto, Cantidad, Precio_Unitario)VALUES
(1, 1, 1, 2, 500.00),
(2, 1, 2, 1, 20.00),
(3, 2, 3, 3, 30.00),
(4, 3, 1, 1, 500.00),
(5, 3, 2, 2, 20.00);