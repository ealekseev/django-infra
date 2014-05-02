from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.views import generic
from django.forms import ModelForm
from django import forms
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from infra.models import *

# Create your forms

class RetailerSearchForm(ModelForm):
    name = forms.CharField(required=False)
    contract_id = forms.CharField(required=False)
    class Meta:
        model = Retailer
        fields = ['name', 'contract_id']

class HardwareSearchForm(ModelForm):
    serial = forms.CharField(required=False)
    hw_type = forms.CharField(required=False)
    class Meta:
        model = Retailer
        fields = ['serial', 'hw_type']

class ServerSearchForm(ModelForm):
    id = forms.IntegerField(required=False)
    mac = forms.CharField(required=False)
    class Meta:
        model = Server
        fields = ['id', 'mac']

class BuildSearchForm(ModelForm):
    name = forms.CharField(required=False)
    class Meta:
        model = Build
        fields = ['name']

class SubnetSearchForm(ModelForm):
    net = forms.CharField(required=False)
    mark = forms.CharField(required=False)
    class Meta:
        model = Subnet
        fields = ['net', 'mark']

class NodeSearchForm(ModelForm):
    hostname = forms.CharField(required=False)
    conf_type = forms.CharField(required=False)
    class Meta:
        model = Node
        fields = ['hostname', 'conf_type']

class IpSearchForm(ModelForm):
    ip = forms.CharField(required=False)
    class Meta:
        model = Ip_address
        fields = ['ip']

# Create your views here.

def retailer_list(request):

    query = {}
    if request.method == 'POST':
        form = RetailerSearchForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['name']:
                query['name__iexact'] = form.cleaned_data['name']
            if form.cleaned_data['contract_id']:
                query['contract_id__iexact'] = form.cleaned_data['contract_id']
    else:
        form = RetailerSearchForm()
    
    if query:
        retailers = Retailer.objects.filter(**query)
    else:
        retailers = Retailer.objects.order_by('id')

    paginator = Paginator(retailers, 25)
    page = request.GET.get('page', 1)
    try:
        retailer_list = paginator.page(page)
    except PageNotAnInteger:
        retailer_list = paginator.page(1)
    except EmptyPage:
        retailer_list = paginator.page(paginator.num_pages)

    context = { 'retailers': retailer_list, 'form': form }
    return render(request, 'infra/retailer_list.html', context)

def hardware_list(request):
    query = {}
    if request.method == 'POST':
        form = HardwareSearchForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['serial']:
                query['serial__iexact'] = form.cleaned_data['serial']
            if form.cleaned_data['hw_type']:
                query['hw_type__iexact'] = form.cleaned_data['hw_type']
    else:
        form = HardwareSearchForm()

    if query:
        hardware = Hardware.objects.filter(**query)
    else:
        hardware = Hardware.objects.order_by('id')

    paginator = Paginator(hardware, 25)
    page = request.GET.get('page', 1)
    try:
        hardware_list = paginator.page(page)
    except PageNotAnInteger:
        hardware_list = paginator.page(1)
    except EmptyPage:
        hardware_list = paginator.page(paginator.num_pages)

    context = { 'hardware': hardware_list, 'form': form }
    return render(request, 'infra/hardware_list.html', context)

def build_list(request):
    query = {}
    if request.method == 'POST':
        form = BuildSearchForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['name']:
                prefix, sep, name = form.cleaned_data['name'].partition('_')
                if name:
                    query['name__icontains'] = name
                    if prefix:
                        query['prefix__iexact'] = prefix
                elif prefix:
                    if sep:
                         query['prefix__iexact'] = prefix
                    else:
                        query['name__icontains'] = prefix
    else:
        form = BuildSearchForm()

    if query:
        build = Build.objects.filter(**query)
    else:
        build = Build.objects.order_by('id')

    paginator = Paginator(build, 25)
    page = request.GET.get('page', 1)
    try:
        build_list = paginator.page(page)
    except PageNotAnInteger:
        build_list = paginator.page(1)
    except EmptyPage:
        build_list = paginator.page(paginator.num_pages)

    context = { 'builds': build_list, 'form': form }
    return render(request, 'infra/build_list.html', context)

def server_list(request):
    query = {}
    if request.method == 'POST':
        form = ServerSearchForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['id']:
                query['id__exact'] = form.cleaned_data['id']
            if form.cleaned_data['mac']:
                query['mac__icontains'] = form.cleaned_data['mac']
    else:
        form = ServerSearchForm()

    if query:
        server = Server.objects.filter(**query)
    else:
        server = Server.objects.order_by('id')

    paginator = Paginator(server, 25)
    page = request.GET.get('page', 1)
    try:
        server_list = paginator.page(page)
    except PageNotAnInteger:
        server_list = paginator.page(1)
    except EmptyPage:
        server_list = paginator.page(paginator.num_pages)

    context = { 'servers': server_list, 'form': form }
    return render(request, 'infra/server_list.html', context)

def subnet_list(request):
    query = {}
    if request.method == 'POST':
        form = SubnetSearchForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['net']:
                query['net__icontains'] = form.cleaned_data['net']
            if form.cleaned_data['mark']:
                query['mark__iexact'] = form.cleaned_data['mark']
    else:
        form = SubnetSearchForm()

    if query:
        subnet = Subnet.objects.filter(**query)
    else:
        subnet = Subnet.objects.order_by('id')

    paginator = Paginator(subnet, 25)
    page = request.GET.get('page', 1)
    try:
        subnet_list = paginator.page(page)
    except PageNotAnInteger:
        subnet_list = paginator.page(1)
    except EmptyPage:
        subnet_list = paginator.page(paginator.num_pages)

    context = { 'subnets': subnet_list, 'form': form }
    return render(request, 'infra/subnet_list.html', context)

def node_list(request):
    query = {}
    if request.method == 'POST':
        form = NodeSearchForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['hostname']:
                query['hostname__icontains'] = form.cleaned_data['hostname']
            if form.cleaned_data['conf_type']:
                query['conf_type__iexact'] = form.cleaned_data['conf_type']
    else:
        form = NodeSearchForm()

    if query:
        node = Node.objects.filter(**query)
    else:
        node = Node.objects.order_by('id')

    paginator = Paginator(node, 25)
    page = request.GET.get('page', 1)
    try:
        node_list = paginator.page(page)
    except PageNotAnInteger:
        node_list = paginator.page(1)
    except EmptyPage:
        node_list = paginator.page(paginator.num_pages)

    context = { 'nodes': node_list, 'form': form }
    return render(request, 'infra/node_list.html', context)

def ip_list(request):
    query = {}
    if request.method == 'POST':
        form = IpSearchForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['ip']:
                query['ip__iexact'] = form.cleaned_data['ip']
    else:
        form = IpSearchForm()

    if query:
        ip = Ip_address.objects.filter(**query)
    else:
        ip = Ip_address.objects.order_by('id')

    paginator = Paginator(ip, 25)
    page = request.GET.get('page', 1)
    try:
        ip_list = paginator.page(page)
    except PageNotAnInteger:
        ip_list = paginator.page(1)
    except EmptyPage:
        ip_list = paginator.page(paginator.num_pages)

    context = { 'ips': ip_list, 'form': form }
    return render(request, 'infra/ip_list.html', context)

# Generic views
class RetailerView(generic.DetailView):
    model = Retailer
    template_name = "infra/retailer_details.html"

class HardwareView(generic.DetailView):
    model = Hardware
    template_name = "infra/hardware_details.html"

class BuildView(generic.DetailView):
    model = Build
    template_name = "infra/build_details.html"

class ServerView(generic.DetailView):
    model = Server
    template_name = "infra/server_details.html"

class SubnetView(generic.DetailView):
    model = Subnet
    template_name = "infra/subnet_details.html"

class NodeView(generic.DetailView):
    model = Node
    template_name = "infra/node_details.html"

class IpView(generic.DetailView):
    model = Ip_address
    template_name = "infra/ip_details.html"

