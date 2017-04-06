# -*- coding: utf-8 -*-
from django.views.generic.edit import FormView
from django.urls import reverse

from . import forms


class CrudFormView(FormView):
    template_name = 'crud_form.html'
    form_class = forms.CrudForm

    def get_success_url(self):
        return reverse('main_menu')

    # def form_valid(self, form):
    #     # This method is called when valid form data has been POSTed.
    #     # It should return an HttpResponse.
    #     form.send_email()
    #     return super(ContactView, self).form_valid(form)


crud_form_view = CrudFormView.as_view()
