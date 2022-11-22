from tkinter.ttk import Style
from rest_framework import serializers
from .models import (User  , photographs , occupationalHealthSafety ,  traning )
from django.contrib.auth import authenticate
from rest_framework_gis.serializers import GeoFeatureModelSerializer


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(style = {'input_type':'password'},write_only = True)
    class Meta:
        model = User
        fields = ('email', 'password','is_mmrda' , 'is_kfw' , 'is_contractor' , 'is_consultant')
        
    

    def create(self,validated_data):
        return User.objects.create_user(**validated_data)


class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255)
    class Meta:
        model = User
        fields = ("email", "password")

        extra_kwargs ={'password':{'write_only':True}}


    def validate(self,data):
       return authenticate(**data)
       





class OccupationalHealthSafetySerailzers(serializers.ModelSerializer):
    class Meta:
        model = occupationalHealthSafety
        fields = "__all__" 




class TraningSerializer(serializers.ModelSerializer):
    class Meta:
        model = traning
        fields = '__all__'



class photographsSerializer(serializers.ModelSerializer):
    class Meta:
        model = photographs
        fields = '__all__'
        


        

