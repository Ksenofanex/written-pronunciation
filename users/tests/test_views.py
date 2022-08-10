from django.contrib.auth import get_user_model

from dictionary.test import WrittenPronunciationTestCase

User = get_user_model()


class LoginViewTests(WrittenPronunciationTestCase):
    def test_page(self):
        """Checks if login page is up and running."""
        self.get_check_200(url="login")

    def test_template(self):
        """Checks if login page uses correct template."""
        response = self.get(url_name="login")
        assert response.template_name == ["registration/login.html"]

    def test_content(self):
        """Checks if login page contains correct content."""
        response = self.get(url_name="login")
        assert "Login" in response.content.decode("utf-8")
        assert "Username" in response.content.decode("utf-8")
        assert "Password" in response.content.decode("utf-8")

    def test_form(self):
        """Checks if login page form works properly and user is logged in
        successfully."""
        self.make_user(username="test-user-1", password="test-password")
        data = {
            "username": "test-user-1",
            "password": "test-password",
        }

        response = self.post(url_name="login", data=data)
        self.assert_http_302_found(response=response)
        assert response.url == self.reverse(name="home")  # Check if redirected
        # page is correct.


class SignUpViewTests(WrittenPronunciationTestCase):
    def test_page(self):
        """Checks if signup page is up and running."""
        self.get_check_200(url="signup")

    def test_template(self):
        """Checks if signup page uses correct template."""
        response = self.get(url_name="signup")
        assert response.template_name == ["signup.html"]

    def test_content(self):
        """Checks if signup page contains correct content."""
        response = self.get(url_name="signup")
        assert "Sign Up" in response.content.decode("utf-8")
        assert "Username" in response.content.decode("utf-8")
        assert "Password" in response.content.decode("utf-8")
        assert "Password confirmation" in response.content.decode("utf-8")

    def test_form(self):
        """Checks if signup page form works properly and user is created
        successfully."""
        data = {
            "username": "new-user",
            "password1": "test.password.",
            "password2": "test.password.",
        }

        response = self.post(url_name="signup", data=data)
        self.assert_http_302_found(response=response)
        assert response.url == self.reverse(name="login")  # Check if
        # redirected page is correct.

        assert User.objects.count() == 1
        assert User.objects.first().username == "new-user"
        assert User.objects.first().check_password("test.password.") is True
