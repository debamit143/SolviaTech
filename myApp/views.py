
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render
from myApp.models import *
from myApp.serializers import *


# Create your views here.

class BreedList(APIView):
    def get(self,request):
        breed_details = Breed.objects.all()
        breed_details_sere = BreedSerializer(breed_details, many=True).data
        return Response({"status": True, "data": breed_details_sere})
    def post(self,request):
        name = str(request.data.get('name'))
        size = str(request.data.get('size'))
        friendliness = int(request.data.get('friendliness'))
        trainability = int(request.data.get('trainability'))
        sheddingamount = int(request.data.get('sheddingamount'))
        exerciseneeds = int(request.data.get('exerciseneeds'))
        
        if (friendliness and trainability and sheddingamount and exerciseneeds) < 1 or (friendliness and trainability and sheddingamount and exerciseneeds) > 5:
            return Response({"status": False, "msg": 'Value must be between 1 to 5'})
        breed_add = Breed(name=name,size=size,friendliness=friendliness,trainability=trainability,sheddingamount=sheddingamount,exerciseneeds=exerciseneeds)
        breed_add.save()
        return Response({"status": True, "msg": 'Breed added successfully'})

class BreedDetails(APIView):
    def get(self,request,breed_id):
        try:
            breed = Breed.objects.get(breed_id=breed_id)
            breed_sere = BreedSerializer(breed).data
            return Response({"status": True, "data": breed_sere})
        except:
            return Response({'status':False,"msg":'Does not exist any Breed with this id'})

        
    def put(self,request,breed_id):
        try:
            name = str(request.data.get('name'))
            size = str(request.data.get('size'))
            friendliness = int(request.data.get('friendliness'))
            trainability = int(request.data.get('trainability'))
            sheddingamount = int(request.data.get('sheddingamount'))
            exerciseneeds = int(request.data.get('exerciseneeds'))
            breed = Breed.objects.get(breed_id=breed_id)
            breed.name = name
            breed.size = size
            breed.friendliness = friendliness
            breed.trainability = trainability
            breed.sheddingamount = sheddingamount
            breed.exerciseneeds = exerciseneeds
            breed.save()
            return Response({"status": True, "data": "breed updated successfully"})
        except:
            return Response({'status':False,"msg":'Does not exist any Breed with this id'})
    def delete(self,request,breed_id):
        try:
            breed = Breed.objects.get(breed_id=breed_id)
            breed.delete()
            return Response({"status": True, "msg": 'breed is deleted'})
        except:
            return Response({'status':False,"msg":'Does not exist any Breed with this id'})

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

class DogDetails(APIView):
    def get(self,request,dog_id):
        try:
            dog = Dog.objects.get(dog_id=dog_id)
            dog_sere = DogSerializer(dog).data
            return Response({"status": True, "data": dog_sere})
        except:
            return Response({'status':False,"msg":'Does not exist any dog with this id'})
        
    def put(self,request,dog_id):
        try:
            name = str(request.data.get('name'))
            age = int(request.data.get('age'))
            gender = str(request.data.get('gender'))
            color = str(request.data.get('color'))
            favoritefood = str(request.data.get('favoritefood'))
            favoritetoy = str(request.data.get('favoritetoy'))
            foreign_breed_id = int(request.data.get('foreign_breed_id'))
            dog = Dog.objects.get(dog_id=dog_id)
            
            try: 
                foreign_breed = Breed.objects.get(breed_id=foreign_breed_id)
                dog.name = name
                dog.age = age
                dog.gender = gender
                dog.color = color
                dog.favoritefood =favoritefood
                dog.favoritetoy = favoritetoy
                dog.foreign_breed_id = foreign_breed_id
                dog.save()
                return Response({"status": True, "msg": 'Breed Updated successfully'})

            except:
                return Response({"status": False, "msg": 'Breed id does not exist'}) 
            
        except:
            return Response({'status':False,"msg":'Does not exist any dog with this id'})
    def delete(self,request,dog_id):
        try:
            dog = Dog.objects.get(dog_id=dog_id)
            dog.delete()
            return Response({"status": True, "msg": 'dog is deleted'})
        except:
            return Response({'status':False,"msg":'Does not exist any dog with this id'})