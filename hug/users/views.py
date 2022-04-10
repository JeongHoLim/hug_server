from django.shortcuts import render
from rest_framework.views import APIView
from users.models import Users
from diary.models import Diary
from rest_framework import status
from rest_framework.response import Response
from .serializers import UserSerializer

class UserDetail(APIView):

    def get(self, request, user_id, format=None):
        user = Users.objects.filter(id = user_id)
        if not user:
            return Response({"msg" : "존재하지 않는 유저"},status=status.HTTP_404_NOT_FOUND)
        serializer = UserSerializer(user,many=True)

        return Response(serializer.data)
    
    def put(self,request,user_id,format=None):
        user = Users.objects.filter(id = user_id)
        if not user:
            return Response({"msg" : "존재하지 않는 유저"},status=status.HTTP_404_NOT_FOUND)

        diaries = Diary.objects.filter(user_id = user_id)
        if not diaries :
            return Response(status=status.HTTP_200_OK)
        print(diaries)

        return Response(status=status.HTTP_200_OK)

