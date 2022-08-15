from dictionary.test import WrittenPronunciationTestCase
from dictionary.tests.factories import WordFactory


class WordListViewTests(WrittenPronunciationTestCase):
    def test_page(self):
        """Checks if Word list page is up and running."""
        self.get_check_200(url="home")

    def test_template(self):
        """Checks if Word list page uses correct template."""
        response = self.get(url_name="home")
        assert response.template_name == [
            "dictionary/home.html",
            "dictionary/word_list.html",
        ]

    def test_word_list(self):
        """Checks if Word appear in list page."""
        word = WordFactory(english="Visible", turkish="Vizıbl")

        response = self.get(url_name="home")
        self.assert_http_200_ok(response=response)

        assert word.english in response.content.decode("utf-8")
        assert word.turkish in response.content.decode("utf-8")
        assert word.author.username in response.content.decode("utf-8")

    def test_is_paginated(self):
        """Checks if Word list page is paginated."""
        WordFactory.create_batch(10)  # Creates specified number of Words.

        self.get(url_name="home")
        assert self.get_context(key="is_paginated") is True

    def test_pagination(self):
        """Checks if pagination works in Word list page."""
        WordFactory.create_batch(10)  # Creates specified number of Words.

        self.get(url_name="home")
        assert self.get_context(key="is_paginated") is True

        paginator = self.get_context(key="paginator")
        assert paginator.num_pages == 2  # Total number of pages.
        assert paginator.count >= 5  # Total number of Words in paginator's
        # queryset.


class WordDetailViewTests(WrittenPronunciationTestCase):
    def test_page(self):
        """Checks if Word detail page is up and running and has correct
        content."""
        word = WordFactory()

        response = self.get(url_name="word-detail", pk=word.id)
        self.assert_http_200_ok(response=response)

        assert word.english in response.content.decode("utf-8")
        assert word.turkish in response.content.decode("utf-8")
        assert word.author.username in response.content.decode("utf-8")

    def test_template(self):
        """Checks if Word detail page uses correct template."""
        word = WordFactory()

        response = self.get(url_name="word-detail", pk=word.id)
        assert response.template_name == [
            "dictionary/word_detail.html",
        ]


class WordCreateViewTests(WrittenPronunciationTestCase):
    def test_unauthenticated_user_can_create(self):
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

    def test_authenticated_user_can_create(self):
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

    def test_template(self):
        """Checks if create page uses correct template with authenticated
        user."""
        user = self.make_user()

        with self.login(user):
            response = self.get(url_name="word-create")
            self.assert_http_200_ok(response=response)

        assert response.template_name == [
            "dictionary/word_create.html",
        ]

    def test_content(self):
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


class WordUpdateViewTests(WrittenPronunciationTestCase):
    def test_unauthenticated_user_can_update(self):
        """Checks if Word update page is accessible to unauthenticated
        user."""
        word = WordFactory()
        redirect_url = (
            self.reverse(name="login") + f"?next=/{word.id}/update/"
        )  # /users/login/?next=/1/update/

        response = self.get(url_name="word-update", pk=word.id)
        self.assert_http_302_found(response=response)
        assert response.url == redirect_url  # Check if unauthenticated user
        # is redirected to login page with correct next parameter.

    def test_unauthorized_user_can_access(self):
        """Checks if Word update page is accessible to unauthorized
        user (i.e.: user that is not author of Word)."""
        user = self.make_user()
        word = WordFactory()

        with self.login(user):
            response = self.get(url_name="word-update", pk=word.id)
            self.assert_http_403_forbidden(response=response)

    def test_authorized_user_can_access(self):
        """Checks if Word update page is accessible to authorized user
        (i.e.: user that is author of Word)."""
        user = self.make_user()
        word = WordFactory(author=user)

        with self.login(user):
            response = self.get(url_name="word-update", pk=word.id)
            self.assert_http_200_ok(response=response)

    def test_authorized_user_can_update(self):
        """Checks if authorized user (i.e.: user that is author of Word)
        can update Word."""
        user = self.make_user()
        word = WordFactory(author=user)
        data = {
            "english": "test-english-updated",
            "turkish": "test-turkish-updated",
        }

        with self.login(user):
            response = self.post(url_name="word-update", pk=word.id, data=data)
            self.assert_http_302_found(response=response)

        response = self.get(url_name="word-detail", pk=word.id)
        self.assert_http_200_ok(response=response)
        assert data["english"] in response.content.decode("utf-8")
        assert data["turkish"] in response.content.decode("utf-8")
        assert user.username in response.content.decode("utf-8")

    def test_template(self):
        """Checks if Word update page uses correct template."""
        user = self.make_user()
        word = WordFactory(author=user)

        with self.login(user):
            response = self.get(url_name="word-update", pk=word.id)
            self.assert_http_200_ok(response=response)

        assert response.template_name == [
            "dictionary/word_update.html",
        ]

    def test_content(self):
        """Checks if Word update page has correct content."""
        user = self.make_user()
        word = WordFactory(author=user)

        with self.login(user):
            response = self.get(url_name="word-update", pk=word.id)
            self.assert_http_200_ok(response=response)

        assert "Update" in response.content.decode("utf-8")
        assert "English word" in response.content.decode("utf-8")
        assert "Turkish word" in response.content.decode("utf-8")


class WordDeleteViewTests(WrittenPronunciationTestCase):
    def test_unauthenticated_user_can_access(self):
        """Checks if Word delete page is accessible to unauthenticated
        user."""
        word = WordFactory()
        redirect_url = (
            self.reverse(name="login") + f"?next=/{word.id}/delete/"
        )  # /users/login/?next=/1/delete/

        response = self.get(url_name="word-delete", pk=word.id)
        self.assert_http_302_found(response=response)
        assert response.url == redirect_url  # Check if unauthenticated user
        # is redirected to login page with correct next parameter.

    def test_unauthorized_user_can_access(self):
        """Checks if Word delete page is accessible to unauthorized
        user (i.e.: user that is not author of Word)."""
        user = self.make_user()
        word = WordFactory()

        with self.login(user):
            response = self.get(url_name="word-delete", pk=word.id)
            self.assert_http_403_forbidden(response=response)

    def test_authorized_user_can_access(self):
        """Checks if Word delete page is accessible to authorized user
        (i.e.: user that is author of Word)."""
        user = self.make_user()
        word = WordFactory(author=user)

        with self.login(user):
            response = self.get(url_name="word-delete", pk=word.id)
            self.assert_http_200_ok(response=response)

    def test_authorized_user_can_delete(self):
        """Checks if authorized user (i.e.: user that is author of Word)
        can delete Word."""
        user = self.make_user()
        word = WordFactory(english="ANNIHILATE", author=user)

        with self.login(user):
            response = self.post(url_name="word-delete", pk=word.id)
            self.assert_http_302_found(response=response)
            assert response.url == self.reverse(name="home")  # Check if
            # redirected page is correct.

        response = self.get(url_name="home")
        assert word.english not in response.content.decode("utf-8")
        assert word.turkish not in response.content.decode("utf-8")

    def test_template(self):
        """Checks if Word delete page uses correct template."""
        user = self.make_user()
        word = WordFactory(author=user)

        with self.login(user):
            response = self.get(url_name="word-delete", pk=word.id)
            self.assert_http_200_ok(response=response)

        assert response.template_name == [
            "dictionary/word_delete.html",
        ]

    def test_content(self):
        """Checks if Word delete page has correct content."""
        user = self.make_user()
        word = WordFactory(author=user)

        with self.login(user):
            response = self.get(url_name="word-delete", pk=word.id)
            self.assert_http_200_ok(response=response)

        assert "Delete" in response.content.decode("utf-8")
        assert "Confirm" in response.content.decode("utf-8")


class SearchViewTests(WrittenPronunciationTestCase):
    def test_template(self):
        """Checks if search page uses correct template."""
        response = self.get(url_name="search", data={"q": "test"})
        self.assert_http_200_ok(response=response)

        assert response.template_name == [
            "dictionary/search.html",
            "dictionary/word_list.html",
        ]

    def test_searching(self):
        """Checks if search page works properly."""
        word = WordFactory(english="search-test", turkish="search-test")
        word_excluded = WordFactory(
            english="must-not-appear", turkish="must-not-appear"
        )

        response = self.get(url_name="search", data={"q": "test"})
        self.assert_http_200_ok(response=response)

        assert word.english in response.content.decode("utf-8")
        assert word.turkish in response.content.decode("utf-8")
        assert word.author.username in response.content.decode("utf-8")
        assert word_excluded.english not in response.content.decode("utf-8")
        assert word_excluded.turkish not in response.content.decode("utf-8")
        assert word_excluded.author.username not in response.content.decode(
            "utf-8"
        )

    def test_is_paginated(self):
        """Checks if search page is paginated."""
        WordFactory.create_batch(10)  # Creates specified number of Words.

        self.get(url_name="search", data={"q": ""})
        assert self.get_context(key="is_paginated") is True

    def test_pagination(self):
        """Checks if pagination works in search page."""
        for i in range(10):
            WordFactory(english=f"test{i}")

        response = self.get(url_name="search", data={"q": "test", "page": 2})
        self.assert_http_200_ok(response=response)
        assert self.get_context(key="is_paginated") is True

        paginator = self.get_context(key="paginator")
        assert paginator.num_pages == 2  # Total number of pages.
        assert paginator.count >= 5  # Total number of Words in paginator's
        # queryset.


class UserWordListViewTests(WrittenPronunciationTestCase):
    def test_template(self):
        """Checks if user word list page uses correct template."""
        user = self.make_user()
        WordFactory(author=user)

        with self.login(user):
            response = self.get(url_name="user-words", username=user.username)
            self.assert_http_200_ok(response=response)

        assert response.template_name == [
            "dictionary/user_word_list.html",
            "dictionary/word_list.html",
        ]

    def test_page(self):
        """Checks if user word list page works properly."""
        user = self.make_user()
        word = WordFactory(author=user)

        with self.login(user):
            response = self.get(url_name="user-words", username=user.username)
            self.assert_http_200_ok(response=response)

        assert word.english in response.content.decode("utf-8")
        assert word.turkish in response.content.decode("utf-8")
        assert word.author.username in response.content.decode("utf-8")

    def test_is_paginated(self):
        """Checks if user word list page is paginated."""
        user = self.make_user()
        for _ in range(10):
            WordFactory(author=user)

        self.get(url_name="user-words", username=user.username)
        assert self.get_context(key="is_paginated") is True

    def test_pagination(self):
        """Checks if pagination works in user word list page."""
        user = self.make_user()
        for _ in range(10):
            WordFactory(author=user)

        self.get(url_name="user-words", username=user.username)
        assert self.get_context(key="is_paginated") is True

        paginator = self.get_context(key="paginator")
        assert paginator.num_pages == 2  # Total number of pages.
        assert paginator.count >= 5  # Total number of Words in paginator's
        # queryset.
