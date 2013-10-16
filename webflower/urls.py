from django.conf.urls import patterns, url

from webflower import views


urlpatterns = patterns(
    '',
    url(r'^$', views.index, name='index'),
    url(r'^ip_address/$', views.ip_address, name='ip_address'),
    url(r'^send_ip_address/$', views.send_ip_address, name='send_ip_address'),
    url(r'^update_ip/$', views.update_ip, name='update_ip'),
)
