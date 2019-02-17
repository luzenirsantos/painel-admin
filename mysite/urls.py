from django.contrib import admin
from django.urls import path
from django.urls.conf import include

urlpatterns = [
    path('', include('loja.urls', namespace='loja')),

    path('admin/', admin.site.urls),
]