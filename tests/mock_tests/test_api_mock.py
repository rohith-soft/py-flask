# This mock test is not working at the moment
import pytest

import app


@pytest.fixture
def app(mocker):
    mocker.patch("flask_sqlalchemy.SQLAlchemy.init_app", return_value=True)
    mocker.patch("flask_sqlalchemy.SQLAlchemy.create_all", return_value=True)
    mocker.patch("models.TodoModel.TodoModel.get_all_todos", return_value={})
    return app.app


def test_api_mock(client):
    response = client.get('todo-app/todos/')
    print(response.data)
    assert response.status_code == 200
