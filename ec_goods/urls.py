# -*-coding:utf-8-*-

from django.conf.urls import url
from ec_goods import views

urlpatterns = [
    url(r'^$', views.home_list_page),
    url(r'^goods/(?P<goods_id>\d+)/$', views.goods_detail),
    url(r'^list/(?P<goods_type_id>\d+)/(?P<pindex>\d+)/$', views.goods_list),
]
# urlpatterns = [
#     url('^$', views.index),
#     url('^list(\d+)_(\d+)_(\d+)/$', views.list),
#     url('^(\d+)/$', views.detail),
# ]