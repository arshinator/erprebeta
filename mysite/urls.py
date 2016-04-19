"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))

"""
from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from myprofile.backends import MyRegistrationView
from django.views.generic import TemplateView, RedirectView

urlpatterns = [
    url(r'^$', 'myprofile.views.index', name='home'),
    url(r'^admin/', admin.site.urls),

    # url(r'^profiles/$', RedirectView.as_view(pattern_name='tandc',permanent=True)),
    url(r'^profiles/(?P<slug>[-\w]+)/$', 'myprofile.views.profile_detail', name='profile_detail'),
    url(r'^profiles/(?P<slug>[-\w]+)/edit/$', 'myprofile.views.edit_profile', name='edit_profile'),
    url(r'^accounts/register/$', MyRegistrationView.as_view(), name='registration_register'),
    url(r'^accounts/create_profile/$', 'myprofile.views.create_profile', name='registration_create_profile'),

    # mycontact
    url(r"^contact/", 'mycontact.views.contact', name="contact"),

    # myupload
    url(r'^dash/', 'myupload.views.Form', name="dash"),
    url(r'^upload', 'myupload.views.Upload', name="upload"),


    # url(r'^dataform/', 'myfield.views.dataform', name="dataform"),
    url(r"^data", 'myfield.views.data', name="data"),

    # terms and refund templates
    url(r'^refund/', TemplateView.as_view(template_name='refund.html'), name='refund'),
    url(r"^tandc/", TemplateView.as_view(template_name='tandc.html'), name='tandc'),
    url(r"^pay/", TemplateView.as_view(template_name='pay.html'), name='pay'),
    url(r"^display/", TemplateView.as_view(template_name='display.html'), name='display'),

    url(r'^accounts/', include('registration.backends.default.urls')),

]
