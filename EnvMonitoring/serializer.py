from rest_framework import serializers 
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from .models import (User , Air , Noise , water , TreeManagment , WasteTreatments , MaterialSourcing ,)

class AirSerializer(serializers.ModelSerializer):
    longitude=serializers.CharField(max_length=10,required=False)
    latitude=serializers.CharField(max_length=10,required=False)
    class Meta:
        model = Air
        fields = ('quarter','package','longitude','latitude','standard','deviation','trends')
        # geo_field='location'
    def create(self,data):
        data.pop('latitude')
        data.pop('longitude')
        return Air.objects.create(**data)

    def validate(self, data):
        if data['quarter']=="" or data['quarter']==None:
            raise serializers.ValidationError("quarter cannot be empty!!")
        if data['package'] == "" or data['package'] == None:
            raise serializers.ValidationError('package cannot be empty!!')
        if data['longitude'] == "" or data['longitude'] == None:
            raise serializers.ValidationError('longitude cannot be empty!!')
        if data['latitude'] == "" or data['latitude'] == None:
            raise serializers.ValidationError('latitude cannot be empty!!')
        # if data['air_id'] == "" or data['air_id'] == None:
        #     raise serializers.ValidationError( 'air_id cannot be empty!!')
        if data['standard'] == "" or data['standard'] == None: 
            raise serializers.ValidationError( 'standard cannot be empty!!')
        if data['deviation'] == "" or data['deviation'] == None:
            raise serializers.ValidationError( 'deviation cannot be empty!!')
        if data ['trends'] == "" or data['trends'] == None:
            raise serializers.ValidationError('Trends cannot be empty!!')
        return data
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
        fields = ('quarter','package','longitude','latitude','quality_of_water' , 'source_of_water')

    def create(self,data):
        data.pop('latitude')
        data.pop('longitude')
        return water.objects.create(**data)

    def validate(self,data):
        if data['quarter']=="" or data['quarter']==None:
            raise serializers.ValidationError("quarter cannot be empty!!")
        if data['package'] == "" or data['package'] == None:
            raise serializers.ValidationError('package cannot be empty!!')
        if data['longitude'] == "" or data['longitude'] == None:
            raise serializers.ValidationError('longitude cannot be empty!!')
        if data['latitude'] == "" or data['latitude'] == None:
            raise serializers.ValidationError('latitude cannot be empty!!')
        # if data['water_id'] == "" or data['water_id'] == None:
        #     raise serializers.ValidationError('water_id cannot be empty!!')
        if data['quality_of_water'] == "" or data['quality_of_water'] == None:
            raise serializers.ValidationError('quality_of_water cannot be empty!!')
        if data['source_of_water'] == "" or data['source_of_water'] == None:
            raise serializers.ValidationError('source_of_water cannot be empty!!')
        return data
        

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
        fields = ('quarter','package','longitude','latitude' ,'noise_level' , 'Monitoring_Period', )

    def create(self,data):
        data.pop('latitude')
        data.pop('longitude')
        return Noise.objects.create(**data)

    def validate(self,data):
        if data['quarter']=="" or data['quarter']==None:
            raise serializers.ValidationError("quarter cannot be empty!!")
        if data['package'] == "" or data['package'] == None:
            raise serializers.ValidationError('package cannot be empty!!')
        if data['longitude'] == "" or data['longitude'] == None:
            raise serializers.ValidationError('longitude cannot be empty!!')
        if data['latitude'] == "" or data['latitude'] == None:
            raise serializers.ValidationError('latitude cannot be empty!!')
        # if data ['noise_id'] == "" or data['noise_id'] == None:
        #     raise serializers.ValidationError('noise_id cannot be empty!!')
        if data['noise_level'] == "" or data['noise_level'] == None:
            raise serializers.ValidationError('noise_level cannot be empty!!')
        if data['Monitoring_Period'] == "" or data['Monitoring_Period'] == None:
            raise serializers.ValidationError('Monitoring_Period cannot be empty!!')
        return data

class Noiseviewserializer(GeoFeatureModelSerializer):
    class Meta:
        model = Noise
        fields = '__all__'
        geo_field='location'

# class EnvQualityMonitoringSerializer(serializers.ModelSerializer):
#     air = AirSerializer(read_only = True )
#     noise = NoiseSerializer(read_only = True)
#     water = WaterSerializer(read_only = True)
#     class Meta:
#         model = EnvQualityMonitoring
#         fields =  [ 'noise' , 'water','air']
        
#         depth = 2
        
# class envMonitoringSerailzer(serializers.ModelSerializer):
#     # Env = EnvQualityMonitoringSerializer( read_only = True) 
#     # air = AirSerializer(read_only = True )
#     # noise = NoiseSerializer(read_only = True)
#     # water = WaterSerializer(read_only = True)
#     class Meta:
#         model = EnvMonitoring
#         fields ='__all__'

        
class TreeManagementSerailizer(serializers.ModelSerializer):
    longitude=serializers.CharField(max_length=10,required=False)
    latitude=serializers.CharField(max_length=10,required=False)
    class Meta:
        model = TreeManagment
        fields = ('quarter','package','longitude','latitude' , 'common_name' ,'botanical_name',
                    'condition', 'survey_date' , 'survey_time' , 'planted','planted_details' , 'No_of_trees_cut',
                   'Cutting_details' , 'transplanted', 'transplanted_details' ,'Management'  )
        
    def create(self,data):
        data.pop('latitude')
        data.pop('longitude')
        return TreeManagment.objects.create(**data)
    
    def validate(self,data):
        if data['quarter']=="" or data['quarter']==None:
            raise serializers.ValidationError("quarter cannot be empty!!")
        if data['package'] == "" or data['package'] == None:
            raise serializers.ValidationError('package cannot be empty!!')
        if data['longitude'] == "" or data['longitude'] == None:
            raise serializers.ValidationError('longitude cannot be empty!!')
        if data['latitude'] == "" or data['latitude'] == None:
            raise serializers.ValidationError('latitude cannot be empty!!')
        if data['common_name'] == "" or data['common_name'] == None:
            raise serializers.ValidationError('common_name cannot be empty!!')
        if data['botanical_name'] == "" or data['botanical_name'] == None:
            raise serializers.ValidationError('botanical_name cannot be empty!!')
        if data['condition'] == "" or data['condition'] == None:
            raise serializers.ValidationError('condition cannot be empty!!') 
        if data['survey_time'] == "" or data['survey_time'] == None:
            raise serializers.ValidationError('survey_time cannot be empty!!') 
        if data['survey_date'] == "" or data['survey_date'] == None:
            raise serializers.ValidationError('survey_date cannot be empty!!')
        if data['planted'] == "" or data['planted'] == None:
            raise serializers.ValidationError('planted cannot be empty!!')
        if data['transplanted'] == "" or data['transplanted'] == None:
            raise serializers.ValidationError('transplanted cannot be empty!!')
        
        return data
        


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
        fields = ('quarter','package','longitude','latitude'  , 'waste_type' ,'quantity',
         'waste_handled' , 'waste_handled_details' , 'photographs' , 'documents','remarks')

    def create(self,data):
        data.pop('longitude')
        data.pop('latitude')
        return WasteTreatments.objects.create(**data)

    def validate(self,data):
        if data['quarter']=="" or data['quarter']==None:
            raise serializers.ValidationError("quarter cannot be empty!!")
        if data['package'] == "" or data['package'] == None:
            raise serializers.ValidationError('package cannot be empty!!')
        if data['longitude'] == "" or data['longitude'] == None:
            raise serializers.ValidationError('longitude cannot be empty!!')
        if data['latitude'] == "" or data['latitude'] == None:
            raise serializers.ValidationError('latitude cannot be empty!!')
        # if data['waste_id'] == "" or data['waste_id'] == None:
        #     raise serializers.ValidationError('waste_id cannot be empty!!')
        if data['waste_type'] == "" or data['waste_type'] == None:
            raise serializers.ValidationError('waste_type cannot be empty!!')
        if data ['quantity'] == "" or data['quantity'] == None:
            raise serializers.ValidationError('quantity cannot be empty!!')
        if data['waste_handled'] == "" or data['waste_handled'] == None:
            raise serializers.ValidationError('waste_handled cannot be empty!!')
    
        
        return data

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
        fields = ('quarter','package','longitude','latitude' ,'approvals','source_of_quary')

    def validate(self,data):
        if data['quarter']=="" or data['quarter']==None:
            raise serializers.ValidationError("quarter cannot be empty!!")
        if data['package'] == "" or data['package'] == None:
            raise serializers.ValidationError('package cannot be empty!!')
        if data['longitude'] == "" or data['longitude'] == None:
            raise serializers.ValidationError('longitude cannot be empty!!')
        if data['latitude'] == "" or data['latitude'] == None:
            raise serializers.ValidationError('latitude cannot be empty!!')
        # if data['materialsourcing_id'] == "" or data['materialsourcing_id'] == None:
        #     raise serializers.ValidationError('materialsourcing_id cannot be empty!!')
        if data['source_of_quary'] == "" or data['source_of_quary'] == None:
            raise serializers.ValidationError('source_of_quary cannot be empty!!')
        
        return data

    def create(self,data):
        data.pop('longitude')
        data.pop('latitude')
        return MaterialSourcing.objects.create(**data)

    

class MaterialSourcingViewserializer(GeoFeatureModelSerializer):
    class Meta:
        model = MaterialSourcing
        fields = '__all__'
        geo_field = 'location'

        
# class EnvQualityMonitoringSerailzer(serializers.ModelSerializer):
#     # EnvMonitoring = envMonitoringSerailzer(read_only = True)
#     noise = NoiseSerializer(read_only = True )
#     water=WaterSerializer( read_only = True)
#     air = AirSerializer(read_only = True)

#     class Meta: 
#         model = EnvQualityMonitoring
#         fields = ['eqm_id' ,'noise' , 'air','water' ]

#         depth = 1