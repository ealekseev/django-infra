from django.conf.urls import patterns, url

from django_project.infra import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^retailer/$', views.retailer_list, name="retailer_list"),
    url(r'^retailer/(?P<retailer_id>\d+)/$', views.retailer_details, name="retailer_details")
)
