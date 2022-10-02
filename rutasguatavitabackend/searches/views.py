from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import TouristDestinationSerializers
from .models import TouristDestination
from rest_framework import status
from django.http import Http404


class TouristDestination_APIView(APIView):


    def get(self, request, format=None, *args, **kwargs):
        tourist_destination = TouristDestination.objects.all()
        serializer = TouristDestinationSerializers(tourist_destination, many=True)
        return Response(serializer.data)


class TouristDestination_APIView_Detail(APIView):

    def get_object(self, pk):
        try:
            return TouristDestination.objects.get(pk=pk)
        except TouristDestination.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        tourist_destination = self.get_object(pk)
        serializer = TouristDestinationSerializers(tourist_destination)  
        return Response(serializer.data)



