#!/usr/bin/python3
# -*- coding:utf-8 -*-
# __author__ = 'liao gao xiang'

from rest_framework import serializers
from stock.models import StockInfo


class StockInfoSerializer(serializers.HyperlinkedModelSerializer):
    """"""

    class Meta:
        model = StockInfo
        fields = '__all__'
