from django.urls import reverse_lazy
from django.views import generic

from .forms import PyPlayyUserCreationForm


class SignupView(generic.CreateView):
    form_class = PyPlayyUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
