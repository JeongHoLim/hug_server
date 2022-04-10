from django.shortcuts import render
from rest_framework.views import APIView
from quote.models import Quote
from .serializers import QuoteSerializer
from rest_framework import status
from rest_framework.response import Response
import random
# Create your views here.

class QuoteDetail(APIView):

    def get(self, request, theme_id, format=None):
        quotes = Quote.objects.filter(theme_id = theme_id)
        if not quotes:
            return Response({"msg" : "데이터 없음"},status=status.HTTP_404_NOT_FOUND)
        serializer = QuoteSerializer(quotes[random.randint(0,len(quotes)-1)])

        return Response(serializer.data)
    

class QuoteList(APIView):

    def get(self,request,theme_id,format=None):
        quotes = Quote.objects.filter(theme_id = theme_id)
        if not quotes:
            return Response({"msg" : "데이터 없음"},status=status.HTTP_404_NOT_FOUND)

        serializer = QuoteSerializer(quotes,many=True)

        return Response(serializer.data)