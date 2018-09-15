from django.urls import path, include
from search import views
urlpatterns = [
    path('', views.index, name = 'index'),
    path('', views.search_form)
]
