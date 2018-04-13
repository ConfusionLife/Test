from django.shortcuts import render,HttpResponse
from . import models
# Create your views here.


def index(request):
    if request.method == 'OPTIONS':
        print(111)
        obj = HttpResponse()
        obj['Access-Control-Allow-Origin'] = 'http://localhost:63342'
        obj['Access-Control-Allow-Headers'] = 'k1'
        return obj
    v1 = request.GET.get('v1')
    v2 = request.GET.get('v2')
    result = v1 + v2
    obj = HttpResponse(result)
    obj['Access-Control-Allow-Origin'] = 'http://localhost:63342'
    return obj