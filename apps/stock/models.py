#!/usr/bin/python3
# -*- coding:utf-8 -*-
# __author__ = 'liao gao xiang'

from django.db import models


class StockInfo(models.Model):
    """股票信息"""
    code = models.CharField(max_length=6, unique=True, verbose_name='股票代码')
    name = models.CharField(max_length=20, verbose_name='股票名称')
    is_st = models.BooleanField(verbose_name='是否垃圾股')
    industry = models.CharField(max_length=10, verbose_name='行业类别')
    is_margin = models.BooleanField(verbose_name='是否两融')
    is_hs300 = models.BooleanField(verbose_name='沪深300')
    is_sh = models.BooleanField(verbose_name='上证A股')
    is_sz = models.BooleanField(verbose_name='深圳A股')
    is_sh50 = models.BooleanField(verbose_name='上证50')
    is_500 = models.BooleanField(verbose_name='中证500')
    is_sme = models.BooleanField(verbose_name='中小板')
    is_second = models.BooleanField(verbose_name='创业板')
    share_total = models.BigIntegerField(verbose_name='总股本')
    share_liqa = models.BigIntegerField(verbose_name='流通A股')
    share_restrict = models.BigIntegerField(blank=True, null=True, verbose_name='限售A股')
    holder_num = models.IntegerField(blank=True, null=True, verbose_name='股东户数')
    holder_average_num = models.IntegerField(blank=True, null=True, verbose_name='户均持股数量')
    holder_average_change = models.DecimalField(max_digits=6, decimal_places=4, blank=True, null=True, verbose_name='股东户数增长率')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        verbose_name = '股票信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return "{}_{}".format(self.code, self.name)


class HolderInfo(models.Model):
    """十大股东信息"""
    code = models.CharField(max_length=6, db_index=True, verbose_name='股票代码')
    name = models.CharField(db_index=True, max_length=100, blank=True, null=True, verbose_name='股东名称')
    quantity = models.BigIntegerField(blank=True, null=True, verbose_name='持股数量')
    pct = models.DecimalField(max_digits=6, decimal_places=4, blank=True, null=True, verbose_name='持股比例')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        verbose_name = '十大股东信息'
        verbose_name_plural = verbose_name
        unique_together = ('code', 'name')

    def __str__(self):
        return "{}_{}".format(self.code, self.name)


class LiquidHolderInfo(models.Model):
    """十大流通股东信息"""
    code = models.CharField(max_length=6, db_index=True, verbose_name='股票代码')
    name = models.CharField(db_index=True, max_length=100, blank=True, null=True, verbose_name='股东名称')
    quantity = models.BigIntegerField(blank=True, null=True, verbose_name='持股数量')
    pct = models.DecimalField(max_digits=6, decimal_places=4, blank=True, null=True, verbose_name='持股比例')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        verbose_name = '十大流通股东信息'
        verbose_name_plural = verbose_name
        unique_together = ('code', 'name')

    def __str__(self):
        return "{}_{}".format(self.code, self.name)


class MarketDay(models.Model):
    """日K线"""
    code = models.CharField(max_length=6, db_index=True, verbose_name='股票代码')
    date = models.DateField(db_index=True, verbose_name='交易日')
    close = models.DecimalField(max_digits=6, decimal_places=4, blank=True, null=True, verbose_name='收盘价')
    open = models.DecimalField(max_digits=6, decimal_places=4, blank=True, null=True, verbose_name='开盘价')
    high = models.DecimalField(max_digits=6, decimal_places=4, blank=True, null=True, verbose_name='最高价')
    low = models.DecimalField(max_digits=6, decimal_places=4, blank=True, null=True, verbose_name='最低价')
    volume = models.BigIntegerField(blank=True, null=True, verbose_name='交易量')
    pct_change = models.DecimalField(max_digits=6, decimal_places=4, blank=True, null=True, verbose_name='涨跌幅')
    swing = models.DecimalField(max_digits=6, decimal_places=4, blank=True, null=True, verbose_name='振幅')
    avg_price = models.DecimalField(max_digits=6, decimal_places=4, blank=True, null=True, verbose_name='均价')
    turn = models.DecimalField(max_digits=6, decimal_places=4, blank=True, null=True, verbose_name='换手率')
    amount = models.BigIntegerField(blank=True, null=True, verbose_name='成交额')
    buy_amount = models.BigIntegerField(blank=True, null=True, verbose_name='流入额')
    sell_amount = models.BigIntegerField(blank=True, null=True, verbose_name='流出额')
    buy_volume = models.BigIntegerField(blank=True, null=True, verbose_name='流入量')
    sell_volume = models.BigIntegerField(blank=True, null=True, verbose_name='流出量')
    net_buy_amount = models.BigIntegerField(blank=True, null=True, verbose_name='净买入额')
    net_buy_volume = models.BigIntegerField(blank=True, null=True, verbose_name='净买入量')
    active_buy_volume = models.BigIntegerField(blank=True, null=True, verbose_name='主动买入量')
    active_sell_volume = models.BigIntegerField(blank=True, null=True, verbose_name='主动卖出量')
    buy_amount_active = models.BigIntegerField(blank=True, null=True, verbose_name='主动买入额')
    sell_amount_active = models.BigIntegerField(blank=True, null=True, verbose_name='主动卖出额')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        verbose_name = '日K线'
        verbose_name_plural = verbose_name
        unique_together = ('code', 'date')

    def __str__(self):
        return "{}_{}".format(self.code, self.date)


class MarketWeek(models.Model):
    """周K线"""
    code = models.CharField(max_length=6, db_index=True, verbose_name='股票代码')
    week = models.PositiveIntegerField(db_index=True, verbose_name='周K线时间')  # 如201801,201802表示2018年的第一周、第二周
    close = models.DecimalField(max_digits=6, decimal_places=4, blank=True, null=True, verbose_name='收盘价')
    open = models.DecimalField(max_digits=6, decimal_places=4, blank=True, null=True, verbose_name='开盘价')
    high = models.DecimalField(max_digits=6, decimal_places=4, blank=True, null=True, verbose_name='最高价')
    low = models.DecimalField(max_digits=6, decimal_places=4, blank=True, null=True, verbose_name='最低价')
    pct_change = models.DecimalField(max_digits=6, decimal_places=4, blank=True, null=True, verbose_name='涨跌幅')
    swing = models.DecimalField(max_digits=6, decimal_places=4, blank=True, null=True, verbose_name='振幅')
    avg_price = models.DecimalField(max_digits=6, decimal_places=4, blank=True, null=True, verbose_name='均价')
    turn = models.DecimalField(max_digits=6, decimal_places=4, blank=True, null=True, verbose_name='换手率')
    volume = models.BigIntegerField(blank=True, null=True, verbose_name='交易量')
    amount = models.BigIntegerField(blank=True, null=True, verbose_name='成交额')
    buy_amount = models.BigIntegerField(blank=True, null=True, verbose_name='流入额')
    sell_amount = models.BigIntegerField(blank=True, null=True, verbose_name='流出额')
    buy_volume = models.BigIntegerField(blank=True, null=True, verbose_name='流入量')
    sell_volume = models.BigIntegerField(blank=True, null=True, verbose_name='流出量')
    net_buy_amount = models.BigIntegerField(blank=True, null=True, verbose_name='净买入额')
    net_buy_volume = models.BigIntegerField(blank=True, null=True, verbose_name='净买入量')
    net_sell_amount = models.BigIntegerField(blank=True, null=True, verbose_name='净卖出额')
    net_sell_volume = models.BigIntegerField(blank=True, null=True, verbose_name='净卖出量')
    buy_amount_active = models.BigIntegerField(blank=True, null=True, verbose_name='主动买入额')
    sell_amount_active = models.BigIntegerField(blank=True, null=True, verbose_name='主动卖出额')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        verbose_name = '周K线'
        verbose_name_plural = verbose_name
        unique_together = ('code', 'week')

    def __str__(self):
        return "{}_{}".format(self.code, self.week)


class MarketMonth(models.Model):
    """月K线"""
    code = models.CharField(max_length=6, db_index=True, verbose_name='股票代码')
    month = models.PositiveIntegerField(db_index=True, verbose_name='月K线时间')  # 如201801,201802表示2018年的第1月，2月
    close = models.DecimalField(max_digits=6, decimal_places=4, blank=True, null=True, verbose_name='收盘价')
    open = models.DecimalField(max_digits=6, decimal_places=4, blank=True, null=True, verbose_name='开盘价')
    high = models.DecimalField(max_digits=6, decimal_places=4, blank=True, null=True, verbose_name='最高价')
    low = models.DecimalField(max_digits=6, decimal_places=4, blank=True, null=True, verbose_name='最低价')
    pct_change = models.DecimalField(max_digits=6, decimal_places=4, blank=True, null=True, verbose_name='涨跌幅')
    swing = models.DecimalField(max_digits=6, decimal_places=4, blank=True, null=True, verbose_name='振幅')
    avg_price = models.DecimalField(max_digits=6, decimal_places=4, blank=True, null=True, verbose_name='均价')
    turn = models.DecimalField(max_digits=6, decimal_places=4, blank=True, null=True, verbose_name='换手率')
    volume = models.BigIntegerField(blank=True, null=True, verbose_name='交易量')
    amount = models.BigIntegerField(blank=True, null=True, verbose_name='成交额')
    buy_amount = models.BigIntegerField(blank=True, null=True, verbose_name='流入额')
    sell_amount = models.BigIntegerField(blank=True, null=True, verbose_name='流出额')
    buy_volume = models.BigIntegerField(blank=True, null=True, verbose_name='流入量')
    sell_volume = models.BigIntegerField(blank=True, null=True, verbose_name='流出量')
    net_buy_amount = models.BigIntegerField(blank=True, null=True, verbose_name='净买入额')
    net_buy_volume = models.BigIntegerField(blank=True, null=True, verbose_name='净买入量')
    net_sell_amount = models.BigIntegerField(blank=True, null=True, verbose_name='净卖出额')
    net_sell_volume = models.BigIntegerField(blank=True, null=True, verbose_name='净卖出量')
    buy_amount_active = models.BigIntegerField(blank=True, null=True, verbose_name='主动买入额')
    sell_amount_active = models.BigIntegerField(blank=True, null=True, verbose_name='主动卖出额')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        verbose_name = '月K线'
        verbose_name_plural = verbose_name
        unique_together = ('code', 'month')

    def __str__(self):
        return "{}_{}".format(self.code, self.month)


class MarketYear(models.Model):
    """年K线"""
    code = models.CharField(max_length=6, db_index=True, verbose_name='股票代码')
    year = models.PositiveSmallIntegerField(db_index=True, verbose_name='月K线时间')  # 如2017,2018
    close = models.DecimalField(max_digits=6, decimal_places=4, blank=True, null=True, verbose_name='收盘价')
    open = models.DecimalField(max_digits=6, decimal_places=4, blank=True, null=True, verbose_name='开盘价')
    high = models.DecimalField(max_digits=6, decimal_places=4, blank=True, null=True, verbose_name='最高价')
    low = models.DecimalField(max_digits=6, decimal_places=4, blank=True, null=True, verbose_name='最低价')
    pct_change = models.DecimalField(max_digits=6, decimal_places=4, blank=True, null=True, verbose_name='涨跌幅')
    swing = models.DecimalField(max_digits=6, decimal_places=4, blank=True, null=True, verbose_name='振幅')
    avg_price = models.DecimalField(max_digits=6, decimal_places=4, blank=True, null=True, verbose_name='均价')
    turn = models.DecimalField(max_digits=6, decimal_places=4, blank=True, null=True, verbose_name='换手率')
    volume = models.BigIntegerField(blank=True, null=True, verbose_name='交易量')
    amount = models.BigIntegerField(blank=True, null=True, verbose_name='成交额')
    buy_amount = models.BigIntegerField(blank=True, null=True, verbose_name='流入额')
    sell_amount = models.BigIntegerField(blank=True, null=True, verbose_name='流出额')
    buy_volume = models.BigIntegerField(blank=True, null=True, verbose_name='流入量')
    sell_volume = models.BigIntegerField(blank=True, null=True, verbose_name='流出量')
    net_buy_amount = models.BigIntegerField(blank=True, null=True, verbose_name='净买入额')
    net_buy_volume = models.BigIntegerField(blank=True, null=True, verbose_name='净买入量')
    net_sell_amount = models.BigIntegerField(blank=True, null=True, verbose_name='净卖出额')
    net_sell_volume = models.BigIntegerField(blank=True, null=True, verbose_name='净卖出量')
    buy_amount_active = models.BigIntegerField(blank=True, null=True, verbose_name='主动买入额')
    sell_amount_active = models.BigIntegerField(blank=True, null=True, verbose_name='主动卖出额')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        verbose_name = '年K线'
        verbose_name_plural = verbose_name
        unique_together = ('code', 'year')

    def __str__(self):
        return "{}_{}".format(self.code, self.year)


class Margin(models.Model):
    """融资融券"""
    code = models.CharField(max_length=6, db_index=True, verbose_name='股票代码')
    date = models.DateField(db_index=True, verbose_name='交易日')
    purchase_with_borrowed_money = models.BigIntegerField(blank=True, null=True, verbose_name='融资买入额')
    repayment_to_broker = models.BigIntegerField(blank=True, null=True, verbose_name='融资偿还额')
    trading_balance = models.BigIntegerField(blank=True, null=True, verbose_name='融资余额')
    sales_of_borrowed_sec = models.BigIntegerField(blank=True, null=True, verbose_name='融券卖出量')
    repayment_of_borrowed_sec = models.BigIntegerField(blank=True, null=True, verbose_name='融券偿还量')
    sale_trading_amount = models.BigIntegerField(blank=True, null=True, verbose_name='融券偿还额')  # 对应excel的“融券卖出额”
    sec_lending_balance_volume = models.BigIntegerField(blank=True, null=True, verbose_name='融券余量')
    sec_lending_balance = models.BigIntegerField(blank=True, null=True, verbose_name='融券余额')
    trading_and_sec_lending_balance = models.BigIntegerField(blank=True, null=True, verbose_name='融资融券余额')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        verbose_name = '融资融券'
        verbose_name_plural = verbose_name
        unique_together = ('code', 'date')

    def __str__(self):
        return "{}_{}".format(self.code, self.date)


class MorphologicFactor(models.Model):
    """形态因子"""
    code = models.CharField(max_length=6, db_index=True, verbose_name='股票代码')
    date = models.DateField(db_index=True, verbose_name='交易日')
    red_three_soldiers = models.DecimalField(max_digits=8, decimal_places=4, blank=True, null=True, verbose_name='红三兵')
    hammer = models.DecimalField(max_digits=8, decimal_places=4, blank=True, null=True, verbose_name='上锤线')
    hammer_down = models.DecimalField(max_digits=8, decimal_places=4, blank=True, null=True, verbose_name='倒锤线')
    two_ravens = models.DecimalField(max_digits=8, decimal_places=4, blank=True, null=True, verbose_name='两只乌鸦')
    three_ravens = models.DecimalField(max_digits=8, decimal_places=4, blank=True, null=True, verbose_name='三只乌鸦')
    morning_star = models.DecimalField(max_digits=8, decimal_places=4, blank=True, null=True, verbose_name='早晨之星')
    evening_star = models.DecimalField(max_digits=8, decimal_places=4, blank=True, null=True, verbose_name='黄昏之星')
    dark_cloud_cover = models.DecimalField(max_digits=8, decimal_places=4, blank=True, null=True, verbose_name='乌云盖顶')
    meteor_line = models.DecimalField(max_digits=8, decimal_places=4, blank=True, null=True, verbose_name='流星线')
    three_line_strike = models.DecimalField(max_digits=8, decimal_places=4, blank=True, null=True, verbose_name='三线打击')
    southern_samsung = models.DecimalField(max_digits=8, decimal_places=4, blank=True, null=True, verbose_name='南方三星')
    be_confronted_with_a_formidable_enemy = models.DecimalField(max_digits=8, decimal_places=4, blank=True, null=True, verbose_name='大敌当前')
    abandoned_infant = models.DecimalField(max_digits=8, decimal_places=4, blank=True, null=True, verbose_name='弃婴')
    belt_line = models.DecimalField(max_digits=8, decimal_places=4, blank=True, null=True, verbose_name='捉腰带线')
    cross_pregnancy_line = models.DecimalField(max_digits=8, decimal_places=4, blank=True, null=True, verbose_name='十字孕线')
    rickshaw_man = models.DecimalField(max_digits=8, decimal_places=4, blank=True, null=True, verbose_name='黄包车夫')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        verbose_name = '形态因子'
        verbose_name_plural = verbose_name
        unique_together = ('code', 'date')

    def __str__(self):
        return "{}_{}".format(self.code, self.date)


class TechnicalFactor(models.Model):
    """技术因子"""
    code = models.CharField(max_length=6, db_index=True, verbose_name='股票代码')
    date = models.DateField(db_index=True, verbose_name='交易日')
    ma = models.DecimalField(max_digits=8, decimal_places=4, blank=True, null=True, verbose_name='MA(均线)')
    macd = models.DecimalField(max_digits=8, decimal_places=4, blank=True, null=True, verbose_name='MACD')
    kdj = models.DecimalField(max_digits=8, decimal_places=4, blank=True, null=True, verbose_name='KDJ')
    rsi = models.DecimalField(max_digits=8, decimal_places=4, blank=True, null=True, verbose_name='RSI')
    bias = models.DecimalField(max_digits=8, decimal_places=4, blank=True, null=True, verbose_name='BIAS')
    bbi = models.DecimalField(max_digits=8, decimal_places=4, blank=True, null=True, verbose_name='BBI')
    cci = models.DecimalField(max_digits=8, decimal_places=4, blank=True, null=True, verbose_name='CCI')
    atr = models.DecimalField(max_digits=8, decimal_places=4, blank=True, null=True, verbose_name='ATR')
    trix = models.DecimalField(max_digits=8, decimal_places=4, blank=True, null=True, verbose_name='TRIX')
    ema = models.DecimalField(max_digits=8, decimal_places=4, blank=True, null=True, verbose_name='EMA')
    dma = models.DecimalField(max_digits=8, decimal_places=4, blank=True, null=True, verbose_name='DMA')
    boll_up = models.DecimalField(max_digits=8, decimal_places=4, blank=True, null=True, verbose_name='布林带上轨')
    boll_down = models.DecimalField(max_digits=8, decimal_places=4, blank=True, null=True, verbose_name='布林带下轨')
    sar = models.DecimalField(max_digits=8, decimal_places=4, blank=True, null=True, verbose_name='SAR')
    si = models.DecimalField(max_digits=8, decimal_places=4, blank=True, null=True, verbose_name='SI')
    wr = models.DecimalField(max_digits=8, decimal_places=4, blank=True, null=True, verbose_name='WR')
    cr = models.DecimalField(max_digits=8, decimal_places=4, blank=True, null=True, verbose_name='CR')
    std = models.DecimalField(max_digits=8, decimal_places=4, blank=True, null=True, verbose_name='STD(方差)')
    vol_ratio = models.DecimalField(max_digits=8, decimal_places=4, blank=True, null=True, verbose_name='量比')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        verbose_name = '技术因子'
        verbose_name_plural = verbose_name
        unique_together = ('code', 'date')

    def __str__(self):
        return "{}_{}".format(self.code, self.date)


class FinancialFactor(models.Model):
    """财务因子，每支股票有季报、半年报、年报"""
    TIME = (
        (1, '第一季度财报'),
        (2, '第二季度财报'),
        (3, '第三季度财报'),
        (4, '第四季度财报'),
        (5, '半年财报'),
        (6, '全年财报'),
    )
    code = models.CharField(max_length=6, db_index=True, verbose_name='股票代码')
    year = models.PositiveSmallIntegerField(db_index=True, verbose_name='年份')  # 年份 + 财报时间来区分不同财报
    time = models.PositiveSmallIntegerField(choices=TIME, db_index=True, verbose_name='财报时间')
    eps = models.DecimalField(max_digits=15, decimal_places=10, blank=True, null=True, verbose_name='每股收益')
    bps = models.DecimalField(max_digits=15, decimal_places=10, blank=True, null=True, verbose_name='每股净资产')
    gross_earnings_per_share = models.DecimalField(max_digits=15, decimal_places=10, blank=True, null=True, verbose_name='每股营业总收入')
    capital_stock_per_share = models.DecimalField(max_digits=15, decimal_places=10, blank=True, null=True, verbose_name='每股资本公积')
    earnings_per_share = models.DecimalField(max_digits=15, decimal_places=10, blank=True, null=True, verbose_name='每股盈余公积')
    undistributed_profit_per_share = models.DecimalField(max_digits=15, decimal_places=10, blank=True, null=True, verbose_name='每股未分配利润')
    pre_tax_earnings_per_share = models.DecimalField(max_digits=15, decimal_places=10, blank=True, null=True, verbose_name='每股税前利润')
    ebitda = models.DecimalField(max_digits=15, decimal_places=10, blank=True, null=True, verbose_name='每股EBITDA')
    pe = models.DecimalField(max_digits=15, decimal_places=10, blank=True, null=True, verbose_name='市盈率')
    roe = models.DecimalField(max_digits=15, decimal_places=10, blank=True, null=True, verbose_name='净资产收益率')
    roa = models.DecimalField(max_digits=15, decimal_places=10, blank=True, null=True, verbose_name='总资产报酬率')
    roic = models.DecimalField(max_digits=15, decimal_places=10, blank=True, null=True, verbose_name='投入资本回报率')
    gross_profit_margin = models.DecimalField(max_digits=15, decimal_places=10, blank=True, null=True, verbose_name='销售毛利率')
    net_profit_margin = models.DecimalField(max_digits=15, decimal_places=10, blank=True, null=True, verbose_name='销售净利率')
    opt_oebt = models.DecimalField(max_digits=15, decimal_places=10, blank=True, null=True, verbose_name='主营业务比率')
    debt_to_assets = models.DecimalField(max_digits=15, decimal_places=10, blank=True, null=True, verbose_name='资产负债率')
    long_debt_to_long_captial = models.DecimalField(max_digits=15, decimal_places=10, blank=True, null=True, verbose_name='长债负债率')
    short_debt_to_long_captial = models.DecimalField(max_digits=15, decimal_places=10, blank=True, null=True, verbose_name='短债负债率')
    assets_to_equity = models.DecimalField(max_digits=15, decimal_places=10, blank=True, null=True, verbose_name='权益乘数')
    fa_current = models.DecimalField(max_digits=15, decimal_places=10, blank=True, null=True, verbose_name='流动比率')
    fa_quick = models.DecimalField(max_digits=15, decimal_places=10, blank=True, null=True, verbose_name='速动比率')
    fa_cash_to_current_debt = models.DecimalField(max_digits=15, decimal_places=10, blank=True, null=True, verbose_name='现金比率')
    fa_debt_to_equity = models.DecimalField(max_digits=15, decimal_places=10, blank=True, null=True, verbose_name='产权比率')
    fa_invturn = models.DecimalField(max_digits=15, decimal_places=10, blank=True, null=True, verbose_name='存货周转率')
    fa_arturn = models.DecimalField(max_digits=15, decimal_places=10, blank=True, null=True, verbose_name='应收转款周转率')
    fa_assets_turn = models.DecimalField(max_digits=15, decimal_places=10, blank=True, null=True, verbose_name='总资产周转率')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        verbose_name = '财务因子'
        verbose_name_plural = verbose_name
        unique_together = ('code', 'year', 'time')

    def __str__(self):
        return "{}_{}_{}".format(self.code, self.year, self.time)
