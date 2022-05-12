from django.urls import path
from . import views

urlpatterns = [
    path('my-messages/', views.my_messages, name='messages')
]
