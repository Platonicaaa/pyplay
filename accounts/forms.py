from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from accounts.models import PyPlayyUser


class PyPlayyUserCreationForm(UserCreationForm):
    class Meta:
        model = PyPlayyUser
        fields = ('username', 'email')


class PyPlayyUserChangeForm(UserChangeForm):
    class Meta:
        model = PyPlayyUser
        fields = ('username', 'email')
