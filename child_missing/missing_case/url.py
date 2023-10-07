from django.conf.urls import url
from missing_case import views
urlpatterns=[
    url('admin_missing/',views.admin_missing),
    url('admin_view/', views.admin_view),
    url('police_verify/', views.police_verify),
    url('police_view/', views.police_view),
    url('register_missing/', views.register_missing),
    url('user_view_case/', views.user_view_case),
    url('user_view_missing/', views.user_view_missing),
    url('verify/(?P<idd>\w+)', views.verify,name='verify'),
    url('decline/(?P<idd>\w+)', views.decline,name='decline'),
    url('solved/(?P<idd>\w+)', views.solved,name='solved'),
    url('ongoing/(?P<idd>\w+)', views.ongoing,name='ongoing'),
    url('simple_upload/',views.simple_upload),
    url('^android/',views.emg_view.as_view()),
    url('solve1/(?P<idd>\w+)', views.solve,name='solve'),
    # url('solve/', views.solve),
    url('pp/', views.Police_view_and_solve),
]