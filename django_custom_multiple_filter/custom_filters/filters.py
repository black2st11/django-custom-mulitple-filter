from django.utils.translation import gettext as _
from django_filters import rest_framework as filters
from django import forms
from django.core.exceptions import ValidationError


class MultipleField(forms.Field):
    widget = forms.MultipleHiddenInput
    default_error_messages = {
        'invalid': _('Enter a valid data.'),
    }

    def __init__(self, coerce=None, *args, **kwargs):
        self.coerce = coerce
        super().__init__(*args, **kwargs)

    def validate(self, value):
        if self.coerce and isinstance(value, list):
            try:
                value = [self.coerce(v) for v in value]
            except ValueError:
                raise ValidationError(self.error_messages['invalid'], code='invalid')
        return value


class MultipleFilter(filters.MultipleChoiceFilter):
    field_class = MultipleField
