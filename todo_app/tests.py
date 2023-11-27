from django.test import TestCase
from django.urls import reverse
from django.utils import timezone  # Import the timezone module
from .models import ToDoList, ToDoItem

# List Unit Tests
class ToDoListTests(TestCase):
    def setUp(self):
        self.todo_list = ToDoList.objects.create(title="Test List")

    def test_list_view(self):
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.todo_list.title)

    def test_list_create_view(self):
        response = self.client.post(reverse("list-add"), {"title": "New List"})
        self.assertEqual(response.status_code, 302)  # Redirect after successful creation
        new_list = ToDoList.objects.get(title="New List")
        self.assertIsNotNone(new_list)

    def test_list_delete_view(self):
        response = self.client.post(reverse("list-delete", args=[self.todo_list.id]))
        self.assertEqual(response.status_code, 302)  # Redirect after successful deletion
        with self.assertRaises(ToDoList.DoesNotExist):
            ToDoList.objects.get(pk=self.todo_list.id)

# Item Unit Tests
class ToDoItemTests(TestCase):
    def setUp(self):
        self.todo_list = ToDoList.objects.create(title="Test List")
        self.todo_item = ToDoItem.objects.create(
            todo_list=self.todo_list,
            title="Test Item",
            description="Test Description",
            due_date=timezone.now() + timezone.timedelta(days=1),  # Use an aware datetime object
        )

    def test_item_list_view(self):
        response = self.client.get(reverse("list", args=[self.todo_list.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.todo_item.title)

    def test_item_create_view(self):
        response = self.client.post(
            reverse("item-add", args=[self.todo_list.id]),
            {
                "todo_list": self.todo_list.id,
                "title": "New Item",
                "description": "New Description",
                "due_date": timezone.now() + timezone.timedelta(days=2),  # Use an aware datetime object
            },
        )
        self.assertEqual(response.status_code, 302)  # Redirect after successful creation
        new_item = ToDoItem.objects.get(title="New Item")
        self.assertIsNotNone(new_item)

    def test_item_update_view(self):
        response = self.client.post(
            reverse("item-update", args=[self.todo_list.id, self.todo_item.id]),
            {
                "todo_list": self.todo_list.id,
                "title": "Updated Item",
                "description": "Updated Description",
                "due_date": timezone.now() + timezone.timedelta(days=3),  # Use an aware datetime object
                "completed": True,
            },
        )
        self.assertEqual(response.status_code, 302)  # Redirect after successful update
        updated_item = ToDoItem.objects.get(pk=self.todo_item.id)
        self.assertEqual(updated_item.title, "Updated Item")
        self.assertTrue(updated_item.completed)

    def test_item_delete_view(self):
        response = self.client.post(
            reverse("item-delete", args=[self.todo_list.id, self.todo_item.id])
        )
        self.assertEqual(response.status_code, 302)  # Redirect after successful deletion
        with self.assertRaises(ToDoItem.DoesNotExist):
            ToDoItem.objects.get(pk=self.todo_item.id)
