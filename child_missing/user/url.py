from django.conf.urls import url
from user import views
urlpatterns=[
    url('user_register/',views.user_register),
    url('mana/',views.admin_verify),
    url('acc/(?P<idd>\w+)', views.approve, name='acc'),
    url('rejj/(?P<idd>\w+)', views.reject, name='rejj'),
]