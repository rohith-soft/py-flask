from flask import request
from flask_classy import FlaskView, route

from models.TodoModel import TodoModel, TodoSchema

error_message = 'Error occurred while {} todo with id {}, {}'

todo_schema = TodoSchema()


class TodoView(FlaskView):
    route_base = '/todos'

    @route('/', methods=['GET'])
    def get_all_todos(self):
        todos = TodoModel.get_all_todos()
        result = todo_schema.dump(todos, many=True)
        return {"todos": result}

    @route('/<int:todo_id>', methods=['GET'])
    def get_todo_by_id(self, todo_id):
        return todo_schema.dump(TodoModel.get_todo_by_id(todo_id))

    @route('/<int:todo_id>', methods=['DELETE'])
    def delete_todo_by_id(self, todo_id):
        try:
            todo = TodoModel.get_todo_by_id(todo_id)
            TodoModel.delete(todo)
            return "Deleted TODO"
        except Exception as e:
            print(error_message.format('deleting', todo_id, e))
            return error_message.format('deleting', todo_id, e)

    @route('/<int:todo_id>', methods=['PUT'])
    def update_todo_by_id(self, todo_id):
        try:
            request_data = request.get_json()
            todo = TodoModel.get_todo_by_id(todo_id)
            TodoModel.update(todo, request_data)
            return todo_schema.dump(todo)

        except Exception as e:
            print(error_message.format('updating', todo_id, e))
            return error_message.format('updating', todo_id, e)

    @route('/', methods=['POST'])
    def add_todo(self):
        try:
            request_data = request.get_json()
            todo = TodoModel(request_data['content'], request_data['completed'])
            TodoModel.create(todo)
            return 'created successfully', 201

        except Exception as e:
            print(error_message.format('creating', '', e))
            return error_message.format('creating', '', e)
