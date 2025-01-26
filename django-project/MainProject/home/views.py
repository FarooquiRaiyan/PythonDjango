from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    people=[
        {'name':"raiyan",'age':110},
        {'name':"aman",'age':120},
        {'name':"rehan",'age':130},
    ]
    return render (request,'index.html',context={"people":people})
    # return HttpResponse("This is homepage")
    
    
def about(request):
    # return HttpResponse("This is about page")      
    return render (request,'aboutus.html')
    
def service(request):
    # return HttpResponse("This is seicerv ")
    return render (request,'service.html')

def contact(request):
    # return HttpResponse("This is seicerv ")
    return render (request,'contact.html')
