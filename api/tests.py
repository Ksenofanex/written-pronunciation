from django.test import TestCase
from django.contrib.auth import get_user_model
from dictionary.models import Word

User = get_user_model()


class MaterialTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        testuser1 = User.objects.create_user(
            username="testuser1",
            password="deneme123",
        )
        Word.objects.create(
            english="Computer", author=testuser1, turkish="Kompitür"
        )

    def test_word(self):
        word = Word.objects.first()
        self.assertEqual(word.english, "Computer")
        self.assertEqual(word.author.username, "testuser1")
        self.assertEqual(word.turkish, "Kompitür")
