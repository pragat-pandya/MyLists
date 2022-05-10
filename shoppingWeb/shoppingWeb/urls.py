from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('list/', include('list.urls')),
    path('', views.index, name='homepage'),
]
