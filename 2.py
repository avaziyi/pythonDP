# -*- coding: utf-8 -*-
"""
Created on Sun Nov 03 15:52:18 2013

@author: 子怿
"""

#策略模式
'''
模式特点：定义算法家族并且分别封装，它们之间可以相互替换而不影响客户端。

程序实例：商场收银软件，需要根据不同的销售策略方式进行收费

代码特点：不同于同例1，这里使用字典是为了避免关键字不在字典导致bug的陷阱。
'''

class CashSuper:
    def AcceptCash(self,money):
        return 0

class CashNormal(CashSuper):
    def AcceptCash(self,money):
        return money

class CashRebate(CashSuper):
    discount = 0
    def __init__(self,ds):
        self.discount = ds
    def AcceptCash(self,money):
        return money * self.discount

class CashReturn(CashSuper):
    total = 0;
    ret = 0;
    def __init__(self,t,r):
        self.total = t
        self.ret = r
    def AcceptCash(self,money):
        if (money>=self.total):
            return money - self.ret
        else:
            return money

class CashContext:
    def __init__(self,csuper):
        self.cs = csuper
    def GetResult(self,money):
        return self.cs.AcceptCash(money)

if __name__ == "__main__":
    money = input("money:")
    strategy = {}
    strategy[1] = CashContext(CashNormal())
    strategy[2] = CashContext(CashRebate(0.8))
    strategy[3] = CashContext(CashReturn(300,100))
    ctype = input("type:[1]for normal,[2]for 80% discount [3]for 300 -100.\ninput:")
    if ctype in strategy:
        cc = strategy[ctype]
    else:
        print "Undefine type.Use normal mode."
        cc = strategy[1]
    print "you will pay:%d" %(cc.GetResult(money))