from django.urls import path
from .views import PapView , RehabilationView , CompensationView , constructionSiteView , LabourCampDetailsView

urlpatterns = [
path ('pap' , PapView.as_view() , name = "project affected Person "),
    path ('rehabilation' , RehabilationView.as_view() , name = "rehabilation"),
    path ('Compensation' , CompensationView.as_view() , name = "CompensationView"),
    path ('constructionsite' , constructionSiteView.as_view() , name = "constructionSiteView"),
    path ('labourcamp' , LabourCampDetailsView.as_view() , name = "LabourCampDetailsView"),
    


]