from django.conf.urls import patterns, url

from django_project.infra import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^retailer/$', views.retailer_list, name="retailer_list"),
    url(r'^retailer/(?P<pk>\d+)/$', views.RetailerView.as_view(), name="retailer_details")
)
