# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.production import views

urlpatterns = [

    # The home page
    #path('', views.index, name='home'),

    path('stocks_table/', views.stocks_table,  name='stocks_table'),


]
