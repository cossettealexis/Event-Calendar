# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Author: cgabuya
# Date: 05/27/2023
# -----------------------------------------------------------------------------


from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, "scheduler/scheduler.html")
