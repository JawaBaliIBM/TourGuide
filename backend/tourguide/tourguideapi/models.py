from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

# class User(models.Model):
#     id = models.CharField(max_length=64)
#     email = models.CharField(max_length=64)
#     phone_number = models.CharField(max_length=16)
#     name = models.CharField(max_length=64)
#     access_token = models.CharField()


class Category(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=128)
    description = models.TextField()

class PointOfInterest(models.Model):
    # class Category(models.TextChoices):
    #     NATURE = "NA", _("Nature")
    #     SHOPPING = "SH", _("Shopping")
    #     LEISURE = "LE", _("Leisure")
    #     CULINARY = "CU", _("Culinary")
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=128)
    # category = models.CharField(max_length=2, choices=Category.choices)
    category = models.ManyToManyField(Category)
    photo = models.CharField(max_length=256)
    description = models.TextField()
    address = models.TextField()
    price = models.PositiveIntegerField(default=0)
    open_time = models.CharField(max_length=64)
    avg_time_spent = models.PositiveIntegerField(default=60)
    lat = models.FloatField()
    long = models.FloatField()


class Plan(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=128)
    # owner = models.ForeignKey(
    #     "User",
    #     on_delete=models.CASCADE,
    #     related_name="plans",
    #     related_query_name="plan",
    # )

class PlanItem(models.Model):
    class PlanItemChoice(models.TextChoices):
        POI = "POI", _("Point of Interest")
        ROUTE = "ROU", _("Route")

    id = models.BigAutoField(primary_key=True)
    plan = models.ForeignKey(
        "Plan",
        on_delete=models.CASCADE,
        related_name="items",
        related_query_name="item"
    )
    name = models.CharField(max_length=128)
    price = models.PositiveIntegerField(default=0)
    type = models.CharField(max_length=3, choices=PlanItemChoice.choices)
