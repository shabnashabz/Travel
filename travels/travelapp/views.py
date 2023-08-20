from django.http import HttpResponse
from django.shortcuts import render

from .models import place
from .models import photo

# Create your views here.
def demo(request):
    # return HttpResponse("hello world")
    newvrbl=place.objects.all()
    newvrbls=photo.objects.all()
    return render(request,"index.html",{'result':newvrbl,'results':newvrbls})
# def contact(request):
#      return HttpResponse("hello world")
# def addition(request):
#     # return HttpResponse("hello world")
#     x=int(request.GET['num1'])
#     y=int(request.GET['num2'])
#     res=x+y
#     ress=x-y
#     rest=x*y
#     restl=x/y
#     return render(request,"result.html",{'result': res, 'resul': ress, 'results': rest, 'resuls': restl})
   