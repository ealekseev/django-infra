from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.views import generic
from django.forms import ModelForm
from django import forms
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from infra.models import Retailer

# Create your forms

class RetailerSearchForm(ModelForm):
    name = forms.CharField(required=False)
    contract_id = forms.CharField(required=False)
    class Meta:
        model = Retailer
        fields = ['name', 'contract_id']

# Create your views here.

def index(request):
    return HttpResponse("Hello, world! You're at the index.")

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

    paginator = Paginator(retailers, 1)
    page = request.GET.get('page', 1)
    try:
        retailer_list = paginator.page(page)
    except PageNotAnInteger:
        retailer_list = paginator.page(1)
    except EmptyPage:
        retailer_list = paginator.page(paginator.num_pages)

    context = { 'retailers': retailer_list, 'form': form }
    return render(request, 'infra/retailer_list.html', context)

def retailer_details(request, retailer_id):

    retailer = get_object_or_404(Retailer, pk=retailer_id)
    context = { 'retailer': retailer }
    return render(request, 'infra/retailer_details.html', context)

def list_hardware(request):
    return HttpResponse("Here will be list of hardware.")

def list_servers(request):
    return HttpResponse("Here will be list of hardware.")

class RetailerView(generic.DetailView):
    model = Retailer
    template_name = "infra/retailer_details.html"
