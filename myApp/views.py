
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render
from myApp.models import *
from myApp.serializers import *

# Create your views here.


class DogList(APIView):
    def get(self, request):
        dog_details = Dog.objects.all()
        dog_details_sere = DogSerializer(dog_details, many=True).data
        return Response({"status": True, "data": dog_details_sere})

    def post(self, request):
        name = str(request.data.get('name'))
        age = int(request.data.get('age'))
        gender = str(request.data.get('gender'))
        color = str(request.data.get('color'))
        favoritefood = str(request.data.get('favoritefood'))
        favoritetoy = str(request.data.get('favoritetoy'))
        foreign_breed_id = int(request.data.get('foreign_breed_id'))

        try:
            dog_add = Dog(name=name, age=age, gender=gender, color=color, favoritefood=favoritefood,
                        favoritetoy=favoritetoy)
            dog_add.foreign_breed_id = foreign_breed_id
            dog_add.save()
            return Response({"status": True, "msg": 'Dog added successfully'})

        except:
            return Response({"status": False, "msg": 'Something Went Wrong'})
