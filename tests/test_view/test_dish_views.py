from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from restaurant.models import Dish, DishType

DISH_URL = reverse("restaurant:dish-list")
DISH_CREATE_URL = reverse("restaurant:dish-create")


class PublicDishTests(TestCase):
    def setUp(self) -> None:
        self.client = Client()

    def test_login_required(self):
        dish = self.client.get(DISH_URL)
        self.assertNotEqual(dish.status_code, 200)

    def test_create_login_required(self):
        dish = self.client.get(DISH_CREATE_URL)
        self.assertNotEqual(dish.status_code, 200)

    def test_update_delete_login_required(self):
        dish_type = DishType.objects.create(name="test_dish_type")
        Dish.objects.create(
            dish_type=dish_type,
            name="Test_name",
            price=100
        )
        dish = self.client.get(reverse(
            "restaurant:dish-update",
            kwargs={"pk": 1}
        ))
        self.assertNotEqual(dish.status_code, 200)

        dish = self.client.get(reverse(
            "restaurant:dish-delete",
            kwargs={"pk": 1}
        ))
        self.assertNotEqual(dish.status_code, 200)


class PrivateDishTests(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="test",
            password="testPASSWORD",
        )
        self.client.force_login(self.user)

    def test_retrieve_dish(self):
        dish_type = DishType.objects.create(name="dish_type_test")
        Dish.objects.create(name="Napoleon", price=15.20, dish_type=dish_type)
        Dish.objects.create(name="Cake", price=15.50, dish_type=dish_type)
        response = self.client.get(DISH_URL)
        self.assertEqual(response.status_code, 200)
        dish = Dish.objects.all()
        self.assertEqual(
            list(response.context["dish_list"]),
            list(dish)
        )
        self.assertTemplateUsed(response, "restaurant/dish_list.html")


class SearchTests(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="test",
            password="testPASSWORD",
        )
        self.client.force_login(self.user)

    def test_search_dish(self):
        dish_type = DishType.objects.create(name="dish_type_test")
        Dish.objects.create(name="Napoleon", price=5.10, dish_type=dish_type)
        response = self.client.get(DISH_URL + "?name=Napoleon")
        self.assertEqual(response.status_code, 200)
