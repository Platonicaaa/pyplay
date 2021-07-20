from bootstrap_datepicker_plus import DateTimePickerInput
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, ButtonHolder, Field, Row, Fieldset
from django import forms

from .models import Auction


class AuctionForm(forms.ModelForm):
    class Meta:
        model = Auction
        fields = '__all__'
        widgets = {
            'time_starting': DateTimePickerInput(),
            'time_ending': DateTimePickerInput(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_id = 'id-auctionForm'
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            'product_id',
            'bids',
            'time_starting',
            'time_ending',
            ButtonHolder(Submit('Save', 'Save')),
        )
