from rest_framework import serializers


class InfoSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name_building = serializers.CharField(max_length=150)
    name_company = serializers.CharField(max_length=150)
    quarters = serializers.IntegerField()