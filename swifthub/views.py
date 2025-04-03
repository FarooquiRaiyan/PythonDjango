from django.http import HttpResponse


def DashboardView(request):
    return HttpResponse("<h1>Welcome to Projects ")