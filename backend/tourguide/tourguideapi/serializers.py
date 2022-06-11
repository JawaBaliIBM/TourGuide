from rest_framework import serializers

from tourguideapi.models import PointOfInterest
from tourguideapi.models import PlanItem
from tourguideapi.models import Plan
from .models import (
    City, PointOfInterest
)

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['id', 'name']

class POISerializer(serializers.ModelSerializer):
    class Meta:
        model = PointOfInterest
        depth = 1
        fields = ['id', 'title', 'photo', 'category', 'description', 
            'address', 'price', 'open_time', 'avg_time_spent']


class PlanItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlanItem
        # fields = '__all__'
        exclude = ['id', 'plan']


class PlanSerializer(serializers.ModelSerializer):
    items = serializers.SerializerMethodField('get_items')

    def get_items(self, obj):
        # Make sure the items returned are sorted by order of trip,
        # in this case, by order or object insertion/creation
        # TODO: Order by seq
        # return PlanItemSerializer(sorted(self.context.get("items", []), key=seq), many=True, read_only=True).data
        return PlanItemSerializer(self.context.get("items", []), many=True, read_only=True).data

    class Meta:
        model = Plan
        # fields = '__all__'
        exclude = ['id']


class PlanReviewSerializer(PlanSerializer):
    total = serializers.SerializerMethodField('get_total')

    def get_total(self, obj):
        total = 0
        plan_items = self.context.get("items", [])
        for plan_item in plan_items:
            total += plan_item.price
        return total
   
