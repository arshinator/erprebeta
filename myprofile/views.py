from django.shortcuts import render, redirect
from .models import Profile
from .forms import ProfileForm
from django.template.defaultfilters import slugify


# Create your views here.




def index(request):
    profiles = Profile.objects.all()
    return render(request, 'index.html', {'profiles': profiles, })


def profile_detail(request, slug):
    # grab the object
    profile = Profile.objects.get(slug=slug)

    # and pass to the template
    return render(request, 'profiles/profile_detail.html', {'profiles': profile, })


def edit_profile(request, slug):
    # grab the object
    profile = Profile.objects.get(slug=slug)
    # set the form we are using
    form_class = ProfileForm

    # if we're coming to this view from a sbmitted form
    if request.method == 'POST':
        # grab the data from the submitted form and apply to the form
        form = form_class(data=request.POST, instance=profile)
        if form.is_valid():
            # save the new data
            form.save()
            return redirect('profile_detail', slug=profile.slug)
            # otherwise just create the form
    else:
        form = form_class(instance=profile)

        # and render the template
        return render(request, 'profiles/edit_profile.html', {'profiles': profile, 'form': form, })


def create_profile(request):
    form_class = ProfileForm
    # if we're coming from a submitted form, do this
    if request.method == 'POST':
        # grab the data from the submitted form and apply to the form
        form = form_class(request.POST)
        if form.is_valid():
            # create an instance but dont save yet
            profile = form.save(commit=False)
            # set the additional details
            profile.user = request.user
            profile.slug = slugify(profile.pan)

            # save the object
            profile.save()

            # redirect to our newly created profiles
            return redirect('profile_detail', slug=profile.slug)

            # otherwise just create the form
    else:
        form = form_class()

    return render(request, 'profiles/create_profile.html', {'form': form, })
