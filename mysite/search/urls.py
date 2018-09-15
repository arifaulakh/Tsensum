from django.urls import path, include
from search import views
urlpatterns = [
    ##path('', views.index, name = 'index'),
    path('search_form/', views.search_form, name="searchform"),
    path('search/', views.search, name="search"),
    path('', views.index, name="index")
]
