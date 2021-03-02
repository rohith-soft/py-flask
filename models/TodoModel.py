from datetime import datetime

from flask_sqlalchemy import SQLAlchemy
from marshmallow import fields, Schema

db = SQLAlchemy()


class TodoModel(db.Model):
    __tablename__ = 'todo'

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Boolean, default=0)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, content, completed):
        self.content = content
        self.completed = completed

    def __repr__(self):
        return '<Task %r>' % self.id

    @staticmethod
    def get_all_todos():
        return TodoModel.query.all()

    @staticmethod
    def get_todo_by_id(todo_id):
        return TodoModel.query.get_or_404(todo_id)

    def create(self):
        db.session.add(self)
        db.session.commit()

    def update(self, data):
        for key, item in data.items():
            setattr(self, key, item)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


class TodoSchema(Schema):
    id = fields.Integer(dump_only=True)
    content = fields.Str(required=True)
    completed = fields.Boolean(required=True)
    date_created = fields.DateTime(required=False)
