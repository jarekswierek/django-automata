# -*- coding: utf-8 -*-
from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit


class CrudForm(forms.Form):
    VIEWS_CHOICES = (
        ('create', 'create'),
        ('read', 'read/list'),
        ('update', 'update'),
        ('delete', 'delete'),
    )

    model_name = forms.CharField()
    views = forms.MultipleChoiceField(
        choices=VIEWS_CHOICES,
        widget=forms.CheckboxSelectMultiple(attrs={"checked":""})
    )

    def __init__(self, *args, **kwargs):
        super(CrudForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
                'CRUD form',
                'model_name',
                'views'
            ),
            ButtonHolder(
                Submit('submit', 'Submit', css_class='button white')
            )
        )
