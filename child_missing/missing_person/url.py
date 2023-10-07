from django.conf.urls import url
from missing_person import views
urlpatterns=[
    url('user_inform/',views.user_inform),
    url('inform/(?P<idd>\w+)', views.inform,name='inform'),
]