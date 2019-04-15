#!/usr/bin/python3
# -*- coding:utf-8 -*-
# __author__ = 'liao gao xiang'

"""quant URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^db/$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^db/$', HomeView.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^db/blog/', include('blog.urls'))
"""

import xadmin
from django.conf.urls import url, include
from rest_framework.documentation import include_docs_urls  # 引入DRF的文档
from rest_framework.authtoken import views
from common.data import BaseView, StockInfoView, HolderInfoView, LiquidHolderInfoView, MarketDayView, MarketWeekView, \
    MarketMonthView, MarginView, MarketYearView, MorphologicFactorView, TechnicalFactorView, FinancialFactorView

urlpatterns = [
    # xadmin后台管理
    url(r'^admin/', xadmin.site.urls),
    # Excel上传
    url(r'^$', BaseView.as_view(), name='index'),
    url(r'^db/stock_info/$', StockInfoView.as_view(), name='stock_info'),
    url(r'^db/holder_info/$', HolderInfoView.as_view(), name='holder_info'),
    url(r'^db/liquid_holder_info/$', LiquidHolderInfoView.as_view(), name='liquid_holder_info'),
    url(r'^db/market_day/$', MarketDayView.as_view(), name='market_day'),
    url(r'^db/market_week/$', MarketWeekView.as_view(), name='market_week'),
    url(r'^db/market_month/$', MarketMonthView.as_view(), name='market_month'),
    url(r'^db/market_year/$', MarketYearView.as_view(), name='market_year'),
    url(r'^db/margin/$', MarginView.as_view(), name='margin'),
    url(r'^db/morphologic_factor/$', MorphologicFactorView.as_view(), name='morphologic_factor'),
    url(r'^db/technical_factor/$', TechnicalFactorView.as_view(), name='technical_factor'),
    url(r'^db/financial_factor/$', FinancialFactorView.as_view(), name='financial_factor'),
    # DRF authentication
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api-token-auth/$', views.obtain_auth_token),
    # DRP document
    url(r'docs/', include_docs_urls(title='量化投资')),  # 一定不能写成r'docs/$'
    # DRF API
    url(r'^api/', include('stock.urls', namespace='users')),  # 总的API入口
]
