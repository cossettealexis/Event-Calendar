# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Author: cgabuya
# Date: 05/27/2023
# -----------------------------------------------------------------------------


from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
]