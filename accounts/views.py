from django.shortcuts import render
from django.views.generic import View
from tasks.models import Task
from projects.models import Project
from .models import Profile
from notifications.models import Notification
# class DashboardView(View):
#     def get(self,request,*args, **kwargs):
#         return render(request, "accounts/dashboard.html")


class DashboardView(View):
    def get(self,request,*args, **kwargs):
        latest_project=Project.objects.all()[:5]
        latest_tasks=Task.objects.all()[:5]
        latest_members=Profile.objects.all()[:8]
        latest_notifications = Notification.objects.for_user(request.user)
        context={}
        context["latest_project"]=latest_project
        context["latest_tasks"] = latest_tasks
        context["latest_members"]= latest_members
        context["latest_notifications"] = latest_notifications[:3]
        context["notification_count"]= latest_notifications.count()
        print(latest_members)
        return render(request, "accounts/dashboard.html", context)