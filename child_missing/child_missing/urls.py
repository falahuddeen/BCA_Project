"""child_missing URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from django.conf.urls import url,include
urlpatterns = [
    path('admin/', admin.site.urls),
    url('aware/',include('awareness.url')),
    url('compl/',include('complaints.url')),
    url('emer/', include('emergency_number.url')),
    url('loca/', include('location.url')),
    url('login/', include('login.url')),
    url('missing_ca/', include('missing_case.url')),
    url('missing_pe/', include('missing_person.url')),
    url('police_station/', include('police_station.url')),
    url('solved/', include('solved_case.url')),
    url('user/', include('user.url')),
    url('temp/', include('temp.url')),
    url('',include('temp.url'))
]
