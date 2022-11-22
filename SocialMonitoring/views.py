from django.shortcuts import render
from .serializers import (PapSerailzer , papviewserialzer , rehabilatinSerializer , Compensationserializer ,
ConstructionSiteDetailsViewSerializer, constructionSiteSerializer , LabourCampDetailSerializer ,
LabourCampDetailViewSerializer) 
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from .renderers import ErrorRenderer
from django.contrib.gis.geos import Point,GEOSGeometry
# Create your views here.


class PapView(generics.GenericAPIView):
    renderer_classes = [ErrorRenderer]
    serializer_class = PapSerailzer
    permission_classes = [IsAuthenticated]
    parser_classes= [MultiPartParser]

    def post(self , request):
        try:
            lat=float(request.data['latitude'])
            long=float(request.data['longitude'])
            location=Point(long,lat,srid=4326)
            serializer = PapSerailzer(data = request.data)
            if serializer.is_valid(raise_exception= True):
                pap = serializer.save(location = location)
                data  = papviewserialzer(pap).data
                return Response (data , status = 200)
        except:
            return Response({"msg":"Please Enter Valid data"} , status = 400)


class RehabilationView(generics.GenericAPIView):
    renderer_classes = [ErrorRenderer]
    serializer_class = rehabilatinSerializer
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser]

    def post(self , request):
        try:
            serializer = rehabilatinSerializer(data = request.data)
            if serializer.is_valid(raise_exception= True):
                serializer.save()
            return Response(serializer.data , status = 200)
        except:
            return Response({'msg' :'Please Enter a valid data'} , status = 400)


class CompensationView(generics.GenericAPIView):
    renderer_classes = [ErrorRenderer]
    parser_classes = [MultiPartParser]
    permission_classes = [IsAuthenticated]
    serializer_class = Compensationserializer

    def post(self , request):
        try:
            serializer = Compensationserializer(data = request.data)
            if serializer.is_valid(raise_exception= True):
                serializer.save()
                return Response(serializer.data , status = 200)
        except:
            return Response({'msg' :'Please enter a valid data'} , status =400)

        

class constructionSiteView(generics.GenericAPIView):
    renderer_classes = [ErrorRenderer]
    parser_classes = [MultiPartParser]
    permission_classes = [IsAuthenticated]
    serializer_class = constructionSiteSerializer

    def post(self , request):
        try:
            lat=float(request.data['latitude'])
            long=float(request.data['longitude'])
            location=Point(long,lat,srid=4326)
            serialzier = constructionSiteSerializer(data= request.data)
            if serialzier.is_valid(raise_exception= True):
                construction = serialzier.save(location = location)
                data = ConstructionSiteDetailsViewSerializer(construction).data
                return Response(data , status = 200)
        except:
            return Response({'msg' : 'Please Enter a valid data' } , status = 400)



class LabourCampDetailsView(generics.GenericAPIView):
    renderer_classes = [ErrorRenderer]
    parser_classes = [MultiPartParser]
    permission_classes = [IsAuthenticated]
    serializer_class =  LabourCampDetailSerializer

    def post(self , request):
        try:
            lat=float(request.data['latitude'])
            long=float(request.data['longitude'])
            location=Point(long,lat,srid=4326)
            serializer = LabourCampDetailSerializer(data = request.data)
            if serializer.is_valid(raise_exception= True):
                LabourCampDetails= serializer.save(location = location)
                data = LabourCampDetailViewSerializer(LabourCampDetails).data 
                return Response(data , status = 200)
        except:
            return Response({"msg": "Please Enter a valid data"} , status = 400)



