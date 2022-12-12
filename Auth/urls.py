from django.urls import path
from .views import (UserRegister, LoginView,)


urlpatterns = [

    path('register', UserRegister.as_view(), name='Register'),
    path('login', LoginView.as_view(), name='login'),



    # path('healthsafety' , OccupationalHealthSafetyView.as_view() , name = 'Health & safety'),



]
