from django.test import TestCase
from .models import ToDo


class ToDoModelTest(TestCase):
    def setUp(self):
        self.todo = ToDo.objects.create(
            title="Sample Task",
            description="This is a sample task.",
        )

    def test_todo_creation(self):
        self.assertEqual(self.todo.title, "Sample Task")
