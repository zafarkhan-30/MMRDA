

from django.urls import path
from .views import (  UserRegister , LoginView ,AirView , WaterView , NoiseView , PhotographsView , EnvMonitoringView , EnvQualityMonitoringView)


urlpatterns = [
    path('register' , UserRegister.as_view() , name= 'Register'),
    path('login' , LoginView.as_view() , name= 'login'),

    path('envmonitoring' , EnvMonitoringView.as_view() , name = 'envmonitoring'),
    path('air' , AirView.as_view() , name = 'Air'),
    path('water' , WaterView.as_view() , name = 'water'),
    path('noise' , NoiseView.as_view() , name = "Noise"),
    path('envQuality' , EnvQualityMonitoringView.as_view() , name = 'EnvQualityMonitoring'),
    # path('tree' , TreeManagementView.as_view() , name = "tree"),
    # path('waste' , WasteTreatmentsView.as_view() , name = "waste"),

    # path ('pap' , PapView.as_view() , name = "project affected Person "),
    # path ('rehabilation' , RehabilationView.as_view() , name = "rehabilation"),
    # path ('socialmonitor' , SocialMonitorView.as_view() , name = "social monitoring"),
    
    # # path('healthsafety' , OccupationalHealthSafetyView.as_view() , name = 'healthsafety'),

    # path('traning' , TraningView.as_view() , name = 'traning'),
    
    path('photographs' , PhotographsView.as_view() , name = 'photographs')

]
