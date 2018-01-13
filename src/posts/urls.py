from django.conf.urls import url
from django.urls import path


from .views import post_home, post_delete, post_update, post_list, post_detail, post_create

urlpatterns = [
    url(r'^$', post_home,),
    url(r'^create/$', post_create,),
    url(r'^(?P<pk>\d+)/$', post_detail,name='detail'),
    url(r'^list/$', post_list,name='list'),
    url(r'^(?P<pk>\d+)/update/$', post_update,name='update'),
    url(r'^(?P<pk>\d+)/delete/$', post_delete,),
]
