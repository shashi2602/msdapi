from django.urls import path
from .views import msdapi,aws,timelines,otView,recentView,iplView,wordcupView,iplscView,wordcupView,ascaptainView,careerView,backgroundView,bestperformanceView,irecordsView


urlpatterns=[
    path("",msdapi.as_view()),
    path("awards",aws.as_view()),
    path("timeline",timelines.as_view()),
    path("bestperformance",bestperformanceView.as_view()),
    path("ir",irecordsView.as_view()),
    path("outside",otView.as_view()),
    path("background",backgroundView.as_view()),
    path("career",careerView.as_view()),
    path("ascaptain",ascaptainView.as_view()),
    path("worldcup",wordcupView.as_view()),
    path("ipl",iplView.as_view()),
    path("worldcup/score",wordcupView.as_view()),
    path("ipl/score",iplscView.as_view()),
    path("recentmatchs",recentView.as_view())

]