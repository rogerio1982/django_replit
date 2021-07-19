from django.shortcuts import render
from blog.models import Project

# Create your views here.
def home(request):
  project = Project.objects.all()
  return render(request, 'index.html', {'projects':project})