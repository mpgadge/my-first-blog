from django.shortcuts import render


def home(request):
   return render(request,'client_console/home.html',{})
