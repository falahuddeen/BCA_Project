from django.conf.urls import url
from awareness import views
urlpatterns=[
    url('post_aware/',views.aware),
    url('view_aware/',views.view_aware)


]