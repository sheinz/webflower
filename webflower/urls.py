from django.conf.urls import patterns, url

from webflower import views


urlpatterns = patterns(
    '',
    url(r'^$', views.index, name='index'),
    url(r'^ip_address/$', views.ip_address, name='ip_address'),
)
