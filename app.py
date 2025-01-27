from flask import Flask, request, jsonify
import pyodbc
import datetime

app = Flask(__name__)

def db_connection():
    conn = None
    try:
        conn = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};'
            'SERVER=localhost,1433;'
            'DATABASE=processoSeletivo;'
            'UID=logonProcesso;'
            'PWD=12345678;'
        )
    except pyodbc.Error as e:
        print(e)
    return conn

@app.route('/users', methods=['GET', 'POST'])
def all_users():
    current_time = datetime.datetime.now()
    conn = db_connection()
    cursor = conn.cursor()

    if request.method == 'GET':
        cursor.execute("SELECT * FROM users")
        columns = [column[0] for column in cursor.description]
        all_users = [dict(zip(columns, row)) for row in cursor.fetchall()]
        return jsonify(all_users), 200

    if request.method == 'POST':
        new_nome = request.json["nome"]
        new_email = request.json["email"]
        new_age = int(request.json["age"])
        new_created_at = current_time

        sql = """INSERT INTO users (nome, email, age, created_at) VALUES (?, ?, ?, ?)"""
        cursor.execute(sql, (new_nome, new_email, new_age, new_created_at))
        conn.commit()
        return "User created successfully", 201

@app.route('/users/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def single_user(id):
    conn = db_connection()
    cursor = conn.cursor()

    if request.method == 'GET':
        cursor.execute("SELECT * FROM users WHERE usuario_id = ?", (id,))
        user = cursor.fetchone()
        if user:
            columns = [column[0] for column in cursor.description]
            user = dict(zip(columns, user))

            cursor.execute("SELECT * FROM addresses WHERE usuario_id = ?", (id,))
            columns = [column[0] for column in cursor.description]
            addresses = [dict(zip(columns, row)) for row in cursor.fetchall()]
            user["addresses"] = addresses

            return jsonify(user), 200
        return "User not found", 404

    if request.method == 'PUT':
        nome = request.json['nome']
        email = request.json['email']
        age = request.json['age']

        sql = """UPDATE users SET nome = ?, email = ?, age = ? WHERE usuario_id = ?"""
        cursor.execute(sql, (nome, email, age, id))
        conn.commit()
        return jsonify({"usuario_id": id, "nome": nome, "email": email, "age": age}), 200

    if request.method == 'DELETE':
        sql = "DELETE FROM users WHERE usuario_id = ?"
        cursor.execute(sql, (id,))
        conn.commit()
        return f"User with id {id} has been deleted.", 200

@app.route('/users/<int:id>/addresses', methods=['POST', 'GET'])
def user_addresses(id):
    conn = db_connection()
    cursor = conn.cursor()

    if request.method == 'POST':
        street = request.json['street']
        city = request.json['city']
        state = request.json['state']
        zipcode = request.json['zipcode']

        sql = """INSERT INTO addresses (usuario_id, street, city, estado, zipcode) VALUES (?, ?, ?, ?, ?)"""
        cursor.execute(sql, (id, street, city, state, zipcode))
        conn.commit()
        return "Address created successfully", 201

    if request.method == 'GET':
        cursor.execute("SELECT * FROM addresses WHERE usuario_id = ?", (id,))
        columns = [column[0] for column in cursor.description]
        addresses = [dict(zip(columns, row)) for row in cursor.fetchall()]
        return jsonify(addresses), 200

@app.route('/addresses/<int:id>', methods=['PUT', 'DELETE'])
def single_address(id):
    conn = db_connection()
    cursor = conn.cursor()

    if request.method == 'PUT':
        street = request.json['street']
        city = request.json['city']
        state = request.json['state']
        zipcode = request.json['zipcode']

        sql = """UPDATE addresses SET street = ?, city = ?, estado = ?, zipcode = ? WHERE endereco_id = ?"""
        cursor.execute(sql, (street, city, state, zipcode, id))
        conn.commit()
        return "Address updated successfully", 200

    if request.method == 'DELETE':
        sql = "DELETE FROM addresses WHERE endereco_id = ?"
        cursor.execute(sql, (id,))
        conn.commit()
        return f"Address with id {id} has been deleted.", 200

if __name__ == '__main__':
    app.run(debug=True)

