#!/usr/bin/python3
# -*- coding:utf-8 -*-
# __author__ = 'liao gao xiang'

from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from stock.serializers import StockInfoSerializer
from stock.models import StockInfo
from rqalpha import api, core, model


class StockInfoPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    page_query_param = 'p'
    max_page_size = 100


class StockInfoView(APIView):
    """"""

    def __int__(self, context):
        context.cash_limit = 5000

    def post(self, request):
        """
        返回回测结果
        :param request:
        :return:
        """
        print(self.request.POST)
        print(request.data, type(request.data))
        return Response("success")

    def handle_bar(self, context, bar_dict):
        """
        必须实现，bar数据的更新会自动触发该方法的调用。策略具体逻辑可在该方法内实现，包括交易信号的产生、订单的创建等。
        在实时模拟交易中，该函数在交易时间内会每分钟被触发一次。
        :param context: (StrategyContext object) – 策略上下文
        :param bar_dict:  (BarDict object) – key为order_book_id，value为bar数据。当前合约池内所有合约的bar数据信息都会更新在bar_dict里面
        :return:
        """
        pass

    def before_trading(self, context):
        """
        选择实现，每天在策略开始交易前会被调用
        :param context: (StrategyContext object) – 策略上下文
        :return:
        """
        pass

    def after_trading(self, context):
        """
        每天在收盘后被调用。不能在这个函数中发送订单。您可以在该函数中进行当日收盘后的一些计算。
        在实时模拟交易中，该函数会在每天15:30触发。
        :param context: (StrategyContext object) – 策略上下文
        :return:
        """
        pass

    def after_trading1(self, context, ontex, ontext1):
        """

        :param context:
        :param ontex:
        :param ontext1:
        :return:
        """
        pass
