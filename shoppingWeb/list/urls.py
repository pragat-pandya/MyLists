from django.urls import path
from . import views

urlpatterns = [
    path('', views.lists, name='lists'),
    path('my-lists/', views.my_lists, name='myLists'),
    path('<str:list_name>/', views.list_view, name="theList")
]
