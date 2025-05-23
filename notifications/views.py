from django.shortcuts import render, redirect
from django.views.generic import ListView, View
from .models import Notification


# Create your views here.
class MarknotificationAsRead(View):
    def post(self, request, notification_id):
        #get notifications
        notification = Notification.objects.get(id=notification_id)
        notification.mark_as_read()
        return redirect("notifications:notification-list")


class NotificationListView(ListView):
    model = Notification
    context_object_name ="notifications"
    template_name= "notification/notification_list.html"
    paginate_by = 10
    
    def get_queryset(self):
        return self.request.user.notifications.unread(self.request.user)
    
    def get_context_data(self, **kwargs):
        context = super(NotificationListView, self).get_context_data(**kwargs)
        latest_notifications = self.request.user.notifications.unread(self.request.user)
            # latest_notifications = Notification.objects.unread(self.request.user)   
        context["latest_notifications"] = latest_notifications[:3]
        context["notification_count"]= latest_notifications.count()
        context["header_text"]="Notifications"
        context["title"]="All Notifications"
        return context