from django.shortcuts import render

# Create your views here.


def projects(request):
    """ a view to return the home page """

    return render(request, 'projects/projects.html')
