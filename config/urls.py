"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from pybo.views import base_views
# from pybo import views

urlpatterns = [
    # path('', views.index),
    # path('', views.djangoindex),
    path('admin/', admin.site.urls),
    path('pybo/', include('pybo.urls')),
    path('encore/', include('encore.urls')),
    path('polls/', include('polls.urls')),
    path('common/', include('common.urls')),
    path('', base_views.index, name="index"), # / 페이지에 해당하는 urlpatterns
]
