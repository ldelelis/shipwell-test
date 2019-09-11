import requests

from django.http import JsonResponse
from django.shortcuts import render
from django.utils.translation import gettext_lazy as _
from rest_framework.views import APIView
from rest_framework.exceptions import ValidationError

from .services import AverageTemperatureService
from .serializers import TemperatureSerializer

# Create your views here.

class AverageTemperatureView(APIView):
    VALID_SOURCES = ('noaa', 'accuweather', 'weatherdotcom')

    def get(self, request, lat, lon):
        """Receives parameter to feed an average temperature service with
            :lat: float latitude to search for
            :lon: float longitude to search for

            :sources: string comma-separated list of sources

            Returns:
            :fahrenheit: float average calculated temperature in fahrenheit
            :celsius: int average calculated temperature, converted to celsius
        """
        sources = request.GET.get('sources', '').split(',')

        serializer = TemperatureSerializer(data={
            "latitude":lat,
            "longitude":lon,
            "sources":sources
        })
        serializer.is_valid(raise_exception=True)

        if len([src for src in sources if src in self.VALID_SOURCES]) != len(sources):
            raise ValidationError({'detail': _('Al menos uno de los filtros provistos es inválido')})

        return JsonResponse(AverageTemperatureService(**serializer.data).get_average_temperatures())

