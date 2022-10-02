from django.urls import path
from .views import *

app_name = 'api'

urlpatterns = [
    path("", TouristDestination_APIView.as_view()),
    path("<int:pk>/", TouristDestination_APIView_Detail.as_view()),
]