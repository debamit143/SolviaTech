
from django.urls import path
from myApp.views import *

urlpatterns = [
    path('dog',DogView.as_view(),name='dogview')
]