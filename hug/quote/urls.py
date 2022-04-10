from django.urls import path
from . import views

urlpatterns = [
    path('<int:theme_id>',views.QuoteDetail.as_view()),
    path('all/<int:theme_id>',views.QuoteList.as_view()),
]