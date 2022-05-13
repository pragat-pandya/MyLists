from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('lists/', include('list.urls')),
    path('', views.index, name='homepage'),
    path('accounts/', include('accounts.urls')),
    path('forgot-password/', views.forgotPassword, name='forgotPassword'),
    path('tutorial/', views.tutorial, name='tellMeMore'),
    path('chats/', include ('chats.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
