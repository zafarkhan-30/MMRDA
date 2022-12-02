
from django.urls import path
from .views import ( AirView , AirListView, WaterView , waterListView, NoiseView ,NoiseListView,
TreeManagementView, TereeManagementView,EnvMonitoringView , envMonitoringView ,WasteTreatmentsView  ,MaterialSourcingView)

urlpatterns = [
path('envmonitoring' , EnvMonitoringView.as_view() , name = 'envmonitoring'),
    path('air' , AirView.as_view() , name = 'Air Details'),
    path('airList', AirListView.as_view() , name = 'ListAirView'),

    path('water' , WaterView.as_view() , name = 'water Details'),
    path('waterList' , waterListView.as_view() , name = 'water Details'),

    path('noise' , NoiseView.as_view() , name = "Noise Details"),
    path('noiseList' ,NoiseListView.as_view() , name = "Noise"),

    path('envview' , envMonitoringView.as_view() , name = 'EnvQualityMonitoring'),
    path('tree' , TreeManagementView.as_view() , name = "Tree Management"),
    path('treeView' , TereeManagementView.as_view() , name = "Tree Management list"),


    
    path('waste' , WasteTreatmentsView.as_view() , name = "Waste Management"),
    path('materialsourcing' , MaterialSourcingView.as_view() , name = "Material Sourcing") , ]