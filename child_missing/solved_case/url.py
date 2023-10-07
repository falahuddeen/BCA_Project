from django.conf.urls import url
from solved_case import views
urlpatterns=[
    url('admin_view/',views.admin_view)
]