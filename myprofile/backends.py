from registration.backends.simple.views import RegistrationView

#my new registration view, subclassing RegistrationView
#from our plugin

class MyRegistrationView(RegistrationView):
    def get_success_url(self, request):
        #the named URL that we want to redirect to after
        #successfull registration
        return ('registration_create_profile')


    # def __init__(self, *args, **kwargs):
    #     super(RegistrationView, self).__init__(*args, **kwargs)
    #     self.pop('username')


