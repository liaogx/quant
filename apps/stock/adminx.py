#!/usr/bin/python3
# -*- coding:utf-8 -*-
# __author__ = 'liao gao xiang'

import xadmin
from stock.models import StockInfo, HolderInfo, LiquidHolderInfo, MarketDay, MarketWeek, MarketMonth, MarketYear, \
    Margin, MorphologicFactor, TechnicalFactor, FinancialFactor


class StockInfoAdmin(object):
    list_display = ['code', 'name', 'is_st', 'industry', 'is_margin', 'is_hs300', 'is_sh', 'is_sz', 'is_sh50', 'is_500',
                    'is_sme', 'is_second', 'share_total', 'share_liqa', 'share_restrict', 'holder_num', 'holder_average_num',
                    'holder_average_change', 'updated_at']
    search_fields = ['code', 'name', 'is_st', 'industry', 'is_margin', 'is_hs300', 'is_sh', 'is_sz', 'is_sh50', 'is_500',
                     'is_sme', 'is_second', 'share_total', 'share_liqa', 'share_restrict', 'holder_num', 'holder_average_num',
                     'holder_average_change', 'updated_at']
    list_filter = ['code', 'name', 'is_st', 'industry', 'is_margin', 'is_hs300', 'is_sh', 'is_sz', 'is_sh50', 'is_500',
                   'is_sme', 'is_second', 'share_total', 'share_liqa', 'share_restrict', 'holder_num', 'holder_average_num',
                   'holder_average_change', 'updated_at']
    import_excel = True


class HolderInfoAdmin(object):
    list_display = ['code', 'name', 'quantity', 'pct', 'updated_at']
    search_fields = ['code', 'name', 'quantity', 'pct', 'updated_at']
    list_filter = ['code', 'name', 'quantity', 'pct', 'updated_at']


class LiquidHolderInfoAdmin(object):
    list_display = ['code', 'name', 'quantity', 'pct', 'updated_at']
    search_fields = ['code', 'name', 'quantity', 'pct', 'updated_at']
    list_filter = ['code', 'name', 'quantity', 'pct', 'updated_at']


class MarketDayAdmin(object):
    list_display = ['code', 'date', 'close', 'open', 'high', 'low', 'volume', 'pct_change', 'swing', 'avg_price', 'turn', 'amount', 'buy_amount',
                    'sell_amount', 'buy_volume', 'sell_volume', 'net_buy_amount', 'net_buy_volume', 'active_buy_volume', 'active_sell_volume',
                    'buy_amount_active', 'sell_amount_active', 'updated_at']
    search_fields = ['code', 'date', 'close', 'open', 'high', 'low', 'volume', 'pct_change', 'swing', 'avg_price', 'turn', 'amount', 'buy_amount',
                     'sell_amount', 'buy_volume', 'sell_volume', 'net_buy_amount', 'net_buy_volume', 'active_buy_volume', 'active_sell_volume',
                     'buy_amount_active', 'sell_amount_active', 'updated_at']
    list_filter = ['code', 'date', 'close', 'open', 'high', 'low', 'volume', 'pct_change', 'swing', 'avg_price', 'turn', 'amount', 'buy_amount',
                   'sell_amount', 'buy_volume', 'sell_volume', 'net_buy_amount', 'net_buy_volume', 'active_buy_volume', 'active_sell_volume',
                   'buy_amount_active', 'sell_amount_active', 'updated_at']


class MarketWeekAdmin(object):
    list_display = ['code', 'week', 'close', 'open', 'high', 'low', 'pct_change', 'swing', 'avg_price', 'turn', 'volume', 'amount', 'buy_amount',
                    'sell_amount', 'buy_volume', 'sell_volume', 'net_buy_amount', 'net_buy_volume', 'net_sell_amount', 'net_sell_volume',
                    'buy_amount_active', 'sell_amount_active', 'updated_at']
    search_fields = ['code', 'week', 'close', 'open', 'high', 'low', 'pct_change', 'swing', 'avg_price', 'turn', 'volume', 'amount', 'buy_amount',
                     'sell_amount', 'buy_volume', 'sell_volume', 'net_buy_amount', 'net_buy_volume', 'net_sell_amount', 'net_sell_volume',
                     'buy_amount_active', 'sell_amount_active', 'updated_at']
    list_filter = ['code', 'week', 'close', 'open', 'high', 'low', 'pct_change', 'swing', 'avg_price', 'turn', 'volume', 'amount', 'buy_amount',
                   'sell_amount', 'buy_volume', 'sell_volume', 'net_buy_amount', 'net_buy_volume', 'net_sell_amount', 'net_sell_volume',
                   'buy_amount_active', 'sell_amount_active', 'updated_at']


class MarketMonthAdmin(object):
    list_display = ['code', 'month', 'close', 'open', 'high', 'low', 'pct_change', 'swing', 'avg_price', 'turn', 'volume', 'amount', 'buy_amount',
                    'sell_amount', 'buy_volume', 'sell_volume', 'net_buy_amount', 'net_buy_volume', 'net_sell_amount', 'net_sell_volume',
                    'buy_amount_active', 'sell_amount_active', 'updated_at']
    search_fields = ['code', 'month', 'close', 'open', 'high', 'low', 'pct_change', 'swing', 'avg_price', 'turn', 'volume', 'amount', 'buy_amount',
                     'sell_amount', 'buy_volume', 'sell_volume', 'net_buy_amount', 'net_buy_volume', 'net_sell_amount', 'net_sell_volume',
                     'buy_amount_active', 'sell_amount_active', 'updated_at']
    list_filter = ['code', 'month', 'close', 'open', 'high', 'low', 'pct_change', 'swing', 'avg_price', 'turn', 'volume', 'amount', 'buy_amount',
                   'sell_amount', 'buy_volume', 'sell_volume', 'net_buy_amount', 'net_buy_volume', 'net_sell_amount', 'net_sell_volume',
                   'buy_amount_active', 'sell_amount_active', 'updated_at']


class MarketYearAdmin(object):
    list_display = ['code', 'year', 'close', 'open', 'high', 'low', 'pct_change', 'swing', 'avg_price', 'turn', 'volume', 'amount', 'buy_amount',
                    'sell_amount', 'buy_volume', 'sell_volume', 'net_buy_amount', 'net_buy_volume', 'net_sell_amount', 'net_sell_volume',
                    'buy_amount_active', 'sell_amount_active', 'updated_at']
    search_fields = ['code', 'year', 'close', 'open', 'high', 'low', 'pct_change', 'swing', 'avg_price', 'turn', 'volume', 'amount', 'buy_amount',
                     'sell_amount', 'buy_volume', 'sell_volume', 'net_buy_amount', 'net_buy_volume', 'net_sell_amount', 'net_sell_volume',
                     'buy_amount_active', 'sell_amount_active', 'updated_at']
    list_filter = ['code', 'year', 'close', 'open', 'high', 'low', 'pct_change', 'swing', 'avg_price', 'turn', 'volume', 'amount', 'buy_amount',
                   'sell_amount', 'buy_volume', 'sell_volume', 'net_buy_amount', 'net_buy_volume', 'net_sell_amount', 'net_sell_volume',
                   'buy_amount_active', 'sell_amount_active', 'updated_at']


class MarginAdmin(object):
    list_display = ['code', 'date', 'purchase_with_borrowed_money', 'repayment_to_broker', 'trading_balance', 'sales_of_borrowed_sec',
                    'repayment_of_borrowed_sec', 'sale_trading_amount', 'sec_lending_balance_volume', 'sec_lending_balance',
                    'trading_and_sec_lending_balance', 'updated_at']
    search_fields = ['code', 'date', 'purchase_with_borrowed_money', 'repayment_to_broker', 'trading_balance', 'sales_of_borrowed_sec',
                     'repayment_of_borrowed_sec', 'sale_trading_amount', 'sec_lending_balance_volume', 'sec_lending_balance',
                     'trading_and_sec_lending_balance', 'updated_at']
    list_filter = ['code', 'date', 'purchase_with_borrowed_money', 'repayment_to_broker', 'trading_balance', 'sales_of_borrowed_sec',
                   'repayment_of_borrowed_sec', 'sale_trading_amount', 'sec_lending_balance_volume', 'sec_lending_balance',
                   'trading_and_sec_lending_balance', 'updated_at']


class MorphologicFactorAdmin(object):
    list_display = ['code', 'date', 'red_three_soldiers', 'hammer', 'hammer_down', 'two_ravens', 'three_ravens', 'morning_star', 'evening_star',
                    'dark_cloud_cover', 'meteor_line', 'three_line_strike', 'southern_samsung', 'be_confronted_with_a_formidable_enemy',
                    'abandoned_infant', 'belt_line', 'cross_pregnancy_line', 'rickshaw_man', 'updated_at']
    search_fields = ['code', 'date', 'red_three_soldiers', 'hammer', 'hammer_down', 'two_ravens', 'three_ravens', 'morning_star', 'evening_star',
                     'dark_cloud_cover', 'meteor_line', 'three_line_strike', 'southern_samsung', 'be_confronted_with_a_formidable_enemy',
                     'abandoned_infant', 'belt_line', 'cross_pregnancy_line', 'rickshaw_man', 'updated_at']
    list_filter = ['code', 'date', 'red_three_soldiers', 'hammer', 'hammer_down', 'two_ravens', 'three_ravens', 'morning_star', 'evening_star',
                   'dark_cloud_cover', 'meteor_line', 'three_line_strike', 'southern_samsung', 'be_confronted_with_a_formidable_enemy',
                   'abandoned_infant', 'belt_line', 'cross_pregnancy_line', 'rickshaw_man', 'updated_at']


class TechnicalFactorAdmin(object):
    list_display = ['code', 'date', 'ma', 'macd', 'kdj', 'rsi', 'bias', 'bbi', 'cci', 'atr', 'trix', 'ema', 'dma', 'boll_up', 'boll_down', 'sar',
                    'si', 'wr', 'cr', 'std', 'vol_ratio', 'updated_at']
    search_fields = ['code', 'date', 'ma', 'macd', 'kdj', 'rsi', 'bias', 'bbi', 'cci', 'atr', 'trix', 'ema', 'dma', 'boll_up', 'boll_down', 'sar',
                     'si', 'wr', 'cr', 'std', 'vol_ratio', 'updated_at']
    list_filter = ['code', 'date', 'ma', 'macd', 'kdj', 'rsi', 'bias', 'bbi', 'cci', 'atr', 'trix', 'ema', 'dma', 'boll_up', 'boll_down', 'sar',
                   'si', 'wr', 'cr', 'std', 'vol_ratio', 'updated_at']


class FinancialFactorAdmin(object):
    list_display = ['code', 'year', 'time', 'eps', 'bps', 'gross_earnings_per_share', 'capital_stock_per_share', 'earnings_per_share',
                    'undistributed_profit_per_share', 'pre_tax_earnings_per_share', 'ebitda', 'pe', 'roe', 'roa', 'roic', 'gross_profit_margin',
                    'net_profit_margin', 'opt_oebt', 'debt_to_assets', 'long_debt_to_long_captial', 'short_debt_to_long_captial',
                    'assets_to_equity', 'fa_current', 'fa_quick', 'fa_cash_to_current_debt', 'fa_debt_to_equity', 'fa_invturn', 'fa_arturn',
                    'fa_assets_turn', 'updated_at']
    search_fields = ['code', 'year', 'time', 'eps', 'bps', 'gross_earnings_per_share', 'capital_stock_per_share', 'earnings_per_share',
                     'undistributed_profit_per_share', 'pre_tax_earnings_per_share', 'ebitda', 'pe', 'roe', 'roa', 'roic', 'gross_profit_margin',
                     'net_profit_margin', 'opt_oebt', 'debt_to_assets', 'long_debt_to_long_captial', 'short_debt_to_long_captial',
                     'assets_to_equity', 'fa_current', 'fa_quick', 'fa_cash_to_current_debt', 'fa_debt_to_equity', 'fa_invturn', 'fa_arturn',
                     'fa_assets_turn', 'updated_at']
    list_filter = ['code', 'year', 'time', 'eps', 'bps', 'gross_earnings_per_share', 'capital_stock_per_share', 'earnings_per_share',
                   'undistributed_profit_per_share', 'pre_tax_earnings_per_share', 'ebitda', 'pe', 'roe', 'roa', 'roic', 'gross_profit_margin',
                   'net_profit_margin', 'opt_oebt', 'debt_to_assets', 'long_debt_to_long_captial', 'short_debt_to_long_captial',
                   'assets_to_equity', 'fa_current', 'fa_quick', 'fa_cash_to_current_debt', 'fa_debt_to_equity', 'fa_invturn', 'fa_arturn',
                   'fa_assets_turn', 'updated_at']


xadmin.site.register(StockInfo, StockInfoAdmin)
xadmin.site.register(HolderInfo, HolderInfoAdmin)
xadmin.site.register(LiquidHolderInfo, LiquidHolderInfoAdmin)
xadmin.site.register(MarketDay, MarketDayAdmin)
xadmin.site.register(MarketWeek, MarketWeekAdmin)
xadmin.site.register(MarketMonth, MarketMonthAdmin)
xadmin.site.register(MarketYear, MarketYearAdmin)
xadmin.site.register(Margin, MarginAdmin)
xadmin.site.register(MorphologicFactor, MorphologicFactorAdmin)
xadmin.site.register(TechnicalFactor, TechnicalFactorAdmin)
xadmin.site.register(FinancialFactor, FinancialFactorAdmin)
