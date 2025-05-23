from django.urls import path
from .views import update_task_status_ajax, create_task_ajax

app_name ="tasks"

urlpatterns=[
     path('create-task/', create_task_ajax, name='create_task_ajax'),
    path('update-task-status/<uuid:task_id>/', update_task_status_ajax, name='update_task_status_ajax'),
    
    
    
]