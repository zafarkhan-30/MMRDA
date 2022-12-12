from .serializers import (PapSerailzer, papviewserialzer, rehabilatinSerializer, Compensationserializer, PapUpdateSerialzier,
                          ConstructionSiteDetailsViewSerializer, constructionSiteSerializer, LabourCampDetailSerializer, LabourCampDetailViewSerializer)
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from .renderers import ErrorRenderer
from django.contrib.gis.geos import Point, GEOSGeometry
from .models import LabourCampDetails, Compensation , PAP , Rehabilation , ConstructionSiteDetails
from .paginations import LimitsetPagination


class PapView(generics.GenericAPIView):
    renderer_classes = [ErrorRenderer]
    serializer_class = PapSerailzer
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser]

    def post(self, request):
    
        lat = float(request.data['latitude'])
        long = float(request.data['longitude'])
        location = Point(long, lat, srid=4326)
        serializer = PapSerailzer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            pap = serializer.save(location=location)
            data = papviewserialzer(pap).data
            return Response(data, status=200)
        else:
            return Response({"msg": serializer.errors}, status=400)

            
class papupdateView(generics.UpdateAPIView):
    serializer_class = PapUpdateSerialzier
    renderer_classes = [ErrorRenderer]
    parser_classes = [MultiPartParser]
    queryset = PAP.objects.all()

    def update(self, request , id ,  **kwargs):
        instance = PAP.objects.get(id=id)
        serializer = PapUpdateSerialzier(instance , data=request.data , partial = True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        else:
            return Response({"msg": "Please Enter a valid data"})

class PapListView(generics.ListAPIView):
    serializer_class = papviewserialzer 
    permission_classes = [IsAuthenticated]
    queryset = PAP.objects.all()

class RehabilationView(generics.GenericAPIView):
    renderer_classes = [ErrorRenderer]
    serializer_class = rehabilatinSerializer
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser]

    def post(self, request):
        try:
            serializer = rehabilatinSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
            return Response(serializer.data, status=200)
        except:
            return Response({'msg': 'Please Enter a valid data'}, status=400)

            
class RehabilationUpdateView(generics.UpdateAPIView):
    serializer_class = rehabilatinSerializer
    renderer_classes = [ErrorRenderer]
    parser_classes = [MultiPartParser]
    queryset = Rehabilation

    def update(self , request , id ):
        instance = Rehabilation.objects.get(id =id)
        serializer = rehabilatinSerializer(instance , data=request.data , partial = True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data , status = 200)
        else:
            return Response(serializer.data)

class RehabilationListView(generics.ListAPIView):
    serializer_class = rehabilatinSerializer
    permission_classes = [IsAuthenticated]
    queryset = Rehabilation.objects.all()



class CompensationView(generics.GenericAPIView):
    renderer_classes = [ErrorRenderer]
    parser_classes = [MultiPartParser]
    permission_classes = [IsAuthenticated]
    serializer_class = Compensationserializer

    def post(self, request):
  
        serializer = Compensationserializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=200)
        else:
            return Response({'msg': serializer.errors}, status=400)

class CompensationUpdateView(generics.UpdateAPIView):
    serializer_class = Compensationserializer
    parser_classes = [MultiPartParser]
    permission_classes = [IsAuthenticated]
    queryset = Compensation.objects.all()

    def update(self , request , id ):
        instance = Compensation.objects.get(id = id )
        serializer = Compensationserializer(instance  , data= request.data , partial = True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data , status = 200)
        else: 
            return Response(serializer.errors , status =400 )

class CompensationListView(generics.ListAPIView):
    serializer_class = Compensationserializer
    renderer_classes = [ErrorRenderer]
    # permission_classes = [IsAuthenticated]
    queryset = Compensation.objects.all()


class constructionSiteView(generics.GenericAPIView):
    renderer_classes = [ErrorRenderer]
    parser_classes = [MultiPartParser]
    permission_classes = [IsAuthenticated]
    serializer_class = constructionSiteSerializer

    def post(self, request):
        try:
            lat = float(request.data['latitude'])
            long = float(request.data['longitude'])
            location = Point(long, lat, srid=4326)
            serialzier = constructionSiteSerializer(data=request.data)
            if serialzier.is_valid(raise_exception=True):
                construction = serialzier.save(location=location)
                data = ConstructionSiteDetailsViewSerializer(construction).data
                return Response(data, status=200)
        except:
            return Response({'msg': 'Please Enter a valid data'}, status=400)

class ConstructionSiteListView(generics.ListAPIView):
    serializer_class = constructionSiteSerializer
    permission_classes = [IsAuthenticated]
    queryset = ConstructionSiteDetails.objects.all()



class LabourCampDetailsView(generics.GenericAPIView):
    renderer_classes = [ErrorRenderer]
    parser_classes = [MultiPartParser]
    serializer_class = LabourCampDetailSerializer
    queryset = LabourCampDetails.objects.all()

    def post(self, request):
        lat = float(request.data['latitude'])
        long = float(request.data['longitude'])
        location = Point(long, lat, srid=4326)
        serializer = LabourCampDetailSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            LabourCampDetails = serializer.save(location=location)
            data = LabourCampDetailViewSerializer(LabourCampDetails).data
            return Response(data, status=200)
        else:
            return Response(serializer.errors, status=400)


class labourcampListView(generics.ListAPIView):
    # permission_classes = [IsAuthenticated]
    pagination_class = LimitsetPagination
    serializer_class = LabourCampDetailViewSerializer
    queryset = LabourCampDetails.objects.all()
