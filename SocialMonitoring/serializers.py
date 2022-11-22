from rest_framework import serializers
from .models import PAP, Rehabilation, Compensation, ConstructionSiteDetails, LabourCampDetails
from rest_framework_gis.serializers import GeoFeatureModelSerializer


class social_MonitoringSerializer(serializers.ModelSerializer):
    class Meta:
        model = PAP
        fields = '__all__'


class PapSerailzer(serializers.ModelSerializer):
    longitude = serializers.CharField(max_length=10, required=False)
    latitude = serializers.CharField(max_length=10, required=False)

    class Meta:
        model = PAP
        fields = ('quarter', 'package', 'longitude', 'latitude', 'pap_id', 'date_of_notification',
                  'action_taken', 'Compensation_offered', 'eligibility_status', 'category_of_PAP',  'Ownership_status', 'legal_status')

    def create(self, data):
        data.pop('longitude')
        data.pop('latitude')
        return PAP.objects.create(**data)


class papviewserialzer(GeoFeatureModelSerializer):
    class Meta:
        model = PAP
        fields = '__all__'
        geo_field = 'location'


class rehabilatinSerializer(serializers.ModelSerializer):
    #     social_Monitoring=social_MonitoringSerializer(read_only = True)
    #     papSerailzer =PapSerailzer( many = True, read_only = True)
    class Meta:
        model = Rehabilation
        fields = ['rehabilation_id', 'shifting_allowance', 'additional_financial_support_or_revolving_fund',
                  'livelihood_support', 'traning', 'tenaments', 'transport_allowance', 'Community_engagement']


class Compensationserializer(serializers.ModelSerializer):
    class Meta:
        model = Compensation
        fields = ('Compensation_id', 'Alternate_accommodation_or_Commercial_Unit',
                  'cash_compensation', 'land_provided_area')


class constructionSiteSerializer(serializers.ModelSerializer):
    longitude = serializers.CharField(max_length=10, required=False)
    latitude = serializers.CharField(max_length=10, required=False)

    class Meta:
        model = ConstructionSiteDetails
        fields = ('quarter', 'package', 'longitude', 'latitude', 'construction_id',
                  'site_photographs', 'signAges_or_labeling', 'Regular_Health_Checkup',
                  'Availability_Of_Doctor', 'Availability_Of_First_aid_Kit', 'Drinking_water', 'Toilet_facility')


class ConstructionSiteDetailsViewSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = ConstructionSiteDetails
        fields = '__all__'
        geo_field = 'location'


class LabourCampDetailSerializer(serializers.ModelSerializer):
    longitude = serializers.CharField(max_length=10, required=False)
    latitude = serializers.CharField(max_length=10, required=False)
    class Meta:
        model = LabourCampDetails
        fields = ('quarter', 'package', 'longitude', 'latitude', 'labourcamp_id',
                  'toilets', 'Drinking_water', 'demarking_of_pathways', 'signAges_or_labeling',
                  'Regular_Health_Checkup', 'Availability_Of_Doctor', 'Availability_Of_First_aid_Kit',
                  'kitchen_area',   'fire_execution', 'segregation_of_waste', 'rooms_or_doms')

class LabourCampDetailViewSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = LabourCampDetails
        fields = '__all__'
        geo_field = 'location'