from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Note

class NoteTests(APITestCase):

    def test_create_note(self):
        url = reverse('note-create')
        data = {'title': 'Test Note', 'body': 'This is a test note.'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Note.objects.count(), 1)
        self.assertEqual(Note.objects.get().title, 'Test Note')