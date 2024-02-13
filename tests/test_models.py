from django.contrib.auth import get_user_model
from django.test import TestCase

from restaurant.models import Dish, Cook, DishType


class ModelsTests(TestCase):
    def test_dish_type_str(self):
        dish_type = DishType.objects.create(
            name="test",
        )
        self.assertEqual(str(dish_type), f"{dish_type.name}")

    def test_cook_str(self):
        cook = Cook.objects.create(
            username="test_user", first_name="test_first", last_name="test_last"
        )
        self.assertEqual(
            str(cook), f"{cook.username}" f" ({cook.first_name} {cook.last_name})"
        )

    def test_dish_str(self):
        dish_type = DishType.objects.create(name="test")
        dish = Dish.objects.create(name="test_name", price="15.50", dish_type=dish_type)
        self.assertEqual(
            str(dish), f"{dish.name} (price: {dish.price}, dish type: {dish.dish_type})"
        )

    def test_create_cook_with_year_of_experience(self):
        username = "test_user"
        password = "test123"
        year_of_experience = "10"
        cook = get_user_model().objects.create_user(
            username=username,
            password=password,
            year_of_experience=year_of_experience,
        )
        self.assertEqual(cook.username, username)
        self.assertEqual(cook.year_of_experience, year_of_experience)
        self.assertTrue(cook.check_password(password))

    def test_cook_get_absolute_url(self):
        cook = get_user_model().objects.create(
            username="test", first_name="test_first", last_name="test_last"
        )
        self.assertEqual(cook.get_absolute_url(), "/cook/1/")
