from django.shortcuts import render
from django.http import HttpResponse
from .keywords import get_graph
# Create your views here.
def search_form(request):
    return render(request,'search/search_form.html')

def index(request):
    return render(request, 'search/index.html')

def search(request):
    if 'q' in request.GET:
        m = 'You searched for: %r' % request.GET['q']
    else:
        m = 'You submitted an empty form.'
    tweet = request.GET['q']
    graph = get_graph(tweet)
    message = 'It works!'
    return HttpResponse(message)
