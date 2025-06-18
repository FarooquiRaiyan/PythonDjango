from home.views import index
from django.urls import path
from home.views import person

urlpatterns = [
    path('index/', index),
    path('person/',person)
]
