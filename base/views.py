from django.shortcuts import render
def  Home(request):
   return render(request,template_name="base/home.html")