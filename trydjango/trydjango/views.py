""" To rendere html pages"""

from django.http import HttpResponse
from articles.models import Article
from django.template.loader import render_to_string, get_template
import random


def home_view(request):
    name="Raiyan"
    name2 ="Farooqui"
    number= random.randint(1,4)
    articel_obj = Article.objects.get(id=number)
    
    context={
        "object":articel_obj,
        "title":articel_obj.title,
        "id":articel_obj.id,
        "content":articel_obj.content
    }
    

    HTML_STRING= render_to_string('home-view.html',context=context)
    
    # HTML_STRING=f"""
    # <h1>{articel_obj.title} (id: {articel_obj.id})  !</h1>
    # <h1>{articel_obj.content}</h1>
    # """.format(context)
    
    
    return HttpResponse(HTML_STRING)
    