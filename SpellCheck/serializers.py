from rest_framework import serializers


class SpellCheckSerializer(serializers.Serializer):
    word = serializers.CharField(max_length=100)