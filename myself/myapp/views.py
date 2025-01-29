from django.shortcuts import render
from django.template import loader
# Create your views here.
from django.shortcuts import HttpResponse
from .import views
import re
import requests

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())