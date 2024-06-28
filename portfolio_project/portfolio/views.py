from django.shortcuts import render
from .models import Education, Skill, Experience, Project

def home(request):
    education = Education.objects.all()
    skills = Skill.objects.all()
    experiences = Experience.objects.all()
    projects = Project.objects.all()

    context = {
        'education': education,
        'skills': skills,
        'experiences': experiences,
        'projects': projects,
    }
    return render(request, 'portfolio/home.html', context)
