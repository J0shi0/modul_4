from django.test import TestCase
from django.urls import reverse

from rest_framework.test import APITestCase
from rest_framework import status

from .models import Task, Comment, Tag

import unittest

data = {
    "title": "Тестовая задача",
    "description": "Тестовое описание",
}


class TaskTests(APITestCase):

    def setUp(self):
        self.task = Task.objects.create(
            title='Тестовая задача',
            description='Тестовое описание'
        )

    def test_create_task(self):
        response = self.client.post(reverse('task-list'),
                                    data={"title": "Тестовая задача", "description": "Тестовое описание",})

        self.assertEqual(response.status_code, 201)
        task = Task.objects.all().first()
        self.assertEqual(task.title, "Тестовая задача")
        self.assertEqual(task.description, "Тестовое описание")

    def test_edit_task(self):
        self.task.title = "Обновленный заголовок"
        self.task.save()
        updated_task = Task.objects.get(id=self.task.id)
        self.assertEqual(updated_task.title, "Обновленный заголовок")

    def test_delete_task(self):
        task_id = self.task.id
        self.task.delete()
        with self.assertRaises(Task.DoesNotExist):
            Task.objects.get(id=task_id)

    def test_view_task(self):
        task = Task.objects.get(id=self.task.id)
        self.assertEqual(task.title, "Тестовая задача")
        self.assertEqual(task.description, "Тестовое описание")


class TaskIntegrationTestCase(TestCase):
    def setUp(self):
        self.task = Task.objects.create(title="Тестовая задача", description="Тестовое описание")
        self.tag = Tag.objects.create(name="Тестовый тэг")

    def test_add_comment_to_task(self):
        comment = Comment.objects.create(task=self.task, text="Тестовый комментарий")
        self.task.refresh_from_db()
        self.assertIn(comment, self.task.comments.all())

    def test_add_tags_to_task(self):
        self.task.tags.add(self.tag)
        self.task.refresh_from_db()
        self.assertIn(self.tag, self.task.tags.all())