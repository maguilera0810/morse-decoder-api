from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from applications.morse.models import CodigoMorse, WordsTable
from .serializers import (
    MorseCodeSerializer,
    TranslateSerializer,
    WordsFrecuencySerializer,
    WordsPagination
)


class MorseCodesView(ListAPIView):
    serializer_class = MorseCodeSerializer

    def get_queryset(self):
        return CodigoMorse.objects.all()


class WordsFrecuencyView(ListAPIView):
    serializer_class = WordsFrecuencySerializer
    pagination_class = WordsPagination

    def get_queryset(self):
        return WordsTable.objects.all()


class Translate2Morse(APIView):
    serializer_class = TranslateSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        code = 400
        res = 'Bad Request'
        if serializer.is_valid():
            text = serializer.data.get('text')
            try:
                WordsTable.update_words(text)
                res = CodigoMorse.translate2Morse(text)
                code = 200
            except Exception as e:
                code = 500
                res = f'DecodeBits2Morse Error: {e}'
        return Response({
            'code': code,
            'response': res
        })


class Translate2Human(APIView):
    serializer_class = TranslateSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        code = 400
        res = 'Bad Request'
        if serializer.is_valid():
            text = serializer.data.get('text')
            try:
                res = CodigoMorse.translate2Human(text)
                WordsTable.update_words(res)
                code = 200
            except Exception as e:
                code = 500
                res = f'DecodeBits2Morse Error: {e}'
        return Response({
            'code': code,
            'response': res
        })


class DecodeBits2Morse(APIView):
    serializer_class = TranslateSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        code = 400
        res = 'Bad Request'
        if serializer.is_valid():
            text = serializer.data.get('text')
            try:
                res = CodigoMorse.decodeBits2Morse(text)
                WordsTable.update_words(CodigoMorse.translate2Human(res))
                code = 200
            except Exception as e:
                code = 500
                res = f'DecodeBits2Morse Error: {e}'
        return Response({
            'code': code,
            'response': res
        })


class DecodeBits2Human(APIView):
    serializer_class = TranslateSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        code = 400
        res = 'Bad Request'
        if serializer.is_valid():
            text = serializer.data.get('text')
            try:
                morse = CodigoMorse.decodeBits2Morse(text)
                res = CodigoMorse.translate2Human(morse)
                WordsTable.update_words(res)
                code = 200
            except Exception as e:
                code = 500
                res = f'DecodeBits2Human Error: {e}'
        return Response({
            'code': code,
            'response': res
        })
