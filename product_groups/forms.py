from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms

from product_groups.models import ProductGroup


class ProductGroupForm(forms.ModelForm):
    class Meta:
        model = ProductGroup
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_id = 'id-productGroupForm'
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('save', 'Save'))
