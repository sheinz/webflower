from django.shortcuts import render
from django.http import HttpResponse

from webflower.models import FlowerPiAddress


def index(request):
    ip_address_list = FlowerPiAddress.objects.all().order_by('-date')
    context = {'ip_address_list': ip_address_list}
    return render(request, 'webflower/index.html', context)

def ip_address(request):
    ip_address = FlowerPiAddress.objects.all().order_by('-date')[0]
    return HttpResponse(ip_address)
