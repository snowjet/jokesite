# Create your views here.

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import loader
from .models import Joke


def index(request):
    joke_list = Joke.objects.order_by('-joke_text')[:5]
    context = {'joke_list': joke_list}
    return render(request, 'chrisapp/index.html', context)
   

def detail(request, joke_id):
    joke = get_object_or_404(Joke, pk=joke_id)
    
    return render(request, 'chrisapp/detail.html', {'joke': joke})
   
def add(request):
    return render(request, 'chrisapp/add.html')

#def index(request):
#    return HttpResponse("""
#    
#    <html>
#    <head>
#        <title>Chris' App</title>
#        <link rel="stylesheet" href="{% static 'css/chrisapp.css' %}">
#    </head>
#    <body>
#    <h1>Hello, world. You're at the fantastic chrisapp index.</h1>
#""")