from django.shortcuts import render

# Create your views here.
def search_form(request):
    return render(request,'search/search_form.html')
