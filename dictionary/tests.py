from django.test import TestCase
from django.urls import reverse


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