from django.urls import path, include
from rest_framework import routers
from .views import (
    CityViewSet, POIList, OnGoingPlanViewset
)

router = routers.SimpleRouter()
router.register(r'cities', CityViewSet, basename='cities')
router.register(r'on-going-plans', OnGoingPlanViewset, basename='on-going-plans')

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/point-of-interets', POIList.as_view(), name='point-of-interets')
]
