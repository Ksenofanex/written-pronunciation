from dictionary.test import WrittenPronunciationTestCase
from dictionary.tests.factories import WordFactory


class WordListViewTests(WrittenPronunciationTestCase):
    def test_if_word_list_page_works(self):
        """Checks if Word list page is up and running."""
        self.get_check_200(url="home")

    def test_if_word_list_page_uses_correct_template(self):
        """Checks if Word list page uses correct template."""
        response = self.get(url_name="home")
        assert response.template_name == [
            "dictionary/home.html",
            "dictionary/word_list.html",
        ]

    def test_if_word_appear_in_list_page(self):
        """Checks if Word appear in list page."""
        word = WordFactory(english="Visible", turkish="Vizıbl")

        response = self.get(url_name="home")
        self.assert_http_200_ok(response=response)

        assert word.english in response.content.decode("utf-8")
        assert word.turkish in response.content.decode("utf-8")
        assert word.author.username in response.content.decode("utf-8")

    def test_if_word_list_page_is_paginated(self):
        """Checks if Word list page is paginated."""
        WordFactory.create_batch(10)  # Creates specified number of Words.

        self.get(url_name="home")
        assert self.get_context(key="is_paginated") is True


class WordDetailViewTests(WrittenPronunciationTestCase):
    def test_if_word_detail_page_works(self):
        """Checks if Word detail page is up and running and has correct
        content."""
        word = WordFactory()

        response = self.get(url_name="word-detail", pk=word.id)
        self.assert_http_200_ok(response=response)

        assert word.english in response.content.decode("utf-8")
        assert word.turkish in response.content.decode("utf-8")
        assert word.author.username in response.content.decode("utf-8")

    def test_if_word_detail_page_uses_correct_template(self):
        """Checks if Word detail page uses correct template."""
        word = WordFactory()

        response = self.get(url_name="word-detail", pk=word.id)
        assert response.template_name == [
            "dictionary/word_detail.html",
        ]


class WordCreateViewTests(WrittenPronunciationTestCase):
    def test_if_unauthenticated_user_is_able_to_create_a_word(self):
        """Checks if unauthenticated user is able to create a Word and
        redirected to login page."""
        data = {
            "english": "test-english",
            "turkish": "test-turkish",
        }

        response = self.post(url_name="word-create", data=data)
        self.assert_http_302_found(response=response)
        assert response.url == self.reverse(name="login") + "?next=/create/"
        # /users/login/?next=/create/ Check if unauthenticated user is
        # redirected to login page with correct next parameter.

    def test_if_authenticated_user_is_able_to_create_a_word(self):
        """Checks if authenticated user is able to create a Word."""
        user = self.make_user()
        data = {
            "english": "test-english",
            "turkish": "test-turkish",
        }

        with self.login(user):
            response = self.post(url_name="word-create", data=data)
            self.assert_http_302_found(response=response)

        response = self.get(
            url_name="word-detail", pk=response["location"].split("/")[-2]
        )  # Fetching ID from /1/ and checking created Word's detail page.
        self.assert_http_200_ok(response=response)

        assert data["english"] in response.content.decode("utf-8")
        assert data["turkish"] in response.content.decode("utf-8")
        assert user.username in response.content.decode("utf-8")

    def test_if_create_page_uses_correct_template(self):
        """Checks if create page uses correct template with authenticated
        user."""
        user = self.make_user()

        with self.login(user):
            response = self.get(url_name="word-create")
            self.assert_http_200_ok(response=response)

        assert response.template_name == [
            "dictionary/word_create.html",
        ]

    def test_if_create_page_has_correct_content(self):
        """Checks if create page has correct content with authenticated
        user."""
        user = self.make_user()

        with self.login(user):
            response = self.get(url_name="word-create")
            self.assert_http_200_ok(response=response)

        assert "New Word" in response.content.decode("utf-8")
        assert "English word" in response.content.decode("utf-8")
        assert "Turkish word" in response.content.decode("utf-8")
        assert "Send Word" in response.content.decode("utf-8")


