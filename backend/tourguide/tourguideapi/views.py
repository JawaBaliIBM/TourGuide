import random
from django.views.decorators.csrf import csrf_exempt


from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.request import Request

from tourguideapi.models import PointOfInterest
from tourguideapi.serializers import POISerializer, PlanReviewSerializer
from tourguideapi.models import Plan, PlanItem


# Create your views here.
# @csrf_exempt
@api_view(http_method_names=['POST'])
def get_recommendation(request: Request):
    data = request.data
    print("data:", data)
    starting_point = data["starting_point"]
    destinations = data["destinations"]
    package_name = data["package_name"]
    is_include_ride = data.get("is_include_ride", True)

    destination_ids = [d["id"] for d in destinations]
    pois = PointOfInterest.objects.filter(id__in=destination_ids)
    # Ideally, call grab API for fare on each places
    # But Farefeed API access is not supported???

    
    pois_ser = POISerializer(pois, many=True)
    return Response(pois_ser.data)

@csrf_exempt
@api_view(http_method_names=['POST'])
def create_plan(request: Request):
    data = request.data
    print("data", data, request)
    package_name = data.get("package_name", "My Tour")
    is_include_ride = data.get("is_include_ride", True)
    plan = Plan.objects.create(name=package_name)

    pois = data.get("destinations", [])
    starting_point = data.get("starting_point")
    plan_items = []

    if starting_point and len(pois) > 0:
        poi = PointOfInterest.objects.get(id=pois[0].get('id'))
        
        # Ideally, call grab API for fare on each routes
        # But Farefeed API access is not supported???
        plan_item = PlanItem(
            plan=plan,
            name=f"{starting_point.get('name', 'Home')} to {poi.title}",
            price=random.randint(1, 100) * 1000 if is_include_ride else 0,
            type=PlanItem.PlanItemChoice.ROUTE)
        plan_items.append(plan_item)
    for idx, poi in enumerate(pois):
        poi = PointOfInterest.objects.get(id=poi.get('id'))
        plan_item = PlanItem(
            plan=plan,
            name=poi.title,
            price=poi.price,
            type=PlanItem.PlanItemChoice.POI.value)
        plan_items.append(plan_item)
        if idx < len(pois) - 1:
            # Ideally, call grab API for fare on each places
            # But Farefeed API access is not supported???
            next_poi = PointOfInterest.objects.get(id=pois[idx + 1].get('id'))
            plan_item = PlanItem(
                plan=plan,
                name=f"{poi.title} to {next_poi.title}",
                price=random.randint(1, 100) * 1000 if is_include_ride else 0,
                type=PlanItem.PlanItemChoice.ROUTE.value)
            plan_items.append(plan_item)

    PlanItem.objects.bulk_create(plan_items)

    return Response({
        "status": "OK",
        "message": "Plan is created.",
        "id": plan.id
    })



@csrf_exempt
@api_view(http_method_names=['GET'])
def get_plan_review(request: Request, id: int):
    plan = Plan.objects.filter(id=id).first()
    if plan is None:
        return Response({"error": "Plan not found"}, status=404)
    
    plan_ser = PlanReviewSerializer(plan)
    return Response(plan_ser.data)
