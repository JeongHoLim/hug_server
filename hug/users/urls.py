from django.urls import path
from . import views

urlpatterns = [
    # path("signin/",views.signIn.as_view()),
    # path("signout/",views.signOut.as_view()),
    # path("signUp/",views.signUp.as_view()),
    path("<int:user_id>",views.UserDetail.as_view()),
]