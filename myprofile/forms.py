from django.forms import ModelForm
from myprofile.models import Profile

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ('first_name','last_name', 'pan','dob')