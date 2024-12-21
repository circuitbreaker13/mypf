from django.shortcuts import render
from .models import Program
from .models import Feature

# Create your views here.

# Home page view
def home(request):
    return render(request, 'home.html')

# Programs page view
def programs(request):
    programs = Program.objects.all()  # Get all programs from the database
    return render(request, 'programs.html', {'programs': programs})

def programs(request):
    features = Feature.objects.all()

    return render(request, 'programs.html', {'features': features})
# Contact page view
def contact(request):
    return render(request, 'contact.html')
