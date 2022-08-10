from dictionary.test import WrittenPronunciationTestCase

from dictionary.tests.factories import WordFactory


class WordModelTests(WrittenPronunciationTestCase):
    """Creates mock model and checks if it is created successfully."""

    @classmethod
    def setUpTestData(cls):
        cls.test_word = WordFactory(english="Factory")

    def test_is_created(self):
        assert self.test_word.english == "Factory"
        assert self.test_word.turkish == "Fektri"
        assert self.test_word.is_approved is True
        assert self.test_word.author is not None
