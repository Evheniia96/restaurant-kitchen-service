from django.urls import path
from .views import index, CookListView, DishListView, DishTypeListView, DishDetailView, CookDetailView, DishCreateView, \
    CookCreateView, DishTypeCreateView, CookExperienceUpdateView

urlpatterns = [
    path("", index, name="index"),
    path("cook/", CookListView.as_view(), name="cook-list"),
    path("cook/<int:pk>/", CookDetailView.as_view(), name="cook-detail"),
    path("cook/create/", CookCreateView.as_view(), name="cook-create"),
    path("cook/<int:pk>/update/", CookExperienceUpdateView.as_view(), name="cook-update"),
    path("dish/", DishListView.as_view(), name="dish-list"),
    path("dish/create/", DishCreateView.as_view(), name="dish-create"),
    path("dish_type/", DishTypeListView.as_view(), name="dish-type-list"),
    path("dish_type/create/", DishTypeCreateView.as_view(), name="dish-type-create"),
    path("dish/<int:pk>/", DishDetailView.as_view(), name="dish-detail"),
    ]

app_name = "restaurant"
