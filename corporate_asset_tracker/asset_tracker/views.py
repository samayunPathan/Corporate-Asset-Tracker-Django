from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def asset(request):
    html = "<html><body>It is now.</body></html>" 
    return HttpResponse(html)