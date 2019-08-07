from django.shortcuts import render
from .models import Neighborhood, Profile, Post, Business
from django.contrib.auth.models import User

# Create your views here.
@login_required(login_url='/accounts/login')
def home(request):
    current_user = request.user
    hoods = Neighborhood.objects.all()
    profile = Profile.objects.all()
    print(profile)
    return render(request, 'index.html',{'hoods':hoods})


