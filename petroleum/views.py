from django.shortcuts import render

# Create your views here.

def index(request):
    context = {'var': 'foo'}
    return render(request, 'petroleum/index.html', context)