from django.shortcuts import render,redirect
from .models import Neighborhood, Profile, Post, Business
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
@login_required(login_url='/accounts/login')
def home(request):
    current_user = request.user
    hoods = Neighborhood.objects.all()
    profile = Profile.objects.all()
    print(profile)
    return render(request, 'index.html',{'hoods':hoods})

@login_required(login_url='/accounts/login')
def profile(request,id):
    current_user = request.user
    user = User.objects.get(id=id)
    hoods = Neighborhood.filter(id=id)
    posts = Post.obbjects.filter(user_id=id)
    try:
        profile = Profile.objects.get(user_id=id)
    except ObjectDoesNotExist:
        return redirect(update_profile, current_user.id)
    else:

        return render(request, 'profile.html', {"user": user, "profile": profile, 'hoods': hoods, "posts": posts})




