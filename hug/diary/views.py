from django.shortcuts import render
from diary.models import Diary
from rest_framework.views import APIView
from .serializers import DiarySerializer
from rest_framework import status
from rest_framework.response import Response


class DiaryList(APIView):

    def get(self,request,user_id,format=None):
        diaries = Diary.objects.filter(user_id = user_id)
        if not diaries:
            return Response({"msg" : "데이터 없음"},status=status.HTTP_404_NOT_FOUND)

        serializer = DiarySerializer(diaries,many=True)

        return Response(serializer.data)

class DiaryDetail(APIView):
    def delete(self, request, user_id, diary_id,format=None):
        diary = Diary.objects.filter(user_id=user_id,id = diary_id)
        if not diary:
            return Response({"msg" : "데이터 없음"},status=status.HTTP_404_NOT_FOUND)
        diary.delete()
        return Response(status=status.HTTP_200_OK)