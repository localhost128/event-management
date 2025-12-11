from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    path("", views.EventListView.as_view()),
    path("<uuid:pk>/", views.EventRetrieveUpdateView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
