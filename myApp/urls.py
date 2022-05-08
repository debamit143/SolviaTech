
from django.urls import path
from myApp.views import *

urlpatterns = [
    path('api/dogs',DogList.as_view(),name='doglist'),
    path('api/dogs/<int:dog_id>',DogDetails.as_view(),name='dogDetails'),
    path('api/breeds',BreedList.as_view(),name='breedlist'),
    path('api/breeds/<int:breed_id>',BreedDetails.as_view(),name='breedDetails')
]