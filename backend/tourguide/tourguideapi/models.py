from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

# class User(models.Model):
#     id = models.CharField(max_length=64)
#     email = models.CharField(max_length=64)
#     phone_number = models.CharField(max_length=16)
#     name = models.CharField(max_length=64)
#     access_token = models.CharField()


# class Category(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     name = models.CharField(max_length=128)
#     description = models.TextField()

class PointOfInterest(models.Model):
    class Category(models.TextChoices):
        NATURE = "NA", _("Nature")
        WELLNESS = "WE", _("Wellness")
        LANDMARK = "LA", _("Landmark")
        CULINARY = "CU", _("Culinary")
        MUSEUMS = "MG", _("Museums & Galleries")
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=128)
    category = models.CharField(max_length=2, choices=Category.choices)
    photo = models.CharField(max_length=256)
    description = models.TextField()
    address = models.TextField()
    price = models.PositiveIntegerField(default=0)
    open_time = models.CharField(max_length=64)
    avg_time_spent = models.PositiveIntegerField(default=60)
    lat = models.FloatField()
    long = models.FloatField()
    city = models.ForeignKey(
        "City",
        on_delete=models.CASCADE,
        related_name="pois",
        related_query_name="poi"
    )

class Plan(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)
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

class City(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=128)
