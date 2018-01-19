from django.conf.urls import url
from django.urls import path


from .views import post_home, post_delete, post_update, post_list, post_detail, post_create

urlpatterns = [

    url(r'^create/$', post_create,),
    url(r'^(?P<slug>[\w-]+)/$', post_detail,name='detail'),
    url(r'^$', post_list,name='list'),
    url(r'^(?P<slug>[\w-]+)/update/$', post_update,name='update'),
    url(r'^(?P<slug>[\w-]+)/delete/$', post_delete,),
]
