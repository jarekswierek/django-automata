# -*- coding: utf-8 -*-
import copy

from django.views import generic
from django.shortcuts import render

from . import forms


class CrudFormView(generic.FormView):
    template_name = 'crud/form.html'
    form_class = forms.CrudForm

    def form_valid(self, form):
        """Render result.
        """
        context = copy.copy(form.cleaned_data)
        context.update({
            'create_view': 'create' in context['views'],
            'list_view': 'read' in context['views'],
            'update_view': 'update' in context['views'],
            'delete_view': 'delete' in context['views'],
        })
        return render(self.request, 'crud/result.html', context)


crud_form_view = CrudFormView.as_view()
