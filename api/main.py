from flask import Flask, request, jsonify
from flask_cors import CORS
import libsql_client
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
CORS(app)

TURSO_DATABASE_URL = "libsql://audio-text-leonchi.aws-eu-west-1.turso.io"
TURSO_AUTH_TOKEN = "eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJhIjoicnciLCJpYXQiOjE3NzQwNDE3MjYsImlkIjoiMDE5ZDBkMWItYzgwMS03YTk4LWFlZjYtZmZhOWRlNmY3YThmIiwicmlkIjoiNzIwZDlmODAtMzEzZS00MDkwLTgxMzUtYzM2MDI0NTE4MjRmIn0.2JXg7v8AcEiGtiykPh4w6XrUOKjrioqZBTsyWUY70jmxyqEiR__O2J40yAEZH_6JSGlIwooPn4Dy4x1F8Z5TDw"

client = libsql_client.create_client_sync(TURSO_DATABASE_URL, auth_token=TURSO_AUTH_TOKEN)

# Модель пользователя


@app.route('/register', methods=['POST'])
def register():
    data = request.json
    email=data.get('email')
    password=data.get('password')
    hashed_password = generate_password_hash(password,method='sha256')
    try:
        client.execute("INSERT INTO users (email, password) VALUES (?, ?)", (email, hashed_password))
        return jsonify({"status": "success", "message": "Пользователь успешно зарегистрирован!"}), 201
    except Exception as e:
        return jsonify({"status": "error", "message": "Такой пользователь уже существует!"}), 400

@app.route ('/login', methods=['POST'])
def login():
    data=request.json
    email=data.get('email')
    password=data.get('password')
    user = client.execute("SELECT * FROM users WHERE email = ?", (email,)).fetchone()
    if user and check_password_hash(user[2], password):
        return jsonify({"status": "success", "message": "Успешный вход!"}), 200
    else:
        return jsonify({"status": "error", "message": "Неверный email или пароль!"}), 401    

if __name__=='__main__':
    app.run(debug=True)