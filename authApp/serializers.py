from rest_framework import serializers


class TokenSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=225)
    password = serializers.CharField(max_length=255)
    client_id = serializers.CharField(max_length=225)
    grant_type = serializers.CharField(max_length=255)
