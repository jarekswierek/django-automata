# -*- coding: utf-8 -*-
from django import forms
from django.urls import reverse

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Submit
from crispy_forms.bootstrap import FormActions


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

        cancel_url = reverse('main_menu')
        cancel = 'window.location.href="{}"'.format(cancel_url)

        super(CrudForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
                'CRUD form',
                'model_name',
                'views'
            ),
            FormActions(
                Submit('save', 'Create', css_class="btn-primary"),
                Submit('cancel', 'Cancel', onclick=cancel)
            )
        )
