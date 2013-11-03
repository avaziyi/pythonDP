# -*- coding: utf-8 -*-
"""
Created on Sun Nov 03 17:09:19 2013

@author: 子怿
"""

#外观模式
'''
模式特点：为一组调用提供一致的接口。

程序实例：接口将几种调用分别组合成为两组，用户通过接口调用其中的一组。

代码特点：无
'''

class SubSystemOne:
    def MethodOne(self):
        print "SubSysOne"

class SubSystemTwo:
    def MethodTwo(self):
        print "SubSysTwo"

class SubSystemThree:
    def MethodThree(self):
        print "SubSysThree"

class SubSystemFour:
    def MethodFour(self):
        print "SubSysFour"


class Facade:
    def __init__(self):
        self.one = SubSystemOne()
        self.two = SubSystemTwo()
        self.three = SubSystemThree()
        self.four = SubSystemFour()
    def MethodA(self):
        print "MethodA"
        self.one.MethodOne()
        self.two.MethodTwo()
        self.four.MethodFour()
    def MethodB(self):
        print "MethodB"
        self.two.MethodTwo()
        self.three.MethodThree()

if __name__ == "__main__":
    facade = Facade()
    facade.MethodA()
    facade.MethodB()