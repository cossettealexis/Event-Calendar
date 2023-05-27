# -*- coding: utf-8 -*-
__author__ = 'sandlbn'

from django.urls import path
from django_bootstrap_calendar.views import CalendarJsonListView, CalendarView

urlpatterns = [
    path(
        r'^json/$',
        CalendarJsonListView.as_view(),
        name='calendar_json'
    ),
    path(
        r'^$',
        CalendarView.as_view(),
        name='calendar'
    ),
]
