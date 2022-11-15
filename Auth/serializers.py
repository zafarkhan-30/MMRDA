from tkinter.ttk import Style
from rest_framework import serializers
from .models import User , Air , Noise , water , photographs , EnvMonitoring , EnvQualityMonitoring
#  , Air, photographs, traning, water ,EnvQualityMonitoring, constructionCamp,LabourCamp,
#  EnvMonitoring , social_Monitoring , PAP ,LabourSite, Rehabilation , TreeManagment ,WasteTreatments , MaterialSourcing)
from django.contrib.auth import authenticate


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(style = {'input_type':'password'},write_only = True)
    class Meta:
        model = User
        fields = '__all__'
        
    

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
       


class AirSerializer(serializers.ModelSerializer):
    class Meta:
        model = Air
        fields = "__all__"



class WaterSerializer(serializers.ModelSerializer):
    class Meta:
        model = water
        fields = "__all__"



class NoiseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Noise
        fields = "__all__"

        
class envMonitoringSerailzer(serializers.ModelSerializer):
    class Meta:
        model = EnvMonitoring
        fields = ['__all__']

        
# class TreeManagementSerailizer(serializers.ModelSerializer):
#     class Meta:
#         model = TreeManagment
#         fields = '__all__'

# class WasteTreatmentsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model  = WasteTreatments
#         fields = '__all__'

# class MaterialSourcingSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = MaterialSourcing
#         fields = '__all__'


class EnvQualityMonitoringSerailzer(serializers.ModelSerializer):
    EnvMonitoring = envMonitoringSerailzer(read_only = True)
    noise = NoiseSerializer(read_only = True )
    water=WaterSerializer( read_only = True)
    air = AirSerializer(read_only = True)

    class Meta: 
        model = EnvQualityMonitoring
        fields = ['eqm_id' , 'EnvMonitoring','noise' , 'air','water' ]

        depth = 2



# class EnvMonitoringSerailzer(serializers.ModelSerializer):
#     eqm_id =EnvQualityMonitoringSerailzer(  read_only = True)
#     air = AirSerializer(read_only = True)
#     noise = NoiseSerializer( read_only = True)
#     water=WaterSerializer( read_only = True)
    
#     class Meta:
#         model = EnvMonitoring
#         fields = ['env_quality_monitoring' ,'eqm_id',"noise" , "water"  , 'air']



# class social_MonitoringSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = PAP
#         fields = '__all__'



# class PapSerailzer(serializers.ModelSerializer):
#     class Meta:
#         model = PAP
#         fields = '__all__'


# class rehabilatinSerializer(serializers.ModelSerializer):
#     social_Monitoring=social_MonitoringSerializer(read_only = True)
#     papSerailzer =PapSerailzer( many = True, read_only = True)
#     class Meta:
#         model = Rehabilation
#         fields = ['social_Monitoring','papSerailzer' , 'rehabilation_id' ,'shifting_allowance' , 
#                     'livelihood' , 'traning' , 'tenements']
        
#         depth = 3

# class LabourCampSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = LabourCamp
#         fields = '__all__'
        

# class constructionCampSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = constructionCamp
#         fields = '__all__'


# class LabourSiteSerialzer(serializers.ModelSerializer):
#     class Meta:
#         model = LabourSite
#         fields = '__all__'


        
# class social_MonitoringSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = PAP
#         fields = '__all__'



# # class OccupationalHealthSafetySerailzers(serializers.ModelSerializer):
# #     class Meta:
# #         model = occupationalHealthSafety
# #         fields = "__all__"




# class TraningSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = traning
#         fields = '__all__'



class photographsSerializer(serializers.ModelSerializer):
    class Meta:
        model = photographs
        fields = '__all__'
        


        

