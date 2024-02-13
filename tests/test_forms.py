from django.test import TestCase
from restaurant.forms import (
    CookCreationForm,
    CookSearchForm,
    DishTypeSearchForm,
    DishSearchForm,
)


class CookCreationFormTest(TestCase):
    def test_cook_creation_form_is_valid(self):
        form_date = {
            "username": "test",
            "password1": "testPASSWORD",
            "password2": "testPASSWORD",
            "year_of_experience": 5,
            "first_name": "test_first",
            "last_name": "test_last",
        }
        form = CookCreationForm(data=form_date)
        self.assertTrue(form.is_valid())
        self.assertEquals(form.cleaned_data, form_date)


class CookSearchFormTest(TestCase):
    def test_cook_search_form_is_valid(self):
        form_date = {"username": "test"}
        form = CookSearchForm(data=form_date)
        self.assertTrue(form.is_valid())


class DishTypeSearchFormTest(TestCase):
    def test_dish_type_search_form_is_valid(self):
        form_date = {"name": "test_name_dish_type"}
        form = DishTypeSearchForm(data=form_date)
        self.assertTrue(form.is_valid())


class DishSearchFormTest(TestCase):
    def test_car_search_form_is_valid(self):
        form_date = {"name": "test_name_dish"}
        form = DishSearchForm(data=form_date)
        self.assertTrue(form.is_valid())
