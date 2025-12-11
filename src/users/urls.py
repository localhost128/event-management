from django.urls import path

from . import views

urlpatterns = [
    path("", views.UserRetriveView.as_view()),
    path("register/", views.UserCreateView.as_view()),
]
