from django.urls import path
from .views import index, CookListView, DishListView, DishTypeListView

urlpatterns = [
    path("", index, name="index"),
    path("cook/", CookListView.as_view(), name="cook-list"),
    path("dish/", DishListView.as_view(), name="dish-list"),
    path("dish_type/", DishTypeListView.as_view(), name="dish-type-list"),
    ]

app_name = "restaurant"
