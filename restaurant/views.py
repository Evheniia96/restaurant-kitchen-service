from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views import generic

from restaurant.models import Cook, Dish, DishType


# @login_required
def index(request):
    """View function for the home page of the site."""

    num_cooks = Cook.objects.count()
    num_dishes = Dish.objects.count()
    num_dish_types = DishType.objects.count()

    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        "num_cooks": num_cooks,
        "num_dishes": num_dishes,
        "num_dish_types": num_dish_types,
        "num_visits": num_visits + 1,
    }

    return render(request, "restaurant/index.html", context=context)


class CookListView(generic.ListView):
    model = Cook
    paginate_by = 2


class CookDetailView(generic.DetailView):
    model = Cook


class DishListView(generic.ListView):
    model = Dish
    paginate_by = 2
    queryset = Dish.objects.all().select_related("dish_type")


class DishDetailView(generic.DetailView):
    model = Dish


class DishTypeListView(generic.ListView):
    model = DishType
    paginate_by = 2
    template_name = "restaurant/dish_type_list.html"
    context_object_name = "dish_type_list"

