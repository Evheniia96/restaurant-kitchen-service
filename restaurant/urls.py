from django.urls import path
from .views import index, CookListView, DishListView, DishTypeListView, DishDetailView, CookDetailView

urlpatterns = [
    path("", index, name="index"),
    path("cook/", CookListView.as_view(), name="cook-list"),
    path("dish/", DishListView.as_view(), name="dish-list"),
    path("dish_type/", DishTypeListView.as_view(), name="dish-type-list"),
    path("dish/<int:pk>/", DishDetailView.as_view(), name="dish-detail"),
    path("cook/<int:pk>/", CookDetailView.as_view(), name="cook-detail"),
    ]

app_name = "restaurant"
