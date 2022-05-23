from django.http import HttpResponse
from django.shortcuts import render


def index(request):
      return render(request, 'mysite/index.html')


def index(request):
    return HttpResponse("index(HttpResponse)", status=200)

# def index_abc_pk(request, abc, pk):
#     print ( abc, pk)
#     return HttpResponse("index(HttpResponse)", status=200)

def index_abc_pk(request, **kwargs):
    print (kwargs)
    print(request.GET)
    return HttpResponse("index(HttpResponse)", status=200)

def index_path(request, path):
    print (path)
    return HttpResponse("index(HttpResponse)", status=200)


# def index(request):
#     return render(request, 'mysite/index.html')

def base(request):
     return render(request, 'mysite/base.html')
