from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from restaurant.models import DishType

DISH_TYPE_URL = reverse("restaurant:dish-type-list")
DISH_TYPE_CREATE_URL= reverse("restaurant:dish-type-create")


class PublicDishTypeTests(TestCase):
    def setUp(self) -> None:
        self.client = Client()

    def test_login_required(self):
        dish_type = self.client.get(DISH_TYPE_URL)
        self.assertNotEqual(dish_type.status_code, 200)

    def test_create_login_required(self):
        dish_type = self.client.get(DISH_TYPE_CREATE_URL)
        self.assertNotEqual(dish_type.status_code, 200)

    def test_update_delete_login_required(self):
        DishType.objects.create(
            name="Test_name"
        )
        dish_type = self.client.get(reverse(
            "restaurant:dish_type-update",
            kwargs={"pk": 1}
        ))
        self.assertNotEqual(dish_type.status_code, 200)

        dish_type = self.client.get(reverse(
            "restaurant:dish-type-delete",
            kwargs={"pk": 1}
        ))
        self.assertNotEqual(dish_type.status_code, 200)


class PrivateDishTypeTests(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="test",
            password="testPASSWORD",
        )
        self.client.force_login(self.user)

    def test_retrieve_dish_types(self):
        DishType.objects.create(name="Pasta")
        DishType.objects.create(name="Pizza")
        response = self.client.get(DISH_TYPE_URL)
        self.assertEqual(response.status_code, 200)
        dish_type = DishType.objects.all()
        self.assertEqual(
            list(response.context["dish_type_list"]),
            list(dish_type)
        )
        self.assertTemplateUsed(response, "restaurant/dish_type_list.html")

    def test_search_dish_types(self):
        DishType.objects.create(name="Pizza")
        response = self.client.get(DISH_TYPE_URL + "?name=Pizza")
        self.assertEqual(response.status_code, 200)

