CREATE TABLE Pedidos (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    usermail VARCHAR(50) NOT NULL,
    request_pedido VARCHAR(300) NOT NULL
);
