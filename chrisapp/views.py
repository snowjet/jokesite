# Create your views here.

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import loader
import logging
import sys
from .forms import JokeForm
from .models import Joke


def index(request):
    joke_list = Joke.objects.order_by('-joke_text')[:5]
    context = {'joke_list': joke_list}
    return render(request, 'chrisapp/index.html', context)
   

def detail(request, joke_id):
    joke = get_object_or_404(Joke, pk=joke_id)  
    return render(request, 'chrisapp/detail.html', {'joke': joke})
     
def add(request):
    print('add called')
    if request.method == 'POST':
        
        # create a form instance and populate it with data from the request:    
        print('request method=POST')

        form = JokeForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # 
            form.save()
            # redirect to main:
            print('form is valid!')
            return HttpResponseRedirect('/chrisapp/')

    # if a GET (or any other method) we'll create a blank form
    else:
        print('else case')
        form = JokeForm()

    return render(request, 'chrisapp/add.html', {'form': form})


