from rest_framework import serializers

from tourguideapi.models import PointOfInterest
from tourguideapi.models import PlanItem
from tourguideapi.models import Plan

class POISerializer(serializers.ModelSerializer):
    class Meta:
        model = PointOfInterest
        depth = 1
        fields = [
            'id', 'title', 'category', 'photo', 'description', 'address',
            'price', 'avg_time_spent'
            ]


class PlanItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlanItem
        # fields = '__all__'
        exclude = ['plan']


class PlanSerializer(serializers.ModelSerializer):
    items = serializers.SerializerMethodField('get_items')

    def get_items(self, obj):
        # Make sure the items returned are sorted by order of trip,
        # in this case, by order or object insertion/creation
        return PlanItemSerializer(obj.items.order_by('id'), many=True, read_only=True).data

    class Meta:
        model = Plan
        fields = '__all__'


class PlanReviewSerializer(PlanSerializer):
    total = serializers.SerializerMethodField('get_total')

    def get_total(self, obj):
        total = 0
        for plan_item in obj.items.all():
            total += plan_item.price
        return total