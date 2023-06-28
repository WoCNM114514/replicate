import numpy as np
from scipy import stats


class BSM:
    def __init__(self, s0, k, t, r, sigma, div=0):
        self.s0 = float(s0) # 标的价格
        self.k = float(k) # 行权价
        self.t = float(t) # 到期时间
        self.r = float(r) # 无风险利率
        self.sigma = float(sigma) # 隐含波动率
        self.div_yield = float(div) # 历史波动率
        self.d1 = ((np.log(self.s0)/self.k) + (self.r-self.div+0.5*self.sigma**2) * self.t) / (self.sigma*np.sqrt(self.t))
        self.d2 = self.d1 - self.sigma*np.sqrt(self.t)

    
    def call_value(self):
        call_value = (self.s0*np.exp(-self.div*self.t)) * stats.norm.cdf(self.d1, 0, 1) - self.k*np.exp(-self.r*self.t) * stats.norm.cdf(self.d2, 0, 1)
        return call_value
    

    def delta(self):
        delta_call = np.exp(-self.div*self.t) * stats.norm.cdf(self.d1, 0, 1)
        delta_put = -np.exp(-self.div*self.t) * stats.norm.cdf(-self.d1, 0, 1)
        return delta_call, delta_put
    

