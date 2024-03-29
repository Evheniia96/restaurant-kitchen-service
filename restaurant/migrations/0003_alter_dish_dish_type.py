# Generated by Django 5.0 on 2024-02-01 20:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("restaurant", "0002_alter_cook_year_of_experience"),
    ]

    operations = [
        migrations.AlterField(
            model_name="dish",
            name="dish_type",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="cooks",
                to="restaurant.dishtype",
            ),
        ),
    ]
