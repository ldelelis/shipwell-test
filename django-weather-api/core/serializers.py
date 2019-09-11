from rest_framework import serializers

class TemperatureSerializer(serializers.Serializer):
    latitude = serializers.FloatField(
        min_value=-90,
        max_value=90
    )
    longitude = serializers.FloatField(
        min_value=-180,
        max_value=180
    )
    sources = serializers.ListField(
        min_length=1,
        child=serializers.CharField()
    )
