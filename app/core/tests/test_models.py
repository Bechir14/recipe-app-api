# test for models


from django.test import TestCase
from django.contrib.auth import get_user_model

class model_test(TestCase):
    def test_create_user_with_email_successful(self):
        email = "test@gmail.com"
        password = "testpass"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))