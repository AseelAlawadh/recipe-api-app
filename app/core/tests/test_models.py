from django.contrib.auth import get_user_model
from django.test import TestCase


class ModelTest(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating new user with an emaill is successful """
        email = "test@test.com"
        password = "test1234"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """ Test email for a new user is normalized"""
        email = "test@TEST.COM"
        user = get_user_model().objects.create_user(email, 'test124')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """ Test creating email without no email raises errors"""
        with self.assertRaises(ValueError):
            # any thing that we run here should raise a ValueError if doesn't raise a ValueError then the test will faill
            get_user_model().objects.create_user(None, 'test124')

    # test superuser
    def test_create_new_superuser(self):
        """Test creating new superuser """
        user = get_user_model().objects.create_superuser(
            'test@test.com',
            'test124'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
