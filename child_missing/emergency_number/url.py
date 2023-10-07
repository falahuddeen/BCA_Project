from django.conf.urls import url
from emergency_number import views
urlpatterns=[
    url('emergency/',views.emergency),
    url('user_view/', views.user_view),
    url('android/',views.emg_view.as_view())
]