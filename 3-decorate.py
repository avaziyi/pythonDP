# -*- coding: utf-8 -*-
"""
Created on Sun Nov 03 16:20:10 2013

@author: 子怿
"""

#encoding=utf-8
#
#by panda
#修饰模式

def printInfo(info):
    print unicode(info, 'utf-8').encode('gbk')

class Person():
    name = ""
    
    def __init__(self, name):
        self.name = name;
        return;
    
    def Show(self):
        printInfo("装扮好的%s" % self.name)
        
class Finery(Person):
    component = None
    
    def __init__(self):
        return;
    
    def Decorate(self, component):
        self.component = component
        
    def Show(self):
        if(None != self.component):
            self.component.Show()
            
class TShirts(Finery):
    def Show(self):
        printInfo("大T恤")
        self.component.Show()

class BigTrouser(Finery):
    def Show(self):
        printInfo("裤子")  
        self.component.Show()      


def clientUI():
    xc = Person("小菜")
    bT = BigTrouser()
    TS = TShirts()
    bT.Decorate(xc)
    TS.Decorate(bT)
    TS.Show()
    return

if __name__ == '__main__':
    clientUI();
