from myApp.models import *
from rest_framework import serializers





class BreedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Breed
        fields = "__all__"

class DogSerializer(serializers.ModelSerializer):

    foreign_breed = BreedSerializer()
    class Meta:
        model = Dog
        fields = '__all__'
