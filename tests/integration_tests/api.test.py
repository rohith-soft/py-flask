import json
import unittest

from app import app


class APIIntegrationTests(unittest.TestCase):

    def test_get_all_todos(self):
        tester = app.test_client(self)
        response = tester.get('todo-app/todos/')
        self.assertEqual(response.status_code, 200)
        # converting bytes to dictionary
        response_dict = json.loads(response.data.decode('utf-8'))
        self.assertEqual('Finished the app', response_dict['todos'][0]['content'])
        self.assertGreater(len(response_dict['todos']), 2)

    def test_get_todo_by_id(self):
        tester = app.test_client(self)
        response = tester.get('todo-app/todos/1')
        self.assertEqual(response.status_code, 200)
        # converting bytes to dictionary
        response_dict = json.loads(response.data.decode('utf-8'))
        self.assertEqual('Finished the app', response_dict['content'])

    def test_update_todo(self):
        content = "Get few more groceries"

        tester = app.test_client(self)
        response = tester.put('todo-app/todos/6', json={"content": content, "completed": True})
        self.assertEqual(response.status_code, 200)

        response = tester.get('todo-app/todos/6')
        self.assertEqual(response.status_code, 200)
        # converting bytes to dictionary
        response_dict = json.loads(response.data.decode('utf-8'))
        self.assertEqual(content, response_dict['content'])

    def test_create_todo(self):
        tester = app.test_client(self)
        get_response = tester.get('todo-app/todos/')
        response_dict = json.loads(get_response.data.decode('utf-8'))
        initial_todo_len = len(response_dict['todos'])

        response = tester.post('todo-app/todos/', json={"content": "Get more groceries", "completed": True})
        self.assertEqual(response.status_code, 201)

        get_response = tester.get('todo-app/todos/')
        response_dict = json.loads(get_response.data.decode('utf-8'))
        final_todo_len = len(response_dict['todos'])
        self.assertGreater(final_todo_len, initial_todo_len)


if __name__ == '__main__':
    unittest.main()
