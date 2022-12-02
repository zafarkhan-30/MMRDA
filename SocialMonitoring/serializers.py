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
    
    def validate(self,data):
        if data['quarter']=="" or data['quarter']==None:
            raise serializers.ValidationError("quarter cannot be empty!!")
        if data['package'] == "" or data['package'] == None:
            raise serializers.ValidationError('package cannot be empty!!')
        if data['longitude'] == "" or data['longitude'] == None:
            raise serializers.ValidationError('longitude cannot be empty!!')
        if data['latitude'] == "" or data['latitude'] == None:
            raise serializers.ValidationError('latitude cannot be empty!!')
        if data['pap_id '] == "" or data['pap_id'] == None:
            raise serializers.ValidationError('pap_id cannot be empty!!')
        if data['date_of_notification'] == "" or data['date_of_notification'] == None:
            raise serializers.ValidationError('date_of_notification cannot be empty!!')
        if data['action_taken'] == "" or data['action_taken'] == None:
            raise serializers.ValidationError('action_taken cannot be empty!!')
        if data['Compensation_offered'] == "" or data['Compensation_offered'] == None:
            raise serializers.ValidationError('Compensation_offered cannot be empty!!')
        if data['eligibility_status'] == "" or data['eligibility_status'] == None:
            raise serializers.ValidationError('eligibility_status cannot be empty!!')
        if data['category_of_PAP'] == "" or data['category_of_PAP'] == None:
            raise serializers.ValidationError('category_of_PAP cannot be empty!!')
        if data ['Ownership_status'] == "" or data['Ownership_status'] == None:
            raise serializers.ValidationError('Ownership_status cannot be empty!!')
        if data['legal_status'] == "" or data['legal_status'] == None:
            raise serializers.ValidationError('legal_status cannot be empty!!')
        return data



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

    def validate(self, data):
        if data['rehabilation_id']=="" or data['rehabilation_id']==None:
            raise serializers.ValidationError('rehabilation_id cannot be empty!!')
        if data['shifting_allowance'] == "" or data['shifting_allowance'] == None:
            raise serializers.ValidationError('shifting_allowance cannot be empty!!')
        if data['additional_financial_support_or_revolving_fund'] == "" or data['additional_financial_support_or_revolving_fund'] == None:
            raise serializers.ValidationError('additional_financial_support_or_revolving_fund cannot be empty!!')
        if data['livelihood_support'] == "" or data['livelihood_support'] == None:
            raise serializers.ValidationError('livelihood_support cannot be empty!!')
        if data['traning'] == "" or data['traning'] == None:
            raise serializers.ValidationError('traning cannot be empty!!')
        if data['tenaments'] == "" or data['tenaments'] == None:
            raise serializers.ValidationError('tenaments cannot be empty!!')
        if data['transport_allowance'] == "" or data['transport_allowance'] == None:
            raise serializers.ValidationError('transport_allowance cannot be empty!!')
        if data['Community_engagement'] == "" or data['Community_engagement'] == None:
            raise serializers.ValidationError('Community_engagement cannot be empty!!')

        return data

class Compensationserializer(serializers.ModelSerializer):
    class Meta:
        model = Compensation
        fields = ('Compensation_id', 'Alternate_accommodation_or_Commercial_Unit',
                  'cash_compensation', 'land_provided_area')
        
        def validate(self , data):
            if data['Compensation_id'] == "" or data['Compensation_id'] == None:
                raise serializers.ValidationError('Compensation_id cannot be empty!!')
            # if data['Alternate_accommodation_or_Commercial_Unit'] == "" or data['Alternate_accommodation_or_Commercial_Unit'] == None:
            #     raise serializers.ValidationError('Alternate_accommodation_or_Commercial_Unit cannot be empty!!')
            if data['cash_compensation'] == "" or data['cash_compensation'] == None:
                raise serializers.ValidationError('cash_compensation cannot be empty!!')
            if data['land_provided_area'] == "" or data['land_provided_area'] == None:
                raise serializers.ValidationError('land_provided_area cannot be empty!!')
            
            return data

class constructionSiteSerializer(serializers.ModelSerializer):
    longitude = serializers.CharField(max_length=10, required=False)
    latitude = serializers.CharField(max_length=10, required=False)

    class Meta:
        model = ConstructionSiteDetails
        fields = ('quarter', 'package', 'longitude', 'latitude', 'construction_id',
                  'site_photographs', 'signAges_or_labeling', 'Regular_Health_Checkup',
                  'Availability_Of_Doctor', 'Availability_Of_First_aid_Kit', 'Drinking_water', 'Toilet_facility')
    
    def create(self,data):
        data.pop('longitude', None)
        data.pop('latitude', None)
        return ConstructionSiteDetails.objects.create(**data)
    
    def validate(self,data):
        if data['quarter']=="" or data['quarter']==None:
            raise serializers.ValidationError("quarter cannot be empty!!")
        if data['package'] == "" or data['package'] == None:
            raise serializers.ValidationError('package cannot be empty!!')
        if data['longitude'] == "" or data['longitude'] == None:
            raise serializers.ValidationError('longitude cannot be empty!!')
        if data['latitude'] == "" or data['latitude'] == None:
            raise serializers.ValidationError('latitude cannot be empty!!')
        if data['construction_id'] == "" or data['construction_id'] == None:
            raise serializers.ValidationError('construction_id cannot be empty!!')
        if data['site_photographs'] == "" or data['site_photographs'] == None:  
            raise serializers.ValidationError('site_photographs cannot be empty!!')
        if data['signAges_or_labeling'] == "" or data['signAges_or_labeling'] == None:
            raise serializers.ValidationError('signAges_or_labeling cannot be empty!!')
        if data['Regular_Health_Checkup'] == "" or data['Regular_Health_Checkup'] == None:
            raise serializers.ValidationError('Regular_Health_Checkup cannot be empty!!')
        if data['Availability_Of_Doctor'] == "" or data['Availability_Of_Doctor'] == None:
            raise serializers.ValidationError('Availability_Of_Doctor cannot be empty!!')   
        if data['Availability_Of_First_aid_Kit'] == "" or data['Availability_Of_First_aid_Kit'] == None:
            raise serializers.ValidationError('Availability_Of_First_aid_Kit cannot be empty!!')
        if data['Drinking_water'] == "" or data['Drinking_water'] == None:
            raise serializers.ValidationError('Drinking_water cannot be empty!!')
        if data['Toilet_facility'] == "" or data['Toilet_facility'] == None:
            raise serializers.ValidationError('Toilet_facility cannot be empty!!')
        
        return data

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

    def create(self,data):
        data.pop('longitude')
        data.pop('latitude')
        return LabourCampDetails.objects.create(**data)
    def validate(self , data):
        if data['quarter']=="" or data['quarter']==None:
            raise serializers.ValidationError("quarter cannot be empty!!")
        if data['package'] == "" or data['package'] == None:
            raise serializers.ValidationError('package cannot be empty!!')
        if data['longitude'] == "" or data['longitude'] == None:
            raise serializers.ValidationError('longitude cannot be empty!!')
        if data['latitude'] == "" or data['latitude'] == None:
            raise serializers.ValidationError('latitude cannot be empty!!')
        if data['toilets'] == "" or data['toilets'] == None:
            raise serializers.ValidationError('toilets cannot be empty!!')
        if data['Drinking_water'] == "" or data['Drinking_water'] == None:
            raise serializers.ValidationError('Drinking_water cannot be empty!!')
        if data ['demarking_of_pathways'] == "" or data['demarking_of_pathways'] == None:
            raise serializers.ValidationError('demarking_of_pathways cannot be empty!!')
        if data['signAges_or_labeling'] == "" or data['signAges_or_labeling'] == None:
            raise serializers.ValidationError('signAges_or_labeling cannot be empty!!')
        if data['Regular_Health_Checkup'] == "" or data['Regular_Health_Checkup'] == None:
            raise serializers.ValidationError('Regular_Health_Checkup cannot be empty!!')
        if data['Availability_Of_First_aid_Kit'] == "" or data['Availability_Of_First_aid_Kit'] == None:
            raise serializers.ValidationError('Availability_Of_First_aid_Kit cannot be empty!!')
        if data['Availability_Of_Doctor'] == "" or data['Availability_Of_Doctor'] == None:
            raise serializers.ValidationError('Availability_Of_Doctor cannot be empty!!')
        if data['kitchen_area'] == "" or data['kitchen_area'] == None:
            raise serializers.ValidationError('kitchen_area cannot be empty !!')
        if data['fire_execution'] == "" or data['fire_execution'] == None:
            raise serializers.ValidationError('fire_execution cannot be empty!!')
        if data['segregation_of_waste'] == "" or data['segregation_of_waste'] == None:
            raise serializers.ValidationError('segregation_of_waste cannot be empty!!')
        if data['rooms_or_doms'] == "" or data['rooms_or_doms'] == None:
            raise serializers.ValidationError('rooms_or_doms cannot be empty!!')

        return data

class LabourCampDetailViewSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = LabourCampDetails
        fields = '__all__'
        geo_field = 'location'