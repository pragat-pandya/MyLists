from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('list/', include('list.urls')),
    path('', views.index, name='homepage'),
    path('accounts/', include('accounts.urls')),
    path('forgot-password/', views.forgotPassword, name='forgotPassword'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
