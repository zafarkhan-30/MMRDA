from django.urls import path
from .views import (  UserRegister , LoginView ,)


urlpatterns = [
    
    path('register' , UserRegister.as_view() , name= 'Register'),
    path('login' , LoginView.as_view() , name= 'login'),

    
    
    # path('healthsafety' , OccupationalHealthSafetyView.as_view() , name = 'Health & safety'),

    # path('traning' , TraningView.as_view() , name = 'traning'),
    
    # path('photographs' , PhotographsView.as_view() , name = 'photographs')

]
