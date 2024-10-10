from django.shortcuts import render

# Create your views here.
def list_carros(request):
    return render(request, 'list_carros.html')
