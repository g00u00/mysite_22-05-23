from django.http import HttpResponse
from django.shortcuts import render


def index(request):
      return render(request, 'mysite/index.html')


# def index(request):
#     return HttpResponse("index(HttpResponse)", status=200)

def index_abc_pk(request, abc, pk):
    # http://127.0.0.1:8000/index_abc_pk/str1/2/
    print (abc)
    print (pk)
    return HttpResponse("index(HttpResponse)", status=200)

def index_abc_pk(request, **kwargs):
    # http://127.0.0.1:8000/index_abc_pk/a/1/?x=1&y=2
    print (kwargs)
    print(kwargs.get('pk'))
    print(request.GET)
    print(request.GET.get('y'))
    return HttpResponse("index(HttpResponse)", status=200)

def index_path(request, path):
    # http://127.0.0.1:8000/index_path/a/1/
    print (path)
    return HttpResponse("index(HttpResponse)", status=200)


# def index(request):
#     return render(request, 'mysite/index.html')

def base(request):
     return render(request, 'mysite/base.html')
