from django.shortcuts import render
from .models import Article
# Create your views here.


def article_search_return(request):
    # print("dirececorty request",dir(request))
    print(request.GET)
    query=request.GET #this is dict
    print(" query",query)
    # queryid=query.get('query')
    # print("queryid",queryid)
    try:
        queryid=int(query.get('query'))
    except:
        queryid=None
        print("cames in exception as query not prcosessd")
    article_obj=None
    if queryid is not None:
        article_obj=Article.objects.get(id=queryid)
    context={
        "object":article_obj
    }
    return render(request,"articles/search.html",context=context)

def article_detail_view(request, id=None):
    article_obj=None
    if id is not None:
        article_obj = Article.objects.get(id=id)
    context ={
        "object":article_obj,
    }
    return render(request, "articles/detail.html", context=context)