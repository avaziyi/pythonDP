# -*- coding: utf-8 -*-
"""
Created on Sun Nov 03 16:32:12 2013

@author: 子怿
"""
'''
这里的decorate是Python的装饰器，不是DP的decorate pattern
'''
def whatIsLiving():
  print u'对啊，怎样才算活着呢？'

print '0'
whatIsLiving()

print

def eat(fun):
  def living():
    print 'living-eat'
    fun()
    print u'活着就是吃嘛。'
  return living

whatIsLiving2 = eat(whatIsLiving)
print whatIsLiving2
print '1'
whatIsLiving2()

print

def sleep(fun):
  def living():
    fun()
    print u'活着还包括睡嘛。'
  return living

whatIsLiving = sleep(whatIsLiving)
print '2'
whatIsLiving()