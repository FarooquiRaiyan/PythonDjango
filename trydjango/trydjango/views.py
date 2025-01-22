""" To rendere html pages"""

from django.http import HttpResponse
from articles.models import Article
from django.template.loader import render_to_string, get_template
import random


def home_view(request,id=None,*args, **kwargs):
    print(args, kwargs)
    name="Raiyan"
    name2 ="Farooqui"
    number= random.randint(1,4)
    article_obj = Article.objects.get(id=number)
    article_queryset = Article.objects.all()
    

    
    context={
        "object_list":article_queryset,
        "object":article_obj,
        "title":article_obj.title,
        "id":article_obj.id,
        "content":article_obj.content
    }
    

    HTML_STRING= render_to_string('home-view.html',context=context)
    
    # HTML_STRING=f"""
    # <h1>{article_obj.title} (id: {article_obj.id})  !</h1>
    # <h1>{article_obj.content}</h1>
    # """.format(context)
    
    
    return HttpResponse(HTML_STRING)
    