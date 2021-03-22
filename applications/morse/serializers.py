#
from rest_framework import serializers, pagination
from applications.morse.models import (
    CodigoMorse,
    WordsTable
)


class MorseCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CodigoMorse
        fields = '__all__'


class TranslateSerializer(serializers.Serializer):
    token = serializers.CharField(required=True)
    text = serializers.CharField(required=False)


class WordsFrecuencySerializer(serializers.ModelSerializer):
    class Meta:
        model = WordsTable
        fields = '__all__'


class WordsPagination(pagination.PageNumberPagination):
    page_size = 1
    max_page_size = 100
