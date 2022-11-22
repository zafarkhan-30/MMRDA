
from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from .models import (User , Air , Noise , water ,EnvMonitoring , 
EnvQualityMonitoring , TreeManagment , WasteTreatments , MaterialSourcing ,)

class AirSerializer(serializers.ModelSerializer):
    longitude=serializers.CharField(max_length=10,required=False)
    latitude=serializers.CharField(max_length=10,required=False)
    class Meta:
        model = Air
        fields = ('quarter','package','longitude','latitude','air_id','standard','deviation','trends')
        # geo_field='location'
    def create(self,data):
        data.pop('latitude')
        data.pop('longitude')
        return Air.objects.create(**data)

class AirViewSerializer(GeoFeatureModelSerializer):
    class Meta:
        model=Air
        fields='__all__'
        geo_field='location'

class WaterSerializer(serializers.ModelSerializer):
    longitude=serializers.CharField(max_length=10,required=False)
    latitude=serializers.CharField(max_length=10,required=False)
    class Meta:
        model = water
        fields = ('quarter','package','longitude','latitude','water_id','quality_of_water' , 'source_of_water')

    def create(self,data):
        data.pop('latitude')
        data.pop('longitude')
        return water.objects.create(**data)

class waterviewserializer(GeoFeatureModelSerializer):
    class Meta:
        model = water
        fields = '__all__'
        geo_field='location'


class NoiseSerializer(serializers.ModelSerializer):
    longitude=serializers.CharField(max_length=10,required=False)
    latitude=serializers.CharField(max_length=10,required=False)
    class Meta:
        model = Noise
        fields = ('quarter','package','longitude','latitude' ,'noise_id','noise_level' , 'Monitoring_Period', )

    def create(self,data):
        data.pop('latitude')
        data.pop('longitude')
        return Noise.objects.create(**data)

class Noiseviewserializer(GeoFeatureModelSerializer):
    class Meta:
        model = Noise
        fields = '__all__'
        geo_field='location'

class EnvQualityMonitoringSerializer(serializers.ModelSerializer):
    air = AirSerializer(read_only = True )
    noise = NoiseSerializer(read_only = True)
    water = WaterSerializer(read_only = True)
    class Meta:
        model = EnvQualityMonitoring
        fields =  [ 'noise' , 'water','air']
        
        depth = 2
        
class envMonitoringSerailzer(serializers.ModelSerializer):
    # Env = EnvQualityMonitoringSerializer( read_only = True) 
    air = AirSerializer(read_only = True )
    noise = NoiseSerializer(read_only = True)
    water = WaterSerializer(read_only = True)
    class Meta:
        model = EnvQualityMonitoring
        fields = ['eqm_id' , 'noise' , 'water','air']

        
class TreeManagementSerailizer(serializers.ModelSerializer):
    longitude=serializers.CharField(max_length=10,required=False)
    latitude=serializers.CharField(max_length=10,required=False)
    class Meta:
        model = TreeManagment
        fields = ('quarter','package','longitude','latitude' ,'tree_id' , 'planted' , 'planted_details' , 'No_of_trees_cut',
                   'Cutting_details' , 'transplanted', 'transplanted_details' ,'Management'  )
        
    def create(self,data):
        data.pop('latitude')
        data.pop('longitude')
        return TreeManagment.objects.create(**data)


class TreeManagmentviewserializer(GeoFeatureModelSerializer):
    class Meta:
        model = TreeManagment
        fields = '__all__'
        geo_field = 'location'

class WasteTreatmentsSerializer(serializers.ModelSerializer):
    longitude=serializers.CharField(max_length=10,required=False)
    latitude=serializers.CharField(max_length=10,required=False)
    class Meta:
        model  = WasteTreatments
        fields = ('quarter','package','longitude','latitude' ,'waste_id' , 'waste_type' ,'quantity',
         'waste_handled' , 'waste_handled_details' , 'photographs' , 'documents','remarks')

    def create(self,data):
        data.pop('longitude')
        data.pop('latitude')
        return WasteTreatments.objects.create(**data)

class wastetreatmentsViewserializer(GeoFeatureModelSerializer):
    class Meta: 
        model = WasteTreatments
        fields = '__all__'
        geo_field= 'location'



class MaterialSourcingSerializer(serializers.ModelSerializer):
    longitude=serializers.CharField(max_length=10,required=False)
    latitude=serializers.CharField(max_length=10,required=False)
    class Meta:
        model = MaterialSourcing
        fields = ('quarter','package','longitude','latitude' ,'materialsourcing_id','approvals','source_of_quary')

    def create(self,data):
        data.pop('longitude')
        data.pop('latitude')
        return MaterialSourcing.objects.create(**data)

class MaterialSourcingViewserializer(GeoFeatureModelSerializer):
    class Meta:
        model = MaterialSourcing
        fields = '__all__'
        geo_field = 'location'

        
class EnvQualityMonitoringSerailzer(serializers.ModelSerializer):
    # EnvMonitoring = envMonitoringSerailzer(read_only = True)
    noise = NoiseSerializer(read_only = True )
    water=WaterSerializer( read_only = True)
    air = AirSerializer(read_only = True)

    class Meta: 
        model = EnvQualityMonitoring
        fields = ['eqm_id' ,'noise' , 'air','water' ]

        depth = 1