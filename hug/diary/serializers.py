from diary.models import Diary
from rest_framework import serializers


class DiarySerializer(serializers.ModelSerializer):

    class Meta:
        model = Diary
        exclude = ["id"]
