# -*- coding: utf-8 -*-
"""
Created on Sun Nov 03 17:28:17 2013

@author: 子怿
"""

#抽象工厂模式
'''
模式特点：提供一个创建一系列相关或相互依赖对象的接口，而无需指定它们的类。

程序实例：提供对不同的数据库访问的支持。

　　　　　IUser和IDepartment是两种不同的抽象产品，它们都有Access和SQL Server这两种不同的实现；IFactory是产生IUser和IDepartment的抽象工厂，根据具体实现（AccessFactory和SqlFactory）产生对应的具体的对象（CAccessUser与CAccessDepartment，或者CSqlUser与CSqlDepartment）。

代码特点：无
'''

class IUser:
    def GetUser(self):
        pass
    def InsertUser(self):
        pass

class IDepartment:
    def GetDepartment(self):
        pass
    def InsertDepartment(self):
        pass

class CAccessUser(IUser):
    def GetUser(self):
        print "Access GetUser"
    def InsertUser(self):
        print "Access InsertUser"


class CAccessDepartment(IDepartment):
    def GetDepartment(self):
        print "Access GetDepartment"
    def InsertDepartment(self):
        print "Access InsertDepartment"

class CSqlUser(IUser):
    def GetUser(self):
        print "Sql GetUser"
    def InsertUser(self):
        print "Sql InsertUser"


class CSqlDepartment(IDepartment):
    def GetDepartment(self):
        print "Sql GetDepartment"
    def InsertDepartment(self):
        print "Sql InsertDepartment"

class IFactory:
    def CreateUser(self):
        pass
    def CreateDepartment(self):
        pass

class AccessFactory(IFactory):
    def CreateUser(self):
        temp=CAccessUser()
        return temp
    def CreateDepartment(self):
        temp = CAccessDepartment()
        return temp

class SqlFactory(IFactory):
    def CreateUser(self):
        temp = CSqlUser()
        return temp
    def CreateDepartment(self):
        temp = CSqlDepartment()
        return temp

if __name__ == "__main__":
    factory = SqlFactory()
    user=factory.CreateUser()
    depart=factory.CreateDepartment()
    user.GetUser()
    depart.GetDepartment()