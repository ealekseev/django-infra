from django.conf.urls import patterns, url
from django.views.generic import TemplateView

from django_project.infra import views

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name="infra/index.html")),
    url(r'^retailer/$', views.retailer_list, name="retailer_list"),
    url(r'^retailer/(?P<pk>\d+)/$', views.RetailerView.as_view(), name="retailer_details"),
    url(r'^hardware/$', views.hardware_list, name="hardware_list"),
    url(r'^hardware/(?P<pk>\d+)/$', views.HardwareView.as_view(), name="hardware_details"),
    url(r'^builds/$', views.build_list, name="build_list"),
    url(r'^builds/(?P<pk>\d+)/$', views.BuildView.as_view(), name="build_details"),
    url(r'^servers/$', views.server_list, name="server_list"),
    url(r'^servers/(?P<pk>\d+)/$', views.ServerView.as_view(), name="server_details"),
)
