#! /usr/bin/python3
# -*- coding:utf-8 -*-
# __author__ = 'liao gao xiang'

from django.conf.urls import url
from stock.views import StockInfoView

urlpatterns = [
    url(r'^stockinfo/$', StockInfoView.as_view()),
]
