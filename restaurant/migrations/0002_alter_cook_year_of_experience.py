# Generated by Django 5.0.1 on 2024-01-31 13:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("restaurant", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cook",
            name="year_of_experience",
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
