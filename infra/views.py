from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.views import generic

from infra.models import Retailer

# Create your views here.

def index(request):
    return HttpResponse("Hello, world! You're at the index.")

def retailer_list(request):

    retailers = Retailer.objects.order_by('id')
    context = { 'retailers': retailers }
    return render(request, 'infra/index.html', context)

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
