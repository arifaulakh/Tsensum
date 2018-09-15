from django.urls import path, include
from search import views
urlpatterns = [
    ##path('', views.index, name = 'index'),
    path('search_form/', views.search_form),
    path('search/', views.search)
]
