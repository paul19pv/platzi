from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views
urlpatterns=[
    url(r'^$',views.hello,name='hello'),
    url(r'^login/$',views.authentication,name='authentication'),
    url(r'^logout/$',auth_views.logout,{'next_page':'/'}, name='logout'),
]
