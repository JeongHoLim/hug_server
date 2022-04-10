from django.urls import path
from . import views

urlpatterns = [
    path('<int:user_id>',views.DiaryList.as_view()),
    path('<int:user_id>/<int:diary_id>',views.DiaryDetail.as_view()),
]