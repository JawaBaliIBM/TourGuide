import logging

from datetime import datetime

from .models import (
    City, PointOfInterest, Plan, PlanItem
)
from rest_framework import generics, viewsets
from rest_framework.response import Response
from .serializers import (
    CitySerializer, POISerializer, PlanSerializer
)

logger = logging.getLogger(__name__)

class CityViewSet(viewsets.ViewSet):
    """
        A simple ViewSet for listing or retrieving cities.
    """
    def list(self, request):
        queryset = City.objects.all()
        serializer = CitySerializer(queryset, many=True)
        return Response(serializer.data)

class POIList(generics.ListAPIView):
    serializer_class = POISerializer

    def get_queryset(self):
        """
        Optionally restricts the returned pois base on category, city, and keyword,
        by filtering against the three query parameter in the URL.
        """
        city_id = self.request.query_params.get('city_id')
        if not city_id is None:
            queryset = City.objects.get(id=int(city_id)).pois.all()
        else:
            queryset = PointOfInterest.objects.all()

        category = self.request.query_params.get('category')
        if not category is None:
            queryset = queryset.filter(category=category)

        keyword = self.request.query_params.get('keyword')
        if not keyword is None:
            queryset = queryset.filter(title__icontains=keyword)

        return queryset

class OnGoingPlanViewset(viewsets.ViewSet):
    def list(self, request):
        year, month, day = self.__today_date()
        try:
            plan = Plan.objects.filter(created_at__year=year,
                created_at__month=month, created_at__day=day)
            serializer = PlanSerializer(
                plan, 
                many=True)
        except Plan.DoesNotExist:
            logger.warning("On going plan does not exist!")
            serializer = PlanSerializer(None, many=True)
        
        return Response(serializer.data)

    def create(self, request):
        data = request.data
        items_data = data.pop('plan_items')
        try:
            plan = Plan.objects.create(**data)
            for item_data in items_data:
                PlanItem.objects.create(plan=plan, **item_data)
        except Exception as e:
            logger.error(e)
            logger.error('Plan insertion failed.')

            return Response({
                'code': 401,
                'isSuccess': False,
                'error': {
                    'message': 'Plan Creation Failed'
                }
            })

        return Response({
            'code': 200,
            'isSuccess': True,
            'error': None
        })

    def __today_date(self):
        today = datetime.today()

        return today.year, today.month, today.day
