from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import requests 
from datetime import datetime



# def hello(request):
#     # return HttpResponse("Hello, world! This is my first Django app.")
#     return HttpResponse("<h1>Hello, world! This is my first Django app.</h1>")

def func(request):
    items = {
        'a': 'apple',
        'b': 'banana',
        'c': 'cherry',
    }
    context = '<h1>Items List</h1>'
    for key, value in items.items():
        context += f'<p>{key}: {value}</p>'
    return HttpResponse(context)

def list_view(request):
    items = ['apple', 'banana', 'cherry']
    context = "<h1>lists Items</h1>"
    for item in items:
        context += f'<p>{item}</p>'
    return HttpResponse(context)


def getval(request, a,b):
    context = f"<h1>Sum: {int(a)+int(b)}</h1>"
    return HttpResponse(context)


def query(request):
    # http://localhost:8000/query/?name=k&rollno=34
    myname = request.GET.get("name")
    rollno = request.GET.get("rollno")
    return HttpResponse(f"<h1>content is: {myname}, {rollno}</h1>")

def jsonVal(request):
    data = {"name":"Aman", "age":34}
    return JsonResponse(data)   #from django.http import JsonResponse



def getAPI(request):
    apiVal = requests.get('https://api.sampleapis.com/coffee/hot')
    data = apiVal.json() 
    return JsonResponse(data, safe=False)  


def first(request):
    return render(request,'first.html')

