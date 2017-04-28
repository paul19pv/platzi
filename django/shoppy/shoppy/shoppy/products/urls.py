from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns=[
    url(r'^$',views.hello_world,name='hello'),
    url(r'^product/(?P<pk>[0-9]+)/$',views.product_detail,name='product_detail'),
    url(r'^product/new',views.new_product,name='new_product')
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
