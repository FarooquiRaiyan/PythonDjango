from django.shortcuts import render
from django.views.decorators.http import require_POST
import json
from django.http import JsonResponse
from .models import Task
from projects.models import Project
from django.core.mail import send_mail



@require_POST
def update_task_status_ajax(request, task_id):
    try:
        task = Task.objects.get(id=task_id)
        data = json.loads(request.body)
        new_status = data.get('status').title()
        
        if new_status in ['Backlog', 'To Do', 'In Progress', 'Completed']:
            old_status = task.status
            task.status = new_status
            task.save()

            # Send email notification if the email is set
            if task.email:
                subject = f"Task '{task.name}' Status Updated"
                message = f"The task '{task.name}' has been moved from '{old_status}' to '{new_status}'."
                recipient_list = [task.email]

                send_mail(
                    subject,
                    message,
                    None,  # From email (uses DEFAULT_FROM_EMAIL)
                    recipient_list,
                    fail_silently=False,
                )
                print("message sent")
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'error': 'Invalid status'}, status=400)

    except Task.DoesNotExist:
        return JsonResponse({'success': False, 'error': 'Task not found'}, status=404)



@require_POST 
def create_task_ajax(request):
    name = request.POST.get('name')
    email = request.POST.get('email') or user.email  # ← NEW
    project_id = request.POST.get('project_id')
    user = request.user

    if not name:
        return JsonResponse({'success': False, 'error': 'Task title is required'})
    if not project_id:
        return JsonResponse({'success': False, 'error': 'Project ID is required'})

    try:
        project = Project.objects.get(id=project_id)

        # Create new task with optional email
        new_task = Task.objects.create(
            name=name,
            project=project,
            owner=user,
            email=email  # ← Save email here
        )

        return JsonResponse({'success': True, 'task_id': str(new_task.id)})
    except Project.DoesNotExist:
        return JsonResponse({'success': False, 'error': 'Project not found'})
