from django.urls import path
from .views import index, CookListView

urlpatterns = [
    path("", index, name="index"),
    path("cook/", CookListView.as_view(), name="cook-list")
    ]

app_name = "restaurant"
