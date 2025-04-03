from django.shortcuts import render
from django.views.generic import View
# Create your views here.

from projects.models import Project
# class DashboardView(View):
#     def get(self,request,*args, **kwargs):
#         return render(request, "accounts/dashboard.html")
    

class DashboardView(View):
    def get(self,request,*args, **kwargs):
        latest_project=Project.objects.all()[:5]
        context={}
        context["latest_project"]=latest_project
        return render(request, "accounts/dashboard.html", context)