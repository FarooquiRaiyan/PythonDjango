from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Students
from .forms import studentForm
# Create your views here.

def home(request):
    if request.method == 'POST':
        form = studentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = studentForm()
    search_query = request.GET.get('q', '')   # get search term
    if search_query:
        students = Students.objects.filter(
            name__icontains=search_query
        ) | Students.objects.filter(
            email__icontains=search_query
        ) | Students.objects.filter(
            roll__icontains=search_query
        ) | Students.objects.filter(
            fav_sub__icontains=search_query
        )
    else:
        students = Students.objects.all()
        
    context = {
        'form': form,
        'students': students,
        'search_query': search_query,
    }
    return render(request,'formsapps/home.html', context)