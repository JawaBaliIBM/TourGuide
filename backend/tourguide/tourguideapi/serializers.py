from .models import (
    City, PointOfInterest
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
            