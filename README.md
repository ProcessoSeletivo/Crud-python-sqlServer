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




Exemplos de requisição:
{
	"info": {
		"_postman_id": "2ce33591-18f7-4426-af0f-85537597d507",
		"name": "processoSeletivo",
		"schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json",
		"_exporter_id": "28684754"
	},
	"item": [
		{
			"name": "usuario",
			"item": [
				{
					"name": "Criar usuario",
					"request": {
						"method": "POST",
						"header": [],
						"body": {
							"mode": "raw",
							"raw": "{\r\n    \"age\": 40,\r\n    \"nome\": \"Leonardp Ip algumacoisa\",\r\n    \"email\": \"leonardo@gmail.com\"\r\n}",
							"options": {
								"raw": {
									"language": "json"
								}
							}
						},
						"url": {
							"raw": "http://127.0.0.1:5000/users",
							"protocol": "http",
							"host": [
								"127",
								"0",
								"0",
								"1"
							],
							"port": "5000",
							"path": [
								"users"
							]
						}
					},
					"response": []
				},
				{
					"name": "Listar usuarios",
					"request": {
						"method": "GET",
						"header": [],
						"url": {
							"raw": "http://127.0.0.1:5000/users",
							"protocol": "http",
							"host": [
								"127",
								"0",
								"0",
								"1"
							],
							"port": "5000",
							"path": [
								"users"
							]
						}
					},
					"response": []
				},
				{
					"name": "Listar Usuario especifico",
					"request": {
						"method": "GET",
						"header": [],
						"url": {
							"raw": "http://127.0.0.1:5000/users/2",
							"protocol": "http",
							"host": [
								"127",
								"0",
								"0",
								"1"
							],
							"port": "5000",
							"path": [
								"users",
								"2"
							]
						}
					},
					"response": []
				},
				{
					"name": "Atualizar Usuario",
					"request": {
						"method": "PUT",
						"header": [],
						"body": {
							"mode": "raw",
							"raw": "{\r\n    \"age\": 40,\r\n    \"nome\": \"Leonardo Ip algumacoisa\",\r\n    \"email\": \"leonardo@gmail.com\"\r\n}",
							"options": {
								"raw": {
									"language": "json"
								}
							}
						},
						"url": {
							"raw": "http://127.0.0.1:5000/users/2",
							"protocol": "http",
							"host": [
								"127",
								"0",
								"0",
								"1"
							],
							"port": "5000",
							"path": [
								"users",
								"2"
							]
						}
					},
					"response": []
				},
				{
					"name": "excluir usuario",
					"request": {
						"method": "DELETE",
						"header": [],
						"url": {
							"raw": "http://127.0.0.1:5000/users/2",
							"protocol": "http",
							"host": [
								"127",
								"0",
								"0",
								"1"
							],
							"port": "5000",
							"path": [
								"users",
								"2"
							]
						}
					},
					"response": []
				}
			]
		},
		{
			"name": "endereço",
			"item": [
				{
					"name": "Consultar endereco",
					"request": {
						"method": "GET",
						"header": [],
						"url": {
							"raw": "http://127.0.0.1:5000/users/2/addresses",
							"protocol": "http",
							"host": [
								"127",
								"0",
								"0",
								"1"
							],
							"port": "5000",
							"path": [
								"users",
								"2",
								"addresses"
							]
						}
					},
					"response": []
				},
				{
					"name": "Inserir Endereco",
					"request": {
						"method": "POST",
						"header": [],
						"body": {
							"mode": "raw",
							"raw": "{\r\n\"street\": \"CLN 212\",\r\n\"city\": \"Asa norte\",\r\n\"state\": \"Brasilia\",\r\n\"zipcode\": 204563 \r\n}",
							"options": {
								"raw": {
									"language": "json"
								}
							}
						},
						"url": {
							"raw": "http://127.0.0.1:5000/users/2/addresses",
							"protocol": "http",
							"host": [
								"127",
								"0",
								"0",
								"1"
							],
							"port": "5000",
							"path": [
								"users",
								"2",
								"addresses"
							]
						}
					},
					"response": []
				},
				{
					"name": "Excluir Endereco",
					"request": {
						"method": "DELETE",
						"header": [],
						"url": {
							"raw": "http://127.0.0.1:5000/addresses/1",
							"protocol": "http",
							"host": [
								"127",
								"0",
								"0",
								"1"
							],
							"port": "5000",
							"path": [
								"addresses",
								"1"
							]
						}
					},
					"response": []
				},
				{
					"name": "Alterar Endereco",
					"request": {
						"method": "PUT",
						"header": [],
						"body": {
							"mode": "raw",
							"raw": "{\r\n\"street\": \"CLN 212\",\r\n\"city\": \"Asa norte\",\r\n\"state\": \"Brasilandia\",\r\n\"zipcode\": 204563 \r\n}",
							"options": {
								"raw": {
									"language": "json"
								}
							}
						},
						"url": {
							"raw": "http://127.0.0.1:5000/addresses/1",
							"protocol": "http",
							"host": [
								"127",
								"0",
								"0",
								"1"
							],
							"port": "5000",
							"path": [
								"addresses",
								"1"
							]
						}
					},
					"response": []
				}
			]
		}
	]
}
