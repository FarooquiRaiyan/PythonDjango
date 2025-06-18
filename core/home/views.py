from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Person
from .serializers import PeopleSerializer


# @api_view(['GET','POST',"PUT"])
# def index(request):
#     courses={
#                 'course_name':'Python',
#                 'learn':['flask','django','Tornado','FastApi'],
#                 'course_provider':'scaler'
#                 }
#     if request.method =="GET":
#         print("You hit a GET method")
#         return Response(courses)
#     elif request.method =="POST":
#         data = request.data
#         print("****")
#         print(data)
#         print("****")
#         print("You hit a POST method")
#         return Response(courses)
#     elif request.method == "PUT":
#         print("You hit a PUT method")
#         return Response(courses)
        
@api_view(['GET','POST'])
def index(request):
    if request.method == "GET":
        json_response={
            'name':'Scaler',
            'courses':['C++','Python'],
            'method':'GET'
        }
    else:
        data = request.data
        print(data)
        json_response={
            'name':'Scaler',
            'courses':['C++','Python'],
            'method':'POST'
        }
        
    return Response(json_response)


@api_view(['GET','POSt'])
def person(request):
    if request.method=='GET':
        objs=Person.objects.all()
        serializer = PeopleSerializer(objs,many=True)
        return Response(serializer.data)
    else:
        data = request.data
        serializer = PeopleSerializer(data = data)
        if serializer.is_valid():
            return Response(serializer.data)
        
        return Response(serializer.errors)
        
        
    
                                                                    