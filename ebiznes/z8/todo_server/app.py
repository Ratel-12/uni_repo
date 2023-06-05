from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.config['SECRET_KEY'] = 'this_is_a_demo_app_and_as_such_only_gets_a_placeholder_here'
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    todos = db.relationship('Todo', backref='user', lazy=True)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(120), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    existing_user = User.query.filter_by(username=data['username']).first()
    if existing_user is not None:
        return {'message': 'Username already exists'}, 400
    new_user = User(username=data['username'], password=generate_password_hash(data['password']))
    db.session.add(new_user)
    db.session.commit()

    login_user(new_user)

    return {'message': 'Registered successfully'}

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(username=data['username']).first()
    if user and check_password_hash(user.password, data['password']):
        login_user(user)
        return {'message': 'Login successful'}
    else:
        return {'message': 'Incorrect username or password'}

@app.route('/<username>/todos', methods=['POST'])
@login_required
def add_todo(username):
    data = request.get_json()
    user = User.query.filter_by(username=username).first()
    if user:
        new_todo = Todo(task=data['task'], user=user)
        db.session.add(new_todo)
        db.session.commit()
        return {'message': 'Todo added'}
    else:
        return {'message': 'User not found'}
    
@app.route('/<username>/todos', methods=['GET'])
@login_required
def get_todos(username):
    user = User.query.filter_by(username=username).first()
    if user:
        todos = [{'id': todo.id, 'task': todo.task} for todo in user.todos]
        return {'todos': todos}
    else:
        return {'message': 'User not found'}
 
@app.route('/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    return {'message': 'Logged out'}

@app.route('/todos/<int:todo_id>', methods=['DELETE'])
@login_required
def delete_todo(todo_id):
    todo = Todo.query.get(todo_id)
    if todo and todo.user == current_user:
        db.session.delete(todo)
        db.session.commit()
        return {'message': 'Todo deleted'}
    else:
        return {'message': 'Todo not found'}

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)

