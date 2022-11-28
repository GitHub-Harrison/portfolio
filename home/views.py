from django.shortcuts import render

# Create your views here.


def index(request):
    """ a view to return the home page """

    return render(request, 'home/index.html')
