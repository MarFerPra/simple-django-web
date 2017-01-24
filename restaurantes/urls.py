from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^test/$', views.test, name='test'),
    url(r'^create_restaurant/$', views.create_restaurant, name='create_restaurant'),
]
