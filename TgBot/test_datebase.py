from flask import Flask, render_template, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost/db_name'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    second_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)



@app.route('/')
def index():
    users = User.query.all()
    return render_template('index.html', users=users)

@app.route('/api/users', methods=['GET'])
def get_users():
    users = [{'id': 1, 'first_name': 'John', 'second_name' : 'Smith', 'last_name':'smmm','email':'dsfadfa@mail.ru' }]
    return jsonify(users)

@app.route('/api/users', methods=['POST'])
def add_user():
    user = request.get_json()
    # Save user to database
    return jsonify(user)

