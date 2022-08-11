from dictionary.test import WrittenPronunciationTestCase
from dictionary.tests.factories import WordFactory
from dictionary.models import Word


class WordViewSetTests(WrittenPronunciationTestCase):
    def test_list_page(self):
        """Checks if Word list page is accessible to all."""
        self.get_check_200(url="v1:word-list")

    def test_object_list(self):
        """Checks if newly created and approved Word appears in list page."""
        word = WordFactory()

        response = self.get(url_name="v1:word-list")
        self.assert_http_200_ok(response=response)
        assert response.data["count"] == 1

        relevant_response_data = response.data["results"][0]
        assert word.english in relevant_response_data["english"]
        assert word.turkish in relevant_response_data["turkish"]
        assert word.author.username in relevant_response_data["author_name"]

    def test_unapproved_object(self):
        """Checks if unapproved Word is visible in list page."""
        WordFactory(is_approved=False)

        response = self.get(url_name="v1:word-list")
        self.assert_http_200_ok(response=response)
        assert response.data["count"] == 0

    def test_detail_page(self):
        """Checks if Word detail page is accessible to all."""
        word = WordFactory()

        self.get_check_200(url="v1:word-detail", pk=word.pk)
        assert word.english in self.last_response.data["english"]
        assert word.turkish in self.last_response.data["turkish"]
        assert word.author.username in self.last_response.data["author_name"]

    def test_unauthenticated_user_can_create(self):
        """Checks if unauthenticated user is able to create Word."""
        word_data = {
            "english": "test-you-shall-not-create-troll",
            "turkish": "test-you-shall-not-create-troll",
        }

        response = self.post(url_name="v1:word-list", data=word_data)
        self.assert_http_403_forbidden(response=response)

    def test_authenticated_user_can_create(self):
        """Checks if authenticated user is able to create Word."""
        test_user = self.make_user(username="test1")
        word_data = {
            "english": "test-all-good-bud",
            "turkish": "test-all-good-bud",
        }

        with self.login(test_user):
            response = self.post(url_name="v1:word-list", data=word_data)
            self.assert_http_201_created(response=response)

    def test_unauthorized_user_can_change(self):
        """Checks if unauthorized user (i.e.: user that doesn't own Word)
        can change Word."""
        unauthorized_user = self.make_user(username="unauthorized_user")
        word = WordFactory()
        word_data = {
            "english": "test-damn-you-unauthorized",
            "turkish": "test-damn-you-unauthorized",
        }

        with self.login(unauthorized_user):
            response = self.put(
                url_name="v1:word-detail",
                pk=word.id,
                data=word_data,
            )
            self.assert_http_403_forbidden(response=response)

    def test_authorized_user_can_change(self):
        """Checks if authorized user (i.e.: user that owns Word) can
        change Word."""
        authorized_user = self.make_user(username="authorized_user")
        word = WordFactory(author=authorized_user)
        word_data = {
            "english": "test-watch-out-for-writer's-block",
            "turkish": "test-watch-out-for-writer's-block",
        }

        with self.login(authorized_user):
            response = self.put(
                url_name="v1:word-detail",
                pk=word.id,
                data=word_data,
            )
            self.assert_http_200_ok(response=response)

    def test_unauthorized_user_can_delete(self):
        """Checks if unauthorized user (i.e.: user that doesn't own Word)
        can delete Word."""
        unauthorized_user = self.make_user(username="unauthorized_user")
        word = WordFactory()

        with self.login(unauthorized_user):
            response = self.delete(url_name="v1:word-detail", pk=word.id)
            self.assert_http_403_forbidden(response=response)

    def test_authorized_user_can_delete(self):
        """Checks if authorized user (i.e.: user that owns Word) can
        delete Word."""
        authorized_user = self.make_user(username="authorized_user")
        word = WordFactory(author=authorized_user)

        with self.login(authorized_user):
            response = self.delete(url_name="v1:word-detail", pk=word.id)
            self.assert_http_204_no_content(response=response)

        assert Word.objects.count() == 0

    def test_is_paginated(self):
        """Checks if Word list page is paginated."""
        WordFactory.create_batch(15)

        response = self.get(url_name="v1:word-list")
        self.assert_http_200_ok(response=response)
        assert response.data["count"] >= 10
        assert response.data["next"] is not None
        assert response.data["previous"] is None

    def test_filtering(self):
        """Checks if filtering works properly in list page."""
        word = WordFactory(english="test-filter", turkish="test-filter")
        WordFactory(english="must-not-appear", turkish="must-not-appear")

        response = self.get(
            url_name="v1:word-list", data={"english": "filter"}
        )
        self.assert_http_200_ok(response=response)
        assert response.data["count"] == 1

        relevant_response_data = response.data["results"][0]
        assert word.english in relevant_response_data["english"]
        assert word.turkish in relevant_response_data["turkish"]
        assert word.author.username in relevant_response_data["author_name"]
