from django.shortcuts import render
from .models import Article
from django.contrib.auth.decorators import login_required
# Create your views here.

from .forms import ArticleForm

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


@login_required
def article_create_view(request):
    form=ArticleForm()
    print(dir(form))
    context={
        "form":form
    }
    if request.method=="POST":
        form=ArticleForm(request.POST)
        if form.is_valid():
            print(request.POST)
            title=form.cleaned_data.get('title')
            content=form.cleaned_data.get('content')
            print(title,content)
            article_object=Article.objects.create(title=title,content=content)
            context['object']=article_object
            context['created']=True 
    return render(request, "articles/create.html", context=context)