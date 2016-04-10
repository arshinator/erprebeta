from django.contrib import admin

# import your model
from .models import Profile

# setup automatic slug creation
class ProfileAdmin(admin.ModelAdmin):
    model=Profile
    list_display = ('first_name','last_name', 'pan','dob',)
    prepopulated_fields = {'slug': ('first_name',)}

# Register your models here.
admin.site.register(Profile, ProfileAdmin)
