from .models import (
    City, PointOfInterest
)
from rest_framework import generics, viewsets
from rest_framework.response import Response
from .serializers import (
    CitySerializer, POISerializer
)

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
        print('city id', city_id)
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

        print(queryset.raw)

        return queryset