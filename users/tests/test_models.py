from dictionary.test import WrittenPronunciationTestCase

from users.tests.factories import UserFactory


class UserModelTests(WrittenPronunciationTestCase):
    """Creates mock models and checks if they are created successfully."""

    @classmethod
    def setUpTestData(cls):
        cls.test_user = UserFactory(
            username="test-user-1",
            email="test-user-email@protonmail.com",
            password="test-password",
        )
        cls.superuser = UserFactory(
            username="superuser_1",
            email="test-superuser-email@protonmail.com",
            password="test_password",
            is_superuser=True,
        )

    def test_if_user_is_created(self):
        assert self.test_user.username == "test-user-1"
        assert self.test_user.email == "test-user-email@protonmail.com"
        assert self.test_user.password == "test-password"

    def test_if_super_user_is_created(self):
        assert self.superuser.username == "superuser_1"
        assert self.superuser.email == "test-superuser-email@protonmail.com"
        assert self.superuser.password == "test_password"
        assert self.superuser.is_superuser is True
