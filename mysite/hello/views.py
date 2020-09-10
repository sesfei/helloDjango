from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("テスト")

def getUser(request, id):
    return HttpResponse("ユーザID：%s" % id)

def listUser(request):
    return HttpResponse("ユーザID：%s" % id)