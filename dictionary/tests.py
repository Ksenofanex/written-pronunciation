from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import Word


class HomePageTests(TestCase):

    def setUp(self):
        url = reverse('home')
        self.response = self.client.get(url)

    def test_homepage_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_homepage_template(self):
        self.assertTemplateUsed(self.response, 'dictionary/home.html')

    def test_homepage_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.response, 'Hi there! I should not be on this page.')


class WordTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            password='testpass123',
        )

        self.word = Word.objects.create(
            english='Blood',
            author=self.user,
            turkish='Blad',
        )

    def test_word_listing(self):
        self.assertEqual(f'{self.word.english}', 'Blood')
        self.assertEqual(f'{self.word.author}', self.user.username)
        self.assertEqual(f'{self.word.turkish}', 'Blad')

    def test_word_list_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'dictionary/home.html')

    def test_book_detail_view(self):
        response = self.client.get(self.word.get_absolute_url())
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'testuser')
        self.assertTemplateUsed(response, 'dictionary/word_detail.html')