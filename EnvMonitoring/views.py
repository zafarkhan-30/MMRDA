
from .serializer import ( AirSerializer ,WaterSerializer,NoiseSerializer , TreeManagmentviewserializer,
TreeManagementSerailizer,EnvQualityMonitoringSerializer,EnvQualityMonitoringSerailzer, Noiseviewserializer,
envMonitoringSerailzer, EnvMonitoring , WasteTreatmentsSerializer , MaterialSourcingSerializer ,AirViewSerializer,
waterviewserializer , wastetreatmentsViewserializer , MaterialSourcingViewserializer)
from rest_framework.response import Response
from .models import Air
from rest_framework import generics
from .renderers import ErrorRenderer
from rest_framework.parsers import MultiPartParser
from rest_framework import status
from django.contrib.gis.geos import Point,GEOSGeometry
import json
from rest_framework.permissions import IsAuthenticated

class EnvMonitoringView(generics.GenericAPIView):
    renderer_classes = [ErrorRenderer]
    serializer_class = envMonitoringSerailzer
    parser_classes = [MultiPartParser]
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        serializer = envMonitoringSerailzer(data = request.data)
        if serializer.is_valid(raise_exception= True):
            serializer.save()
            return Response(serializer.data , status = 200)
        else:
            return Response({'msg' :'Please enter valid data'} , status = 400 )

class AirView(generics.GenericAPIView):
    renderer_classes = [ErrorRenderer]
    serializer_class = AirSerializer
    parser_classes = [MultiPartParser]
    permission_classes = [IsAuthenticated]

    def post(self , request):
        lat=float(request.data['latitude'])
        long=float(request.data['longitude'])
        location=Point(long,lat,srid=4326)
        Serializer = AirSerializer(data = request.data)
        if Serializer.is_valid(raise_exception = True):
            air=Serializer.save(location=location)
            data=AirViewSerializer(air).data
            return Response(data, status= status.HTTP_200_OK)
        else:
            return Response(Serializer.errors , status= status.HTTP_400_BAD_REQUEST)

class WaterView(generics.GenericAPIView):
    renderer_classes = [ErrorRenderer]
    serializer_class = WaterSerializer
    parser_classes = [MultiPartParser]
    permission_classes = [IsAuthenticated]

    def post(self , request):
        lat=float(request.data['latitude'])
        long=float(request.data['longitude'])
        location=Point(long,lat,srid=4326)
        serializer = WaterSerializer(data = request.data )
        if serializer.is_valid(raise_exception = True):
            water_data =serializer.save(location=location)
            data = waterviewserializer(water_data).data

            return Response(data , status = 200)
        else:
            return Response({'msg' : 'Enter a valid data'} , status = 400)

class NoiseView(generics.GenericAPIView):
    renderer_classes = [ErrorRenderer]
    permission_classes = [IsAuthenticated]
    serializer_class = NoiseSerializer
    parser_classes = [MultiPartParser]

    def post (self , request ):
        try:
            lat=float(request.data['latitude'])
            long=float(request.data['longitude'])
            location=Point(long,lat,srid=4326)
            serializer = NoiseSerializer(data = request.data )
            if serializer.is_valid(raise_exception= True):
                Noise  = serializer.save(location = location)
                data = Noiseviewserializer(Noise).data

                return Response (data , status = 200)
        except:
            return Response({'msg': 'Please Enter Valid data'} ,  status=400 )

class envMonitoringView(generics.GenericAPIView):
    serializer_class = EnvQualityMonitoringSerailzer

    def get(self , request):
        # env = EnvQualityMonitoring.objects.prefetch_related('airs').get(id = 2)
        # data = env.airs.all()
        # print(data)      
        # serializer_context = {
        #     'request': request,}
        env = Air.objects.all()

        serialzier = AirSerializer(env , many = True)
        return Response (serialzier.data , status = status.HTTP_200_OK)

class TreeManagementView(generics.GenericAPIView):
    serializer_class = TreeManagementSerailizer
    renderer_classes = [ErrorRenderer]
    parser_classes = [MultiPartParser]
    permission_classes = [IsAuthenticated]

    def post(self , request):
        try:
            lat=float(request.data['latitude'])
            long=float(request.data['longitude'])
            location=Point(long,lat,srid=4326)
            serializer = TreeManagementSerailizer(data = request.data)
            if serializer.is_valid(raise_exception=True):
                tree = serializer.save(location = location)
                data = TreeManagmentviewserializer(tree).data 
                return Response(data , status = status.HTTP_200_OK)
        except: 
            return Response(serializer.errors , status = status.HTTP_400_BAD_REQUEST)

class WasteTreatmentsView(generics.GenericAPIView):
    serializer_class = WasteTreatmentsSerializer
    renderer_classes = [ErrorRenderer]
    parser_classes = [MultiPartParser]
    permission_classes = [IsAuthenticated]

    def post(self , request):
        try:
            lat=float(request.data['latitude'])
            long=float(request.data['longitude'])
            location=Point(long,lat,srid=4326)
            serializer = WasteTreatmentsSerializer(data = request.data)
            if serializer.is_valid(raise_exception= True):
                waste = serializer.save(location =location)
                data = wastetreatmentsViewserializer(waste ).data
                return Response(data , status = 200)
        except:
            return Response({'msg' : 'Please Eneter a valid data'} ,status = 400)

class MaterialSourcingView(generics.GenericAPIView):
    serializer_class = MaterialSourcingSerializer
    renderer_classes = [ErrorRenderer]
    parser_classes = [MultiPartParser]
    permission_classes = [IsAuthenticated]


    def post(self , request):
        try:
            lat=float(request.data['latitude'])
            long=float(request.data['longitude'])
            location=Point(long,lat,srid=4326)
            serializer = MaterialSourcingSerializer(data = request.data)
            if serializer.is_valid(raise_exception= True):
                material = serializer.save(location=location)
                data = MaterialSourcingViewserializer(material).data 
                return Response(data , status = status.HTTP_200_OK)
        except:
            return Response ({'msg' : "Please eneter a valid data"} , status = 400)
