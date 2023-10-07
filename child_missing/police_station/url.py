from django.conf.urls import url
from police_station import views
urlpatterns=[
    url('admin_verify/',views.admin_verify),
    url('police_register/', views.police_register),
    url('accept/(?P<idd>\w+)', views.accept,name='accept'),
    url('reject/(?P<idd>\w+)', views.reject,name='reject'),

]