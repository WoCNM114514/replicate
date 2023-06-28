import numpy as np
import scipy.stats as si
import pandas as pd
from scipy.stats import norm
import matplotlib.pyplot as plt
import datetime
from bsm import *
import jqdatasdk
from jqdatasdk import *


class DeltaDynamicHedging:
    '''
    PnL ≈ (gamma/2) * (dS)^2 + theta * dt
    '''
    def __init__(self) :
        pass


    def month_get(self, start_date, end_date): # 获取交易时间和时间间隔（频率：月）
        '''
        start_date: string, 起始日期
        end_date: string, 结束日期
        '''
        # Get trading days and month splits
        trade_days = pd.Series(index=get_trade_days(start_date, end_date))
        trade_days.index = pd.to_datetime(trade_days.index)
        month_split = list(trade_days.resample('M', label='left').mean().index) + [pd.to_datetime('20230615')]
        return trade_days, month_split
 