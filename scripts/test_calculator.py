# -*- coding: utf-8 -*-

class TestClass():
    @classmethod
    def setup_class(cls):
        # 类级别的前置操作
        print("执行类级别的前置操作")

    @classmethod
    def teardown_class(cls):
        # 类级别的后置操作
        print("执行类级别的后置操作")

    def test0021(self):
        print("执行测试用例test0021")

    def test0022(self):
        print("执行测试用例test0022")