from rest_framework.test import APIClient

from test_plus.test import TestCase as PlusTestCase

from users.tests.factories import UserFactory


class WrittenPronunciationTestCase(PlusTestCase):
    """django-test-plus package's base test class."""

    user_factory = UserFactory
    client_class = APIClient
