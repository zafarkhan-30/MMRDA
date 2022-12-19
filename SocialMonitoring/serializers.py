from rest_framework import serializers
from .models import PAP, Rehabilation, Compensation, ConstructionSiteDetails, LabourCamp 
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
        fields = ('quarter', 'packages', 'dateOfConduct','longitude', 'latitude', 'dateOfNotification',
                  'actionTaken', 'compensationStatus', 'eligibility', 'categoryOfPap',  'ownershipStatus', 'legalStatus',
                  'rehabilitationStatus' ,'isShiftingAllowance' , 'isLivelihoodSupport' , 'isTraining' , 'isTenaments' ,
                  'isTransportationAllowance' ,'isfinancialSupport','isCommunityEngagement' , 'isEngagementType',
                    )

    def create(self, data):
        data.pop('longitude')
        data.pop('latitude')
        return PAP.objects.create(**data)
    
    # def validate(self,data):
    #     if data['quarter']=="" or data['quarter']==None:
    #         raise serializers.ValidationError("quarter cannot be empty!!")
    #     if data['packages'] == "" or data['packages'] == None:
    #         raise serializers.ValidationError('package cannot be empty!!')
    #     if data['dateOfConduct'] == "" or data['dateOfConduct'] == None:
    #         raise serializers.ValidationError('dateOfConduct cannot be empty')
    #     if data['longitude'] == "" or data['longitude'] == None:
    #         raise serializers.ValidationError('longitude cannot be empty!!')
    #     if data['latitude'] == "" or data['latitude'] == None:
    #         raise serializers.ValidationError('latitude cannot be empty!!')
    #     if data['dateOfNotification'] == "" or data['dateOfNotification'] == None:
    #         raise serializers.ValidationError('dateOfNotification cannot be empty')
    #     if data['actionTaken'] == "" or data['actionTaken'] == None:
    #         raise serializers.ValidationError('action_taken cannot be empty!!')
    #     if data['compensationStatus'] == "" or data['compensationStatus'] == None:
    #         raise serializers.ValidationError('compensationStatus cannot be empty!!')
    #     if data['eligibility'] == "" or data['eligibility'] == None:
    #         raise serializers.ValidationError('eligibility_status cannot be empty!!')
    #     if data['categoryOfPap'] == "" or data['categoryOfPap'] == None:
    #         raise serializers.ValidationError('category_of_PAP cannot be empty!!')
    #     if data ['ownershipStatus'] == "" or data['ownershipStatus'] == None:
    #         raise serializers.ValidationError('Ownership_status cannot be empty!!')
    #     if data['legalStatus'] == "" or data['legalStatus'] == None:
    #         raise serializers.ValidationError('legal_status cannot be empty!!')
    #     if data['rehabilitationStatus'] == "" or data['rehabilitationStatus'] == None:
    #         raise serializers.ValidationError('rehabilitationStatus cannot be empty!!')
    #     if data['isShiftingAllowance'] == "" or data['isShiftingAllowance'] == None:
    #         raise serializers.ValidationError('isShiftingAllowance cannot be empty ')
    #     if data['isLivelihoodSupport'] == "" or data['isLivelihoodSupport'] == None:
    #         raise serializers.ValidationError('isLivelihoodSupport cannot be empty')
    #     if data['isTraining'] == "" or data['isTraining'] == None:
    #         raise serializers.ValidationError('isTraining cannot be empty')
    #     if data['isTenaments'] == "" or data['isTenaments'] == None:
    #         raise serializers.ValidationError('isTenaments cannot be empty')
    #     if data['isTransportationAllowance'] == "" or data['isTransportationAllowance'] == None: 
    #         raise serializers.ValidationError('isTransportationAllowance cannot be empty')
        
        
    #     return data

# class PapUpdateSerialzier(serializers.ModelSerializer):
#     longitude = serializers.CharField(max_length=10, required=False)
#     latitude = serializers.CharField(max_length=10, required=False)
#     class Meta:
#         model = PAP
#         fields = ('quarter', 'packages', 'longitude', 'latitude', 'dateOfNotification',
#                   'action_taken', 'Compensation_offered', 'eligibility_status', 'category_of_PAP',  'Ownership_status', 'legal_status')

class papviewserialzer(GeoFeatureModelSerializer):
    class Meta:
        model = PAP
        fields = '__all__'
        geo_field = 'location'


# class rehabilatinSerializer(serializers.ModelSerializer):
#     #     social_Monitoring=social_MonitoringSerializer(read_only = True)
#     #     papSerailzer =PapSerailzer( many = True, read_only = True)
#     class Meta:
#         model = Rehabilation
#         fields = ['shifting_allowance', 'additional_financial_support_or_revolving_fund',
#                   'livelihood_support', 'traning', 'tenaments', 'transport_allowance', 'Community_engagement']

#     def validate(self, data):
#         # if data['PAP_id']=="" or data['PAP_id']==None:
#         #     raise serializers.ValidationError('PAP_id cannot be empty!!')
#         if data['shifting_allowance'] == "" or data['shifting_allowance'] == None:
#             raise serializers.ValidationError('shifting_allowance cannot be empty!!')
#         if data['additional_financial_support_or_revolving_fund'] == "" or data['additional_financial_support_or_revolving_fund'] == None:
#             raise serializers.ValidationError('additional_financial_support_or_revolving_fund cannot be empty!!')
#         if data['livelihood_support'] == "" or data['livelihood_support'] == None:
#             raise serializers.ValidationError('livelihood_support cannot be empty!!')
#         if data['traning'] == "" or data['traning'] == None:
#             raise serializers.ValidationError('traning cannot be empty!!')
#         if data['tenaments'] == "" or data['tenaments'] == None:
#             raise serializers.ValidationError('tenaments cannot be empty!!')
#         if data['transport_allowance'] == "" or data['transport_allowance'] == None:
#             raise serializers.ValidationError('transport_allowance cannot be empty!!')
#         if data['Community_engagement'] == "" or data['Community_engagement'] == None:
#             raise serializers.ValidationError('Community_engagement cannot be empty!!')

#         return data

# class Compensationserializer(serializers.ModelSerializer):
#     class Meta:
#         model = Compensation
#         fields = ('PAP_id', 'Alternate_accommodation_or_Commercial_Unit',
#                   'cash_compensation', 'land_provided_area')
        
#         def validate(self , data):
#             if data['PAP_id'] == "" or data['PAP_id'] == None:
#                 raise serializers.ValidationError('PAP_id cannot be empty!!')
#             # if data['Alternate_accommodation_or_Commercial_Unit'] == "" or data['Alternate_accommodation_or_Commercial_Unit'] == None:
#             #     raise serializers.ValidationError('Alternate_accommodation_or_Commercial_Unit cannot be empty!!')
#             if data['cash_compensation'] == "" or data['cash_compensation'] == None:
#                 raise serializers.ValidationError('cash_compensation cannot be empty!!')
#             if data['land_provided_area'] == "" or data['land_provided_area'] == None:
#                 raise serializers.ValidationError('land_provided_area cannot be empty!!')
            
#             return data

class constructionSiteSerializer(serializers.ModelSerializer):
    longitude = serializers.CharField(max_length=10, required=False)
    latitude = serializers.CharField(max_length=10, required=False)

    class Meta:
        model = ConstructionSiteDetails
        fields = ('quarter', 'packages','dateOfConduct' ,'longitude', 'latitude',
                  'sitephotographs', 'isDemarkingOfPathwaysCheck','isSignagesLabelingCheck', 'isRegularHealthCheckup',
                  'isAvailabilityOfDoctor', 'isFirstAidKit', 'isDrinkingWaterCheck', 'isToiletFacility')
    
    def create(self,data):
        data.pop('longitude', None)
        data.pop('latitude', None)
        return ConstructionSiteDetails.objects.create(**data)
    
    def validate(self,data):
        if data['quarter']=="" or data['quarter']==None:
            raise serializers.ValidationError("quarter cannot be empty!!")
        if data['packages'] == "" or data['packages'] == None:
            raise serializers.ValidationError('package cannot be empty!!')
        if data['longitude'] == "" or data['longitude'] == None:
            raise serializers.ValidationError('longitude cannot be empty!!')
        if data['latitude'] == "" or data['latitude'] == None:
            raise serializers.ValidationError('latitude cannot be empty!!')
        # if data['LabourCampTitle'] == "" or data['LabourCampTitle'] == None:
        #     raise serializers.ValidationError('LabourCampTitle cannot be empty!!')
        # if data['sitephotographs'] == "" or data['sitephotographs'] == None:  
        #     raise serializers.ValidationError('site_photographs cannot be empty!!')
        if data['isSignagesLabelingCheck'] == "" or data['isSignagesLabelingCheck'] == None:
            raise serializers.ValidationError('signAges_or_labeling cannot be empty!!')
        if data['isDemarkingOfPathwaysCheck'] == "" or data['isDemarkingOfPathwaysCheck'] == None:
            raise serializers.ValidationError('demarking_of_pathways cannot be empty!!')
        if data['isRegularHealthCheckup'] == "" or data['isRegularHealthCheckup'] == None:
            raise serializers.ValidationError('Regular_Health_Checkup cannot be empty!!')
        if data['isAvailabilityOfDoctor'] == "" or data['isAvailabilityOfDoctor'] == None:
            raise serializers.ValidationError('Availability_Of_Doctor cannot be empty!!')   
        if data['isFirstAidKit'] == "" or data['isFirstAidKit'] == None:
            raise serializers.ValidationError('Availability_Of_First_aid_Kit cannot be empty!!')
        if data['isDrinkingWaterCheck'] == "" or data['isDrinkingWaterCheck'] == None:
            raise serializers.ValidationError('Drinking_water cannot be empty!!')
        if data['isToiletFacility'] == "" or data['isToiletFacility'] == None:
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
        model = LabourCamp
        fields = ('quarter', 'packages','longitude', 'latitude', 'LabourCampTitle',
                  'isToilet', 'isDrinkingWater', 'isDemarkingOfPathways', 'isSignagesLabeling',
                  'isRegularHealthCheckup', 'isAvailabilityOfDoctor', 'isFirstAidKit',
                  'isKitchenArea',   'isFireExecution', 'isSegregationOfWaste', 'isRoomsOrDoms' , 'transportationFacility')

    def create(self,data):
        data.pop('longitude')
        data.pop('latitude')
        return LabourCamp.objects.create(**data)
        
    def validate(self , data):
        if data['quarter']=="" or data['quarter']==None:
            raise serializers.ValidationError("quarter cannot be empty!!")
        if data['packages'] == "" or data['packages'] == None:
            raise serializers.ValidationError('package cannot be empty!!')
        if data['longitude'] == "" or data['longitude'] == None:
            raise serializers.ValidationError('longitude cannot be empty!!')
        if data['latitude'] == "" or data['latitude'] == None:
            raise serializers.ValidationError('latitude cannot be empty!!')
        if data['isToilet'] == "" or data['isToilet'] == None:
            raise serializers.ValidationError('toilets cannot be empty!!')
        if data['LabourCampTitle'] == "" or data['LabourCampTitle'] == None:
            raise serializers.ValidationError('labourcamp Title cannot be empty!!')
        if data['isDrinkingWater'] == "" or data['isDrinkingWater'] == None:
            raise serializers.ValidationError('Drinking_water cannot be empty!!')
        if data ['isDemarkingOfPathways'] == "" or data['isDemarkingOfPathways'] == None:
            raise serializers.ValidationError('demarking_of_pathways cannot be empty!!')
        if data['isSignagesLabeling'] == "" or data['isSignagesLabeling'] == None:
            raise serializers.ValidationError('signAges_or_labeling cannot be empty!!')
        if data['isRegularHealthCheckup'] == "" or data['isRegularHealthCheckup'] == None:
            raise serializers.ValidationError('Regular_Health_Checkup cannot be empty!!')
        if data['isAvailabilityOfDoctor'] == "" or data['isAvailabilityOfDoctor'] == None:
            raise serializers.ValidationError('Availability_Of_First_aid_Kit cannot be empty!!')
        if data['isFirstAidKit'] == "" or data['isFirstAidKit'] == None:
            raise serializers.ValidationError('Availability_Of_Doctor cannot be empty!!')
        if data['isKitchenArea'] == "" or data['isKitchenArea'] == None:
            raise serializers.ValidationError('kitchen_area cannot be empty !!')
        if data['isFireExecution'] == "" or data['isFireExecution'] == None:
            raise serializers.ValidationError('fire_execution cannot be empty!!')
        if data['isSegregationOfWaste'] == "" or data['isSegregationOfWaste'] == None:
            raise serializers.ValidationError('segregation_of_waste cannot be empty!!')
        if data['isRoomsOrDoms'] == "" or data['isRoomsOrDoms'] == None:
            raise serializers.ValidationError('rooms_or_doms cannot be empty!!')
        if data[ 'transportationFacility'] == "" or data['transportationFacility'] == None:
            raise serializers.ValidationError('transport_facility cannot be empty')

        return data

class LabourCampDetailViewSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = LabourCamp
        fields = '__all__'
        geo_field = 'location'

# class testserialzier(serializers.ModelSerializer):
#     class Meta:
#         model = Test
#         fields = '__all__'