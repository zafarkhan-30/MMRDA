from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import Group 
from Auth.models import User ,  occupationalHealthSafety
from .serializers import (LoginSerializer, RegisterSerializer , photographsSerializer , OccupationalHealthSafetySerailzers ,TraningSerializer )
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import generics
from .renderers import ErrorRenderer
from rest_framework.parsers import MultiPartParser



def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

class UserRegister(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    parser_classes = [MultiPartParser]

    def post(self, request):
        try:
            serializer = RegisterSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                try:
                    
                    user = serializer.save()
                    mmrda_group = Group.objects.get(name='mmrda')
                    kfw_group = Group.objects.get(name="kfw")
                    consultant_group = Group.objects.get(name='consultant')
                    contractor_group = Group.objects.get(name='contractor')
                    if user.is_mmrda == True:
                        user.groups.add(mmrda_group)

                    if user.is_kfw == True:
                        user.groups.add(kfw_group)

                    if user.is_consultant == True:
                        user.groups.add(consultant_group)

                    if user.is_contractor == True:
                        user.groups.add(contractor_group)
                except:
                    return Response({'msg': 'Please select any one group'}, status=400)

                return Response({'msg': 'Registration Successfull'}, status=200)
        except:
            return Response({'msg': 'Registration NotSuccessfull'}, status=400)


class LoginView(generics.GenericAPIView):
    serializer_class = [LoginSerializer , RegisterSerializer]
    renderer_classes = [ErrorRenderer]
    parser_classes = [MultiPartParser]

    def post(self, request):
        try:
            serializer = LoginSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            user_data = serializer.validated_data
            user = RegisterSerializer(user_data)
            if serializer is not None:
                token = get_tokens_for_user(serializer.validated_data)
               
                return Response({'Token': token, 'msg': 'Login sucessfull', 'user' : user.data}, status=200)
        except:
            return Response(serializer.errors, status=404)
# "user_group": user_data.groups.values_list("name", flat=True)








class OccupationalHealthSafetyView(generics.ListCreateAPIView):
    queryset = occupationalHealthSafety.objects.all()
    serializer_class = OccupationalHealthSafetySerailzers
    renderer_classes = [ErrorRenderer]
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser]

    def post(self , request):
        try:
            serializer  = OccupationalHealthSafetySerailzers(data = request.data , many = True)
            if serializer.is_valid():
                serializer.save()
                return Response({'msg':'Data save sucessfully'} , status = 200)
        except:
            return Response({'msg' : 'Please Enter Valid data'} , status = 400)


class TraningView(generics.GenericAPIView):

    serializer_class = TraningSerializer
    renderer_classes = [ErrorRenderer]
    # permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser]

    def post(self , request):
        try:
            serializer = TraningSerializer(data = request.data )
            if serializer.is_valid(raise_exception= True):
                serializer.save()
                return Response(serializer.data , status = 200)
        except:
            return Response({'Please Enetr a valid data'} , status =400)
    


class PhotographsView(generics.GenericAPIView):
    serializer_class = photographsSerializer
    renderer_classes = [ErrorRenderer]
    # permission_classes = [IsAuthenticated]
    parser_classes =[MultiPartParser]

    def post(self, request):
        serializer = photographsSerializer(data = request.data )
        # if serializer.is_valid(raise_exception= True):
        if serializer.is_valid(raise_exception = True):
            serializer.save()
            return Response(serializer.data , status = 200)
        else:
            return Response(serializer.errors , status = 400)
        

   