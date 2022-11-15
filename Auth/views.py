
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import Group
from Auth.models import User , EnvQualityMonitoring , Air , Noise
# traning, Rehabilation, EnvQualityMonitoring, PAP, Air, water, Noise, social_Monitoring , TreeManagment
from Auth.permissions import Allpermission
from .serializers import (LoginSerializer, RegisterSerializer , AirSerializer ,WaterSerializer,NoiseSerializer , photographsSerializer ,EnvQualityMonitoringSerailzer,envMonitoringSerailzer, EnvMonitoring)
# AirSerializer, LabourSiteSerialzer, WaterSerializer,NoiseSerializer, constructionCampSerializer ,
# social_MonitoringSerializer, EnvMonitoringSerailzer, photographsSerializer, TraningSerializer, photographs, 
                        # EnvQualityMonitoringSerailzer, PapSerailzer, rehabilatinSerializer , TreeManagementSerailizer , WasteTreatmentsSerializer , MaterialSourcingSerializer , LabourCampSerializer
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import generics
from rest_framework.views import APIView
from .renderers import ErrorRenderer
from rest_framework.parsers import MultiPartParser
from rest_framework import status

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


class UserRegister(generics.GenericAPIView):
    serializer_class = RegisterSerializer

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
                    if user.is_mmrda:
                        user.groups.add(mmrda_group)

                    elif user.is_kfw:
                        user.groups.add(kfw_group)

                    elif user.is_consultan:
                        user.groups.add(consultant_group)

                    elif user.is_contractor:
                        user.groups.add(contractor_group)
                except:
                    return Response({'msg': 'Please select any one group'}, status=400)

                return Response({'msg': 'Registration Successfull'}, status=200)
        except:
            return Response({'msg': 'Registration NotSuccessfull'}, status=400)


class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        try:
            serializer = LoginSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            user_data = serializer.validated_data
            user = RegisterSerializer(serializer.validated_data)
            if serializer is not None:
                token = get_tokens_for_user(serializer.validated_data)
                return Response({'Token': token, 'msg': 'Login sucessfull', "data": user_data.email,
                                "user_group": user_data.groups.values_list("name", flat=True)}, status=200)
        except:
            return Response({'msg': 'email or password is not valid !!'}, status=404)
















class EnvMonitoringView(generics.GenericAPIView):
    renderer_classes = [ErrorRenderer]
    serializer_class = envMonitoringSerailzer
    
    def post(self, request):
        serializer = envMonitoringSerailzer(data = request.data)
        if serializer.is_valid(raise_exception= True):
            serializer.save()
            return Response(serializer.data , status = 200)
        else:
            return Response({'msg' :'Please enter valid data'} , status = 400 )













class EnvQualityMonitoringView(generics.GenericAPIView):
    def get(self , request):
        # data = EnvMonitoring.objects.filter()
        data = EnvQualityMonitoring.air_set
        print(data , "adafaf")
        serializer = NoiseSerializer(data , many = True)
        return Response(serializer.data , status = 200)







class AirView(generics.GenericAPIView):
    renderer_classes = [ErrorRenderer]
    serializer_class = AirSerializer
    def post(self , request):
        Serializer = AirSerializer(data = request.data)
        if Serializer.is_valid(raise_exception = True):
            Serializer.save()
            return Response(Serializer.data , status= status.HTTP_200_OK)
        else:
            return Response(Serializer.errors , status= status.HTTP_400_BAD_REQUEST)

class WaterView(generics.GenericAPIView):
    renderer_classes = [ErrorRenderer]
    # permission_classes = [IsAuthenticated]
    serializer_class = WaterSerializer

    def post(self , request):
        serializer = WaterSerializer(data = request.data )
        if serializer.is_valid(raise_exception = True):
            serializer.save()
            return Response(serializer.data , status = 200)
        else:
            return Response({'msg' : 'Enter a valid data'} , status = 400)

class NoiseView(generics.GenericAPIView):
    renderer_classes = [ErrorRenderer]
    # permission_classes = [IsAuthenticated]
    serializer_class = NoiseSerializer

    def post (self , request ):
        serializer = NoiseSerializer(data = request.data )
        if serializer.is_valid(raise_exception= True):
            serializer.save()
            return Response (serializer.data , status = 200)
        else:
            return Response({'msg': 'Please Enter Valid data'} ,  status=400 )


# class TreeManagementView(generics.GenericAPIView):
#     serializer_class = TreeManagementSerailizer
#     # queryset = TreeManagment.objects.all()
#     def post(self , request):
#         try:
#             serializer = self.get_serializer(data = request.data)
#             if serializer.is_valid(raise_exception=True):
#                 serializer.save()
#                 return Response(serializer.data , status = status.HTTP_200_OK)
#         except:   
#             return Response({'msg' : 'please enter a valid data'} , status = status.HTTP_400_BAD_REQUEST)


# class WasteTreatmentsView(APIView):
#     def post(self , request):
#         try:
#             serializer = WasteTreatmentsSerializer(data = request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data , status = 200)
#         except:
#             return Response({'msg' : 'Please Eneter a valid data'} ,status = 400)

# class MaterialSourcingView(APIView):
#     def post(self , request):
#         try:
#             serializer = MaterialSourcingSerializer(data = request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data , status = 200)
#         except :
#             return Response ({'msg' : "Please eneter a valid data"} , status = 400)

# class envMonitoringview(generics.ListAPIView):

#     queryset = EnvQualityMonitoring.objects.all()
#     renderer_classes = [ErrorRenderer]
#     serializer_class = EnvQualityMonitoringSerailzer
#     permission_classes = [IsAuthenticated]

#     def post (self , request):
#         try:
#             queryset = self.get_queryset()
#             serializer = EnvQualityMonitoringSerailzer(queryset , many = True)
#             return Response({'msg' : "data save sucessfully"}, status= 200)
#         except:
#             return Response({"msg":"Please Enter Valid data"} , status = 400)
    
    # def get(self , request):
    #     try:
    #         queryset = self.get_queryset()
    #         serializer = EnvQualityMonitoringSerailzer(queryset , many = True)
    #         return Response (serializer.data, status = 200)
    #     except:
    #         return Response({"msg":"Please Enter Valid data"} , status = 400)



# class PapView(generics.GenericAPIView):
#     renderer_classes = [ErrorRenderer]
#     serializer_class = PapSerailzer
#     permission_classes = [IsAuthenticated]
#     parser_classes= [MultiPartParser]

#     def post(self , request):
#         try:
#             serializer = PapSerailzer(data = request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response ({'msg' : "data save sucessfully"} , status = 200)
#             else:
#                 return Response(serializer.errors , status = 400)
#         except:
#             return Response({"msg":"Please Enter Valid data"} , status = 400)


# class RehabilationView(generics.ListAPIView):
#     queryset = Rehabilation.objects.all()
#     renderer_classes = [ErrorRenderer]
#     serializer_class = rehabilatinSerializer
#     permission_classes = [IsAuthenticated]
#     parser_classes = [MultiPartParser]



# class LabourCampView(APIView):
#     def post(self , request):
#         try:
#             serializer = LabourCampSerializer(data = request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data , status = 200)
#         except:
#             return Response({'msg': 'Please Enter a valid data'} , status = 400)


# class constructionCampView(APIView):
#     def post(self , request):
#         try:
#             serializer = constructionCampSerializer(data = request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data , status = 200)
#         except:
#             return Response({"msg": "Please Enter a valid data"} , status =400)

# class LabourSiteView(APIView):
#     def post(self , request):
#         try:
#             serializer = LabourSiteSerialzer(data = request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data , status = 200)
#         except:
#             return Response({"msg": "Please Enter a valid data"} , status = 400)



# class SocialMonitorView(generics.ListAPIView):
#     queryset = Rehabilation.objects.all()
#     renderer_classes = [ErrorRenderer]
#     serializer_class = rehabilatinSerializer
#     permission_classes = [IsAuthenticated]



# # class OccupationalHealthSafetyView(generics.ListCreateAPIView):
# #     queryset = occupationalHealthSafety.objects.all()
# #     serializer_class = OccupationalHealthSafetySerailzers
# #     renderer_classes = [ErrorRenderer]
# #     permission_classes = [IsAuthenticated]
# #     parser_classes = [MultiPartParser]

# #     def post(self , request):
# #         try:
# #             serializer  = OccupationalHealthSafetySerailzers(data = request.data , many = True)
# #             if serializer.is_valid():
# #                 serializer.save()
# #                 return Response({'msg':'Data save sucessfully'} , status = 200)
# #         except:
# #             return Response({'msg' : 'Please Enter Valid data'} , status = 400)


# class TraningView(generics.GenericAPIView):
#     # queryset = traning.objects.all()
#     serializer_class = TraningSerializer
#     # renderer_classes = [ErrorRenderer]
#     # permission_classes = [IsAuthenticated]
#     # parser_classes = [MultiPartParser]

#     def post(self , request):
#         serializer = self.get_serializer(data = request.data )
#         if serializer.is_valid(raise_exception= True):
#             serializer.save()
#             return Response(serializer.data , status = 200)
#         else:
#             return Response(serializer.errors , status =400)
#         # except:
#         #     return Response (serializer.data, status = 400)


class PhotographsView(generics.GenericAPIView):
#     # queryset = photographs.objects.all()
    serializer_class = photographsSerializer
#     # renderer_classes = [ErrorRenderer]
#     # permission_classes = [IsAuthenticated]
#     # parser_classes =[MultiPartParser]


    def post(self, request):
        serializer = photographsSerializer(data = request.data )
        # if serializer.is_valid(raise_exception= True):
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status = 200)
        else:
            return Response(serializer.errors , status = 400)
        

   