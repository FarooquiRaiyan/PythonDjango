from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import View , ListView
from tasks.models import Task
from projects.models import Project 
from .models import Profile
# from notifications.models import Notification
from teams.models import Team
from .forms import RegisterForm
from django.contrib.auth.decorators import login_not_required

# class DashboardView(View):
#     def get(self,request,*args, **kwargs):
#         return render(request, "accounts/dashboard.html")


#user Registration
@login_not_required
def RegisterView(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user =form.save()
            messages.success(request,"Registration is succesfull")
            return redirect('login')
        else:
            messages.error(request, "Please enter correct details ") 
    else:
        form=RegisterForm()                   
    return render(request,'registration/register.html', {'form':form})

class DashboardView(View):
    
    def get(self,request,*args, **kwargs):
        latest_project=Project.objects.all()
        latest_tasks=Task.objects.all()
        latest_members=Profile.objects.all()
        
        context={}
        # if request.user.is_authenticated:
        latest_notifications = request.user.notifications.unread(request.user)
        context["latest_notifications"] = latest_notifications[:3]
        context["notification_count"]= latest_notifications.count()
        context["latest_project"]=latest_project[:5]
        context["latest_project_count"]=latest_project.count()
        context["projects_near_due_date"] = latest_project.due_in_two_days_or__less()[:5]
        # context["latest_tasks_count"] = latest_tasks.count()
        context["latest_members"]= latest_members[:8]
        context["latest_members_count"]= latest_members.count()
        context["teams_count"]= Team.objects.count()
        context["header_text"]="Dashboard"
        context["title"]="Dashboard"
        return render(request, "accounts/dashboard.html", context)
    


class MembersListView(ListView):
    model = Profile
    context_object_name ="members"
    template_name= "accounts/profile_list.html"
    paginate_by = 3
    
    def get_context_data(self, **kwargs):
        context = super(MembersListView, self).get_context_data(**kwargs)
        latest_notifications = self.request.user.notifications.unread(self.request.user)
            # latest_notifications = Notification.objects.unread(self.request.user)   
        context["latest_notifications"] = latest_notifications[:3]
        context["notification_count"]= latest_notifications.count()
        context["header_text"]="Members"
        context["title"]="All Members"
        return context