from django.shortcuts import render
from django.utils.crypto import get_random_string  #unic name
from django.http import HttpResponse
from django.shortcuts import redirect
from rest_framework.decorators import api_view  # decorator is a function the argument itself function
from rest_framework.response import Response
from .models import short
# Create your views here.

def name1(request):
    url=get_random_string(length=5)
    return HttpResponse(url)

@api_view(['POST'])
def fun(request):
    u=request.data['url']
    v=get_random_string(length=5)
    obj=short(url=u,alfanumeric=v)
    obj.save() #save short url
    return Response(v)

def sample(request,us):
    short_url=us
    data=short.objects.get(alfanumeric=short_url)
   # return HttpResponse(data.url)
    return redirect(data.url)