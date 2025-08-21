from django.http import HttpResponse, JsonResponse

def myHandler(request, exception):
    return HttpResponse("<h1>Page not found</h1>", status=404)
