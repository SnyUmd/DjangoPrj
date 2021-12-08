# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 13:38:46 2021

@author: SNY-Beelink
"""

from django.urls import path
from . import views

#URLパターン逆引きの為に名前を付ける
app_name = 'blog'

urlpatterns = {
    path('', views.IndexView.as_view(), name='index'),
}
