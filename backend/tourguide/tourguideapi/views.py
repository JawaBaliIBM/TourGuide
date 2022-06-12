import random, time
from django.views.decorators.csrf import csrf_exempt


from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.request import Request

from tourguideapi.models import (
    City, PointOfInterest
)
from tourguideapi.serializers import (
    CitySerializer, POISerializer, PlanSerializer
)

import logging

from datetime import datetime

logger = logging.getLogger(__name__)



from tourguideapi.models import PointOfInterest
from tourguideapi.serializers import PlanReviewSerializer
from tourguideapi.models import Plan
from tourguideapi.models import PlanItem


# Create your views here.
# @csrf_exempt
@api_view(http_method_names=['POST'])
def get_recommendation(request: Request):
    data = request.data
    starting_point = data["starting_point"]
    destinations = data["destinations"]
    package_name = data["package_name"]
    is_include_ride = data.get("is_include_ride", True)

    destination_ids = [d["id"] for d in destinations]
    pois = PointOfInterest.objects.filter(id__in=destination_ids).all()
    starting_point = PointOfInterest.objects.get(id=starting_point["id"])
    # Ideally, call grab API for fare on each places
    # But Farefeed API access is not supported???
    # Now just sort it randomly
    pois = list(pois)
    random.shuffle(list(pois))
    # Put starting point at the front
    pois.insert(0, pois.pop(pois.index(starting_point)))
    
    pois_ser = POISerializer(pois, many=True)
    return Response(pois_ser.data)


@csrf_exempt
@api_view(http_method_names=['POST'])
def get_plan_review(request: Request):
    # plan = Plan.objects.filter(id=id).first()
    # if plan is None:
    #     return Response({"error": "Plan not found"}, status=404)
    data = request.data
    package_name = data.get("package_name", "My Tour")
    is_include_ride = data.get("is_include_ride", True)
    plan = Plan(name=package_name)

    pois = data.get("destinations", [])
    plan_items = []

    for idx, poi in enumerate(pois):
        poi = PointOfInterest.objects.get(id=poi.get('id'))
        plan_item = PlanItem(
            plan=plan,
            name=poi.title,
            price=poi.price,
            type=PlanItem.PlanItemChoice.POI.value,
            seq=2 * idx + 1)
        plan_items.append(plan_item)
        if idx < len(pois) - 1 and is_include_ride:
            # Ideally, call grab API for fare on each places
            # But Farefeed API access is not supported???
            next_poi = PointOfInterest.objects.get(id=pois[idx + 1].get('id'))
            plan_item = PlanItem(
                plan=plan,
                name=f"{poi.title} to {next_poi.title}",
                price=random.randint(1, 100) * 1000,
                type=PlanItem.PlanItemChoice.ROUTE.value,
                seq=2 * (idx + 1))
            plan_items.append(plan_item)

    plan_ser = PlanReviewSerializer(plan, context={'items': plan_items})
    return Response(plan_ser.data)


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
            time.sleep(1)
            plan = Plan.objects.filter(created_at__year=year,
                created_at__month=month, created_at__day=day).latest('id')
            serializer = PlanSerializer(
                plan)
        except Plan.DoesNotExist:
            logger.warning("On going plan does not exist!")
            serializer = PlanSerializer(None, many=False)
        
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
