# Crud-python-sqlServer
Criação do banco:

CREATE TABLE dbo.users
(
    usuario_id int PRIMARY KEY IDENTITY(1,1) NOT NULL,
    nome varchar(255) NOT NULL,
    email varchar(255) UNIQUE NOT NULL,
    age int NOT NULL,
    created_at datetime NOT NULL
);

CREATE TABLE dbo.addresses
(
    endereco_id int PRIMARY KEY IDENTITY(1,1) NOT NULL,
    street varchar(255) NOT NULL,
    city varchar(255) NOT NULL,
    estado varchar(255) NOT NULL,
    zipcode varchar(255) NOT NULL,
	usuario_id int NULL,
	FOREIGN KEY (usuario_id) REFERENCES users(usuario_id)
);
