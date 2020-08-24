from django.shortcuts import render
from django.views.generic import ListView
from rest_framework import generics
from base.models import Personalinfo,Awards,worldcup,IPL,Recentmatchdecs,iplscoresmodel,worldcupscore,Career,Hascaptain,background,OutsideCricketModel,Timeline,Bestperformances,records
from .serializers import msdserializers,awards,careerserliz,recentmmodelserliz,iplserliz,recentmdecserliz,iplscserlize,iplscmodelserliz,worldcupscoreserliz,worldcupserliz,hascaptainserliz,backgroundserliz,outsidecricketserliz,timeline,bestprfms,recordsinfo
from rest_framework.views import APIView
from rest_framework import status,viewsets
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer


class msdapi(generics.ListAPIView,APIView):
    queryset=Personalinfo.objects.all()
    serializer_class=msdserializers

class aws(generics.ListAPIView,APIView):
    queryset=Awards.objects.all()
    serializer_class=awards

class timelines(generics.ListAPIView,APIView):
    queryset=Timeline.objects.all()
    serializer_class=timeline

class bestperformanceView(generics.ListAPIView,APIView):
    queryset=Bestperformances.objects.all()
    serializer_class=bestprfms

class irecordsView(generics.ListAPIView,APIView):
    queryset=records.objects.all()
    serializer_class=recordsinfo

class otView(generics.ListAPIView,APIView):
    queryset=OutsideCricketModel.objects.all()
    serializer_class=outsidecricketserliz

class backgroundView(generics.ListAPIView,APIView):
    queryset=background.objects.all()
    serializer_class=backgroundserliz


class careerView(generics.ListAPIView,APIView):
    queryset=Career.objects.all()
    serializer_class=careerserliz

class ascaptainView(generics.ListAPIView,APIView):
    queryset=Hascaptain.objects.all()
    serializer_class=hascaptainserliz

class wordcupView(generics.ListAPIView,APIView):
    queryset=worldcup.objects.all()
    serializer_class=worldcupserliz

class iplView(generics.ListAPIView,APIView):
    queryset=IPL.objects.all()
    serializer_class=iplserliz

class wcscoreView(generics.ListAPIView,APIView):
    queryset=worldcupscore.objects.all()
    serializer_class=worldcupscoreserliz

class iplscView(generics.ListAPIView,APIView):
    queryset=iplscoresmodel.objects.all()
    serializer_class=iplscmodelserliz

class recentView(generics.ListAPIView,APIView):
    queryset=Recentmatchdecs.objects.all()
    serializer_class=recentmmodelserliz

