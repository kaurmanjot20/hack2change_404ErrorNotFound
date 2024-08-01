from rest_framework import serializers

class PredictionSerializer(serializers.Serializer):
    State_Name = serializers.CharField()
    Crop_Type = serializers.CharField()
    Crop = serializers.CharField()
    N = serializers.FloatField()
    P = serializers.FloatField()
    K = serializers.FloatField()
    pH = serializers.FloatField()
    rainfall = serializers.FloatField()
    temperature = serializers.FloatField()
    Area_in_hectares = serializers.FloatField()