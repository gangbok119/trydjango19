from django.conf.urls import url
from django.urls import path


from .views import post_home, post_delete, post_update, post_list, post_detail, post_create

urlpatterns = [
    url(r'^$', post_home,),
    url(r'^create/$', post_create,),
    url(r'^detail/(?P<pk>\d+)/$', post_detail,),
    url(r'^list/$', post_list,),
    url(r'^update/$', post_update,),
    url(r'^delete/$', post_delete,),
]
