from django.urls import path, include
from rest_framework import routers
from .views import (
    CityViewSet, POIList, OnGoingPlanViewset
)
from tourguideapi.views import get_recommendation
from tourguideapi.views import get_plan_review

router = routers.SimpleRouter()
router.register(r'cities', CityViewSet, basename='cities')
router.register(r'on-going-plans', OnGoingPlanViewset, basename='on-going-plans')

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/point-of-interets', POIList.as_view(), name='point-of-interets'),
    path('api/recommendation/', get_recommendation, name="get_recommendation"),
    path('api/plan-review/',
         get_plan_review,
         name = 'get_plan_review'),
]
