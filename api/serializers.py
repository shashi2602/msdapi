from rest_framework import serializers
from base.models import Retirement,Recentmatchs,Recentmatchdecs,iplscoresmodel,iplscoremodel,worldcupscore,wcscores,IPL,worldcup,Hascaptain,Personalinfo,Internationalinfo,DomesticInfo,Careerstats,Bestperformances,records,BatFiledaverages,Bowlingaverages,Timeline,Awards,honours,OutsideCricketModel,background,Career,careerindex

class internationalif(serializers.ModelSerializer):
    class Meta:
        model=Internationalinfo
        fields="__all__"
        # ["national_side","test_debut","last_test","ODI_debut","last_ODI","ODI_shirtno","T20I_debut","last_T20I","T20I_shirtno"]


class domesticif(serializers.ModelSerializer):
    class Meta:
        model=DomesticInfo
        fields=["year","team"]

class careersts(serializers.ModelSerializer):
    class Meta:
        model=Careerstats
        fields="__all__"
        # ["series_name","Matches","Runs_scored","Batting_average","top_100s_50s","Top_score","Balls_bowled","Wickets","Bowling_average","top_5_wickets_in_innings","top_10_wickets_in_match","Best_bowling","Catches_and_stumpings"]


class bestprfms(serializers.ModelSerializer):
    class Meta:
        model=Bestperformances
        fields=["year","desc"]

class recordsinfo(serializers.ModelSerializer):
    class Meta:
        model=records
        fields=["series_name",'desc']

class bafavg(serializers.ModelSerializer):
    class Meta:
        model=BatFiledaverages
        fields="__all__"
        # ["series_name","Mat","Inns","NO","Runs","HS","Ave","BF","SR","Best","_100","_50","_4s","_6s","Ct","St"]

class bowlingavg(serializers.ModelSerializer):
    class Meta:
        model=Bowlingaverages
        fields="__all__"
        # ["series_name","Mat","Inns","Balls","Runs","Wkts","BBI","BBM","Ave","Econ","SR","Best","_4w","_5w","_10"]

class timeline(serializers.ModelSerializer):
    class Meta:
        model=Timeline
        fields=['date',"title","desc"]

class nationalawards(serializers.ModelSerializer):
    class Meta:
        model=honours
        fields=['honour']

class awards(serializers.ModelSerializer):
    honours=nationalawards(many=True)
    class Meta:
        model=Awards
        fields=["awardname",'honours']
        
class outsidecricketserliz(serializers.ModelSerializer):
    class Meta:
        model=OutsideCricketModel
        fields=['id',"title","desc"]
class backgroundserliz(serializers.ModelSerializer):
    class Meta:
        model=background
        fields=["id","desc"]
class careerindexserliz(serializers.ModelSerializer):
    class Meta:
        model=careerindex
        fields=['id','desc']

class careerserliz(serializers.ModelSerializer):
    careerindex=careerindexserliz(many=True)
    class Meta:
        model=Career
        fields=['title','careerindex']


class hascaptainserliz(serializers.ModelSerializer):
    class Meta:
        model=Hascaptain
        fields=['id','desc']


class worldcupserliz(serializers.ModelSerializer):
    class Meta:
        model=worldcup
        fields=["id","year","desc"]

class iplserliz(serializers.ModelSerializer):
    class Meta:
        model=IPL
        fields=['id','desc']

class wcserlize(serializers.ModelSerializer):
    class Meta:
        model=wcscores
        fields="__all__"
        # ["title","name","M","I","NO","R","HS","_100s","_50s","_4s6s","Avg","SR","Ct","St"]

class worldcupscoreserliz(serializers.ModelSerializer):
    wcscore=wcserlize(many=True)
    class Meta:
        model=worldcupscore
        fields=['title','wcscore']

class iplscserlize(serializers.ModelSerializer):
    class Meta:
        model=iplscoresmodel
        fields="__all__"
        # ["title","name","M","I","NO","R","HS","_100s","_50s","_4s6s","Avg","SR","Ct","St"]

class iplscmodelserliz(serializers.ModelSerializer):
    msdiplscore=iplscserlize(many=True)
    class Meta:
        model=iplscoremodel
        fields=['title','msdiplscore']

class recentmmodelserliz(serializers.ModelSerializer):
    class Meta:
        model=Recentmatchdecs
        fields=["Batting","Bowling","Opposition","Match_date"]
    

class recentmdecserliz(serializers.ModelSerializer):
    recentm=recentmmodelserliz(many=True)
    class Meta:
        model=Recentmatchs
        fields=['series_name',"recentm"]

class retirmentserliz(serializers.ModelSerializer):
    class Meta:
        model=Retirement
        fields=['desc']
class msdserializers(serializers.ModelSerializer):
    international=internationalif(many=True)
    domestic=domesticif(many=True)
    careerstats=careersts(many=True)
    bestperformances=bestprfms(many=True)
    internationalrecords=recordsinfo(many=True)
    Battingandfieldingaverages=bafavg(many=True)
    Bowlingaverages=bowlingavg(many=True)
    timeline=timeline(many=True)
    awards=awards(many=True)
    Outsidecricket=outsidecricketserliz(many=True)
    background=backgroundserliz(many=True)
    career=careerserliz(many=True)
    hascaptain=hascaptainserliz(many=True)
    worldcup=worldcupserliz(many=True)
    ipl=iplserliz(many=True)
    worldcupscore=worldcupscoreserliz(many=True)
    inIPL=iplscmodelserliz(many=True)
    recentmatchs=recentmdecserliz(many=True)
    retirement=retirmentserliz(many=True)
    class Meta:
        model=Personalinfo
        fields=['f_name','nickname',"born","age","batting","bowling","height","role","teams","field_position","man_of_the_matchs","international","domestic","careerstats",'bestperformances',"internationalrecords","Battingandfieldingaverages","Bowlingaverages","timeline","awards","Outsidecricket","background","career","hascaptain","worldcup",'ipl',"worldcupscore","inIPL","recentmatchs","retirement"]