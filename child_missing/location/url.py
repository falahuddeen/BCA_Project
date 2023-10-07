from django.conf.urls import url
from location import views
urlpatterns=[
    url('police_view/',views.police_view),
    url('user_view/', views.user_view),
    url('RFID_loc/',views.police_view_rfid)
]