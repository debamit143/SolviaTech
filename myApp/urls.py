
from django.urls import path
from myApp.views import *

urlpatterns = [
    path('api/dogs',DogList.as_view(),name='dogview')
]