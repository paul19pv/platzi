from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
urlpatterns=[
    url(r'^$',views.ProductList.as_view(),name='hello'),
    url(r'^product/(?P<pk>[0-9]+)/$',views.ProductDetail.as_view(),name='product_detail'),
    url(r'^product/new$',views.new_product,name='new_product'),
    url(r'^login/$',views.auth_login,name='authentication'),
    url(r'^logout$',auth_views.logout,{'next_page':'/'},name='logout'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
