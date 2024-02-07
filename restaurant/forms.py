from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from restaurant.models import Dish, Cook


class DishForm(forms.ModelForm):
    cooks = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )

    class Meta:
        model = Dish
        fields = "__all__"


class CookCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Cook
        fields = UserCreationForm.Meta.fields + (
            "year_of_experience",
            "first_name",
            "last_name",
        )

    def clean_year_of_experience(self):
        return validate_year_of_experience(self.cleaned_data["year_of_experience"])


class CookExperienceUpdateForm(forms.ModelForm):
    class Meta:
        model = Cook
        fields = ["year_of_experience"]

    def clean_year_of_experience(self):
        return validate_year_of_experience(self.cleaned_data["year_of_experience"])


def validate_year_of_experience(
    year_of_experience,
):
    if year_of_experience > 100:
        raise ValidationError("Year of experience should be less than 100")

    return year_of_experience


class DishSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput
        (attrs={"placeholder": "Search by dish"})
    )


class DishTypeSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput
        (attrs={"placeholder": "Search by dish type"})
    )


class CookSearchForm(forms.Form):
    username = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput
        (attrs={"placeholder": "Search by cook"})
    )
