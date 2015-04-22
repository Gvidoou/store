from django.conf.urls import patterns, url
from Products import views


urlpatterns = patterns(
    '',
    url(r'^$', views.ProductList.as_view(), name='products_list'),
    url(r'^(?P<slug>[-_\w]+)/$', views.ProductDetailView.as_view(),
        name='product'),
)
