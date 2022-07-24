# django-custom-mulitple-filter

django-filter 에서 multiplefilter를 구현하기 위해서는 choices(queryset) 가 되는 부분이 필요했는데
하지만 결국 field 기반으로 돌아가기 때문에 choices 하는 부분 없이 그 field 를 통해서 필터링을 거는 방식으로 구현

더 구현되어져야 하는 부분은 테스트가 빈약하기에 해당하는 부분 필터만 테스트 할 수 있게 변경해야함

```python
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
        # 따로 필드에 대한 제약을 걸어놓음 이 부분은 typemultiplechoicefilter 참조
        if self.coerce and isinstance(value, list):
            try:
                value = [self.coerce(v) for v in value]
            except ValueError:
                raise ValidationError(self.error_messages['invalid'], code='invalid')
        return value


class MultipleFilter(filters.MultipleChoiceFilter):
    field_class = MultipleField
```
