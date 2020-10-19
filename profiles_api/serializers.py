from rest_framework import serializers


class HelloSerializer(serializers.Serializer):
    """Serilizers a name fie f field for testing our APIView"""
    name = serializers.CharField(max_length=10)
