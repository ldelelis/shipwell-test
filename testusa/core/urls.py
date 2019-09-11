from django.urls import path

from .views import AverageTemperatureView

urlpatterns = [
        path(
            'average-temperature/<str:lat>/<str:lon>/',
            AverageTemperatureView.as_view(),
            name='average-temperature'
        ),
]
