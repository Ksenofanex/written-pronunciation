from django.test import TestCase
from django.contrib.auth import get_user_model
from dictionary.models import Word


class MaterialTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(
            username="testuser1",
            password="deneme123",
        )
        testuser1.save()

        word = Word.objects.create(
            english="Computer", author=testuser1, turkish="Kompitür"
        )
        word.save()

    def test_word(self):
        word = Word.objects.get(id=1)
        english = f"{word.english}"
        author = f"{word.author.username}"
        turkish = f"{word.turkish}"
        self.assertEqual(english, "Computer")
        self.assertEqual(author, "testuser1")
        self.assertEqual(turkish, "Kompitür")
