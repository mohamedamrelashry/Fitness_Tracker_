from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Activity
from rest_framework.test import APIClient
from datetime import date

User = get_user_model()

class ActivityAPITest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='alice', password='pass123')
        Activity.objects.create(user=self.user, activity_type='running', duration_minutes=30, date=date.today())
        self.client = APIClient()

    def test_list_requires_auth(self):
        res = self.client.get('/api/activities/')
        self.assertIn(res.status_code, (401, 403))

    def test_user_activity_list(self):
        self.client.login(username='alice', password='pass123')
        res = self.client.get('/api/activities/')
        self.assertEqual(res.status_code, 200)
