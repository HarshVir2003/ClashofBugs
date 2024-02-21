from django.test import TestCase
from .models import User


class UserModelTestCase(TestCase):
    def test_user_uid_generation(self):
        # Create a user without specifying the UID
        user = User.objects.create(username='testuser', xp=100, trophies=5)

        # Retrieve the created user from the database
        saved_user = User.objects.get(username='testuser')

        # Check if the UID is generated (non-empty) for the user
        self.assertIsNotNone(saved_user.UID)
        self.assertNotEqual(saved_user.UID, '')  # Ensure UID is not an empty string
