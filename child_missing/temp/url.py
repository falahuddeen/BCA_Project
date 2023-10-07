from django.conf.urls import url
from temp import views
urlpatterns=[
    url('',views.main_home),
    url('admin_home/', views.admin_home),
    url('main_home/', views.main_home),
    url('police_station_home/', views.police_station_home),
    url('user_home/',views.user_home)
]