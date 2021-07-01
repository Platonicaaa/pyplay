from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin

from .forms import PyPlayyUserCreationForm, PyPlayyUserChangeForm
from .models import PyPlayyUser


class PyPlayyUserAdmin(UserAdmin):
    add_form = PyPlayyUserCreationForm
    form = PyPlayyUserChangeForm
    model = PyPlayyUser
    list_display = ['email', 'username']


admin.site.register(PyPlayyUser, PyPlayyUserAdmin)
