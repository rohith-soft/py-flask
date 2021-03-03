from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from configs import DbConfig
from views.TodoView import TodoView

app = Flask(__name__)

app.config.from_object(DbConfig.DbConfig)
db = SQLAlchemy(app)

TodoView.register(app, route_prefix='/todo-app/')

if __name__ == '__main__':
    with app.app_context():
        app.run(debug=True)
