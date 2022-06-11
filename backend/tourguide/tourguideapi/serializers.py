from .models import (
    City, PointOfInterest, Plan, PlanItem
)
from rest_framework import serializers

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['id', 'name']

class POISerializer(serializers.ModelSerializer):
    class Meta:
        model = PointOfInterest
        fields = ['id', 'title', 'photo', 'category', 'description', 
            'address', 'price', 'open_time', 'avg_time_spent']

class PlanItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlanItem
        fields = ['name', 'price', 'type', 'seq', 'ticket_url']

class PlanSerializer(serializers.ModelSerializer):
    plan_items = serializers.SerializerMethodField()

    class Meta:
        model = Plan
        fields = ['name', 'plan_items']

    def get_plan_items(self, obj):
        plan_items = PlanItem.objects.filter(plan=obj)
        return PlanItemSerializer(plan_items, many=True).data

