# -*- coding: utf-8 -*-
from django.conf.urls import url

from crud.views import crud_form_view

urlpatterns = [
    url(r'^form/$', crud_form_view, name='crud_form_view')
]
