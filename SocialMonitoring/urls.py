from django.urls import path
from .views import ( PapView , constructionSiteView ,
 LabourCampDetailsView , labourcampListView ,
 ConstructionSiteListView,)

urlpatterns = [
    path ('pap' , PapView.as_view() , name = "project affected Person "),
    # path ('pap/<int:id>' , papupdateView.as_view() , name = "project affected Person "),
    # path ('paplist' , PapListView.as_view() , name = "project affected Person List "),

    # path ('rehabilation' , RehabilationView.as_view() , name = "rehabilation"),
    # path ('rehabilationList' , RehabilationListView.as_view() , name = "rehabilation"),
    # path ('rehabilationUpdate/<int:id>' , RehabilationUpdateView.as_view() , name = "rehabilation update"),

    # path ('Compensation' , CompensationView.as_view() , name = "CompensationView"),
    # path ('CompensationList' , CompensationListView.as_view() , name = "CompensationView List"),
    # path ('Compensationupdate/<int:id>' , CompensationUpdateView.as_view() , name = "CompensationView List"),


    path ('constructionsite' , constructionSiteView.as_view() , name = "constructionSiteView"),
    path ('constructionsiteList' , ConstructionSiteListView.as_view() , name = "ConstructionSiteListView"),

    path ('labourcamp' , LabourCampDetailsView.as_view() , name = "LabourCampDetailsView"),
    path ('labourcampList' , labourcampListView.as_view() , name = "LabourCampDetail List "),
    # path ('testview' , testview.as_view() , name = "testview  "),
    


]