from django import forms
import re
from .models import *

def is_valid_email(value):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(pattern, value):
        raise forms.ValidationError(
            'enter a valid email',
            code='invalid',
            params={'value': value}
        )


def validate_name(value):
    if not value.isalpha():
        raise forms.ValidationError(
            '%(value) has non-letters characters',
            code='invalid',
            params={'value':value}
        )

class DetailsForm(forms.ModelForm):
    first_name = forms.CharField(validators=[validate_name])
    last_name = forms.CharField(validators=[validate_name])
    email = forms.EmailField(validators=[is_valid_email])

    class Meta:
        model = Details
        fields = ['first_name','last_name','email']