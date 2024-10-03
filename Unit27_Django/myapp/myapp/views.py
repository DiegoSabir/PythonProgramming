from django.http import HttpResponse

def hola(request):
    print(request)
    print(request.GET)
    return HttpResponse(request.GET['numeros'])