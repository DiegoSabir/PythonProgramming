from django.shortcuts import render, HttpResponse

#Models
from .models import Project

# Create your views here.
def profile(request):
    
    projects = Project.objects.all()

    return render(request, 'profile.html', {'projects':projects})