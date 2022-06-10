from django.urls import path, include
from rest_framework import routers
from .views import (
    CityViewSet, POIList
)

router = routers.SimpleRouter()
router.register(r'cities', CityViewSet, basename='cities')

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/point-of-interets', POIList.as_view(), name='point-of-interets')
]
