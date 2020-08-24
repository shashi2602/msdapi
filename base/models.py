from django.db import models

class Personalinfo(models.Model):
    f_name=models.CharField(max_length=200)
    born=models.CharField(max_length=200)
    nickname=models.CharField(max_length=200)
    age=models.CharField(max_length=200)
    batting=models.CharField(max_length=200)
    bowling=models.CharField(max_length=200)
    role=models.CharField(max_length=200)
    teams=models.CharField(max_length=200)
    field_position=models.CharField(max_length=200)
    height=models.CharField(max_length=200)
    man_of_the_matchs=models.CharField(max_length=200)

    def __str__(self):
        return self.f_name

class Internationalinfo(models.Model):
    name=models.ForeignKey(Personalinfo,related_name="international",on_delete=models.CASCADE)
    national_side=models.CharField(max_length=200)
    test_debut=models.CharField(max_length=200)
    last_test=models.CharField(max_length=200)
    ODI_debut=models.CharField(max_length=200)
    last_ODI=models.CharField(max_length=200)
    ODI_shirtno=models.CharField(max_length=200)
    T20I_debut=models.CharField(max_length=200)
    last_T20I=models.CharField(max_length=200)
    T20I_shirtno=models.CharField(max_length=200)

    def __str__(self):
        return "international"

class DomesticInfo(models.Model):
    name=models.ForeignKey(Personalinfo,related_name="domestic",on_delete=models.CASCADE)
    year=models.CharField(max_length=200)
    team=models.CharField(max_length=200)

    def __str__(self):
        return str(self.year)


class Careerstats(models.Model):
    name=models.ForeignKey(Personalinfo,related_name="careerstats",on_delete=models.CASCADE)
    series_name=models.CharField(max_length=200)  
    Matches=models.CharField(max_length=200)    
    Runs_scored=models.CharField(max_length=200)    
    Batting_average=models.CharField(max_length=200)    
    top_100s_50s=models.CharField(max_length=200)    
    Top_score=models.CharField(max_length=200)    
    Balls_bowled=models.CharField(max_length=200)    
    Wickets=models.CharField(max_length=200)      
    Bowling_average=models.CharField(max_length=200)    
    top_5_wickets_in_innings=models.CharField(max_length=200)    
    top_10_wickets_in_match=models.CharField(max_length=200)    
    Best_bowling=models.CharField(max_length=200)    
    Catches_and_stumpings=models.CharField(max_length=200)

    def __str__(self):
        return self.series_name

class Bestperformances(models.Model):
    name=models.ForeignKey(Personalinfo,related_name="bestperformances",on_delete=models.CASCADE)
    year=models.CharField(max_length=200)
    desc=models.TextField(default="")

    def __str__(self):
        return self.year
class BatFiledaverages(models.Model):
    name=models.ForeignKey(Personalinfo,related_name="Battingandfieldingaverages",on_delete=models.CASCADE)
    series_name=models.CharField(max_length=200)
    Mat=models.CharField(max_length=200)
    Inns=models.CharField(max_length=200)
    NO=models.CharField(max_length=200)
    Runs=models.CharField(max_length=200)
    HS=models.CharField(max_length=200)
    Ave	=models.CharField(max_length=200)
    BF=models.CharField(max_length=200)
    SR=models.CharField(max_length=200)
    Best=models.CharField(max_length=200,default="")
    _100=models.CharField(max_length=200)
    _50=models.CharField(max_length=200)
    _4s= models.CharField(max_length=200)
    _6s=models.CharField(max_length=200)
    Ct=models.CharField(max_length=200)
    St=models.CharField(max_length=200)

    def __str__(self):
        return self.series_name

class Bowlingaverages(models.Model):
    name=models.ForeignKey(Personalinfo,related_name="Bowlingaverages",on_delete=models.CASCADE)
    series_name=models.CharField(max_length=200)
    Mat=models.CharField(max_length=200)
    Inns=models.CharField(max_length=200)
    Balls=models.CharField(max_length=200)
    Runs=models.CharField(max_length=200)
    Wkts=models.CharField(max_length=200)
    BBI=models.CharField(max_length=200)
    BBM	=models.CharField(max_length=200)
    Ave=models.CharField(max_length=200)
    Econ=models.CharField(max_length=200)
    SR=models.CharField(max_length=200)
    Best=models.CharField(max_length=200,default="")
    _4w= models.CharField(max_length=200)
    _5w=models.CharField(max_length=200)
    _10=models.CharField(max_length=200)

    def __str__(self):
        return self.series_name

class records(models.Model):
    name=models.ForeignKey(Personalinfo,related_name="internationalrecords",on_delete=models.CASCADE)
    series_name=models.CharField(max_length=200)
    desc=models.TextField(default="")

    def __str__(self):
        return self.series_name
    

class Timeline(models.Model):
    name=models.ForeignKey(Personalinfo,related_name="timeline",on_delete=models.CASCADE)
    date=models.CharField(max_length=100)
    title=models.CharField(max_length=200)
    desc=models.CharField(max_length=1000)
    
    def __str__(self):
        return self.title

class Awards(models.Model):
    name=models.ForeignKey(Personalinfo,related_name="awards",on_delete=models.CASCADE)
    awardname=models.CharField(max_length=200,default="")

    def __str__(self):
        return self.awardname


class honours(models.Model):
    name=models.ForeignKey(Awards,related_name="honours",on_delete=models.CASCADE)
    honour=models.CharField(max_length=1000)
    def __str__(self):
        return self.name.awardname


class OutsideCricketModel(models.Model):
    name=models.ForeignKey(Personalinfo,related_name="Outsidecricket",on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    desc=models.CharField(max_length=1000)

    def __str__(self):
        return self.title

class background(models.Model):
    name=models.ForeignKey(Personalinfo,related_name="background",on_delete=models.CASCADE)
    desc=models.TextField()


class Career(models.Model):
    name=models.ForeignKey(Personalinfo,related_name="career",on_delete=models.CASCADE)
    title=models.CharField(max_length=200,default="")

    def __str__(self):
        return self.title


class careerindex(models.Model):
    name=models.ForeignKey(Career,related_name="careerindex",on_delete=models.CASCADE)
    desc=models.TextField()
    def __str__(self):
        return self.name.title

class Hascaptain(models.Model):
    name=models.ForeignKey(Personalinfo,related_name="hascaptain",on_delete=models.CASCADE)
    desc=models.TextField()

class worldcup(models.Model):
    name=models.ForeignKey(Personalinfo,related_name="worldcup",on_delete=models.CASCADE)
    year=models.CharField(max_length=200)
    desc=models.TextField()


class IPL(models.Model):
    name=models.ForeignKey(Personalinfo,related_name="ipl",on_delete=models.CASCADE)
    desc=models.TextField()

class worldcupscore(models.Model):
    name=models.ForeignKey(Personalinfo,related_name="worldcupscore",on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    def __str__(self):
          return self.title

class wcscores(models.Model):
    wc=models.ForeignKey(worldcupscore,related_name="wcscore",on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    name=models.CharField(max_length=200)
    M=models.CharField(max_length=200)
    I=models.CharField(max_length=200)
    NO=models.CharField(max_length=200)
    R=models.CharField(max_length=200)
    HS=models.CharField(max_length=200)
    _100s=models.CharField(max_length=200)
    _50s=models.CharField(max_length=200)
    _4s6s=models.CharField(max_length=200)
    Avg=models.CharField(max_length=200)
    SR=models.CharField(max_length=200)
    Ct=models.CharField(max_length=200)
    St=models.CharField(max_length=200)

    def __str__(self):
        return self.name


class iplscoremodel(models.Model):
    name=models.ForeignKey(Personalinfo,related_name="inIPL",on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    def __str__(self):
          return self.title

class iplscoresmodel(models.Model):
    wc=models.ForeignKey(iplscoremodel,related_name="msdiplscore",on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    name=models.CharField(max_length=200)
    M=models.CharField(max_length=200)
    I=models.CharField(max_length=200)
    NO=models.CharField(max_length=200)
    R=models.CharField(max_length=200)
    HS=models.CharField(max_length=200)
    _100s=models.CharField(max_length=200)
    _50s=models.CharField(max_length=200)
    _4s6s=models.CharField(max_length=200)
    Avg=models.CharField(max_length=200)
    SR=models.CharField(max_length=200)
    Ct=models.CharField(max_length=200)
    St=models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Recentmatchs(models.Model):
    name=models.ForeignKey(Personalinfo,related_name="recentmatchs",on_delete=models.CASCADE)
    series_name=models.CharField(max_length=200)

    def __str__(self):
        return self.series_name

class Recentmatchdecs(models.Model):
    name=models.ForeignKey(Recentmatchs,related_name="recentm",on_delete=models.CASCADE)
    Batting=models.CharField(max_length=200)
    Bowling=models.CharField(max_length=200)
    Opposition=models.CharField(max_length=200)
    Match_date=models.CharField(max_length=200)

class Retirement(models.Model):
    name=models.ForeignKey(Personalinfo,related_name="retirement",on_delete=models.CASCADE)
    desc=models.CharField(max_length=200)

    def __str__(self):
        return self.desc


class Reference(models.Model):
    name=models.ForeignKey(Personalinfo,related_name="reference",on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    desc=models.CharField(max_length=200)

    def __str__(self):
        return self.title