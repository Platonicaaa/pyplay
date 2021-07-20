from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, ButtonHolder, Submit
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from accounts.models import PyPlayyUser


class PyPlayyUserCreationForm(UserCreationForm):
    class Meta:
        model = PyPlayyUser
        fields = ('username', 'email')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_id = 'id-signup'
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('create', 'Create'))


class PyPlayyUserChangeForm(UserChangeForm):
    class Meta:
        model = PyPlayyUser
        fields = ('username', 'email')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_id = 'id-changeuser'
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('save', 'Save'))

