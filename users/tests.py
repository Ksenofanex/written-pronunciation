from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

User = get_user_model()


class CustomUserTests(TestCase):
    def test_create_user(self):
        user = User.objects.create_user(
            username="hedaelus",
            email="hedaelus@gmail.com",
            password="test",
        )
        self.assertEqual(user.username, "hedaelus")
        self.assertEqual(user.email, "hedaelus@gmail.com")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        admin_user = User.objects.create_superuser(
            username="superadmin",
            email="superadmin@admin.com",
            password="admin123",
        )
        self.assertEqual(admin_user.username, "superadmin")
        self.assertEqual(admin_user.email, "superadmin@admin.com")
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)


class SignupTests(TestCase):
    username = "newuser"
    email = "newuser@email.com"

    def setUp(self):
        url = reverse("signup")
        self.response = self.client.get(url)

    def test_signup_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, "signup.html")
        self.assertContains(self.response, "Sign Up")
        self.assertNotContains(
            self.response, "Hi there! I should not on this page."
        )

    def test_signup_form(self):
        User.objects.create_user(self.username)
        self.assertEqual(User.objects.all().count(), 1)
        self.assertEqual(User.objects.first().username, self.username)
