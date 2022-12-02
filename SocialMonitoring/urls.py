from django.urls import path
from .views import PapView , RehabilationView , CompensationView ,CompensationListView, constructionSiteView , LabourCampDetailsView , labourcampListView

urlpatterns = [
path ('pap' , PapView.as_view() , name = "project affected Person "),
    path ('rehabilation' , RehabilationView.as_view() , name = "rehabilation"),
    path ('Compensation' , CompensationView.as_view() , name = "CompensationView"),
    path ('CompensationList' , CompensationListView.as_view() , name = "CompensationView List"),

    path ('constructionsite' , constructionSiteView.as_view() , name = "constructionSiteView"),
    path ('labourcamp' , LabourCampDetailsView.as_view() , name = "LabourCampDetailsView"),
    path ('labourcampList' , labourcampListView.as_view() , name = "LabourCampDetail List "),
    


]