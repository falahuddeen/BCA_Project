from django.conf.urls import url
from complaints import views
urlpatterns=[
    # url('post_replay/',views.post_replay),
    url('police_view/', views.police_view),
    url('post_complaint/(?P<idd>\w+)', views.post_complaint,name='postcomp'),
    url('user_view/(?P<idd>\w+)', views.user_view,name='user_view'),
    url('post_replay/(?P<idd>\w+)',views.post_replay,name='post_replay'),
    # url('rep/',views.post_replay)
]