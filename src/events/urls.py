from django.urls import path

from . import views

urlpatterns = [
    path("", views.EventListView.as_view()),
    path("<uuid:pk>/", views.EventRetrieveUpdateView.as_view()),
    path("<uuid:pk>/register/", views.EventRegisterView.as_view()),
]
