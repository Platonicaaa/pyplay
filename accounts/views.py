from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views import generic

from .forms import PyPlayyUserCreationForm
from .utils import is_seller, is_buyer


@login_required
def user_home(request):
    user = request.user
    if is_buyer(user):
        return HttpResponseRedirect(reverse('auctions:index'))
    elif is_seller(user):
        return HttpResponseRedirect(reverse('products:index'))
    else:
        return HttpResponseRedirect(reverse('auctions:index'))


class SignupView(generic.CreateView):
    form_class = PyPlayyUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
