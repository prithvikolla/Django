from django.shortcuts import render, get_object_or_404
from .models import Experience
# Create your views here.
def home(request):
    experiences = Experience.objects
    return render(request,'Experience/home.html', {'experiences': experiences})

def detail(request,experience_id):
    experience_detail = get_object_or_404(Experience,pk = experience_id)
    return render(request,'Experience/detail.html', {'experience':experience_detail})
