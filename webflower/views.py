from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt

from webflower.models import FlowerPiAddress

import pyjsonrpc
from urllib2 import URLError


def index(request):
    ip_address_list = FlowerPiAddress.objects.all().order_by('-date')
    context = {'ip_address_list': ip_address_list}
    return render(request, 'webflower/index.html', context)


def ip_address(request):
    ip_address = FlowerPiAddress.objects.all().order_by('-date')[0]
    return HttpResponse(ip_address)


def send_ip_address(request):
    return render(request, 'webflower/send_ip_address.html', {})


@csrf_exempt
def update_ip(request):
    try:
        _ip_address = request.POST['ip_address']
    except KeyError:
        return HttpResponse("No IP address")
    else:
        ip = FlowerPiAddress(ip_address=_ip_address, date=timezone.now())
        ip.save()
        return HttpResponseRedirect(reverse('webflower:index'))


def light(request):
    return render(request, 'webflower/light.html', {})


def set_light(request):
    try:
        light = request.POST['light']
    except KeyError:
        return HttpResponse("Wrong request")
    else:
        ip = FlowerPiAddress.objects.all().order_by('-date')[0]
        json_server = "http://{}:8000".format(ip)
        try:
            http_client = pyjsonrpc.HttpClient(url=json_server)
            result = http_client.call("light", light)
        except URLError:
            result = "Server \"{}\" is not responding".format(ip)
        return HttpResponse("Turning light. {}".format(result))
