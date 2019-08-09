from django import forms
from .models import Profile, Neighborhood, Business, Post
from django.contrib.auth.models import User



class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_pic', 'bio']


class NeighborhoodForm(forms.ModelForm):

    class Meta:
        model = Neighborhood
        fields = ['name', 'location', 'police', 'police_department_address',
                  'health', 'health_department_address']

class BusinessForm(forms.ModelForm):
    class Meta:
        model=Business
        exclude = ['business_user','business_neighborhood']

class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields = ['categories','post_image','description']

class HoodForm(forms.Form):
    your_name = forms.CharField(label='First Name',max_length=30)
    email = forms.EmailField(label='Email')