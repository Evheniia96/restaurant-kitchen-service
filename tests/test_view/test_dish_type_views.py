from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse


DISH_TYPE_URL = reverse("restaurant:dish-type-list")
DISH_URL = reverse("restaurant:dish-list")
COOK_URL = reverse("restaurant:cook-list")


class PublicDishTypeTests(TestCase):
    def setUp(self) -> None:
        self.client = Client()

    def test_login_required(self):
        dish_type = self.client.get(DISH_TYPE_URL)
        dish = self.client.get(DISH_URL)
        cook = self.client.get(COOK_URL)
        self.assertNotEqual(dish_type.status_code, 200)
        self.assertNotEqual(dish.status_code, 200)
        self.assertNotEqual(cook.status_code, 200)


class PrivateDishTypeTests(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="test",
            password="testPASSWORD",
        )
        self.client.force_login(self.user)


class PublicDishTests(TestCase):
    def setUp(self) -> None:
        self.client = Client()
