from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def search_form(request):
    return render(request,'search/search_form.html')

def index(request):
    return render(request, 'search/index.html')

def search(request):
    if 'q' in request.GET:
        message = 'You searched for: %r' % request.GET['q']
    else:
        mesage = 'You submitted an empty form.'
    return HttpResponse(message)