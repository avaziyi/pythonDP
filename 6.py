# -*- coding: utf-8 -*-
"""
Created on Sun Nov 03 17:03:52 2013

@author: 子怿
"""

#原型模式
'''
模式特点：用原型实例指定创建对象的种类，并且通过拷贝这些原型创建新的对象。

程序实例：从简历原型，生成新的简历

代码特点：简历类Resume提供的Clone()方法其实并不是真正的Clone，只是为已存在对象增加了一次引用。

　　　　　Python为对象提供的copy模块中的copy方法和deepcopy方法已经实现了原型模式，但由于例子的层次较浅，二者看不出区别。
'''

import copy
class WorkExp:
    place=""
    year=0

class Resume:
    name = ''
    age = 0
    def __init__(self,n):
        self.name = n
    def SetAge(self,a):
        self.age = a
    def SetWorkExp(self,p,y):
        self.place = p
        self.year = y
    def Display(self):
        print self.age
        print self.place
        print self.year
    def Clone(self):
    #实际不是“克隆”，只是返回了自身
        return self

if __name__ == "__main__":
    a = Resume("a")
    b = a.Clone()
    c = copy.copy(a)
    d = copy.deepcopy(a)
    a.SetAge(7)
    b.SetAge(12)
    c.SetAge(15)
    d.SetAge(18)
    a.SetWorkExp("PrimarySchool",1996)
    b.SetWorkExp("MidSchool",2001)
    c.SetWorkExp("HighSchool",2004)
    d.SetWorkExp("University",2007)
    a.Display()
    b.Display()
    c.Display()
    d.Display()