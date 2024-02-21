from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from restaurant.forms import CookSearchForm

COOK_URL = reverse("restaurant:cook-list")
COOK_CREATE_URL = reverse("restaurant:cook-create")


class PublicCookTests(TestCase):
    def setUp(self) -> None:
        self.client = Client()

    def test_login_required(self):
        cook = self.client.get(COOK_URL)
        self.assertNotEqual(cook.status_code, 200)


class PrivateCookTests(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="test",
            password="testPASSWORD",
        )
        self.client.force_login(self.user)

    def test_get_content_data(self):
        res = self.client.get(COOK_URL)
        self.assertIsInstance(res.context["search_form"], CookSearchForm)

    def test_create_cook(self):
        form_data = {
            "username": "test_username",
            "password1": "Test12345",
            "password2": "Test12345",
            "first_name": "test_first",
            "last_name": "test_last",
            "year_of_experience": 5,
        }
        self.client.post(COOK_CREATE_URL, form_data)
        user = get_user_model().objects.get(username=form_data["username"])

        self.assertEqual(user.first_name, form_data["first_name"])
        self.assertEqual(user.last_name, form_data["last_name"])
        self.assertEqual(user.year_of_experience, form_data["year_of_experience"])
