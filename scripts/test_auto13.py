# -*- coding: utf-8 -*-
def setup_function():
    print("setup_function")


def teardown_function():
    print("teardown_function")

def test_01():
    print("---用例a执行---")

class TestCase():
    def test_02(self):
        print("---用例b执行---")

    def test_03(self):
        print("---用例c执行---")

def test_04():
    print("---用例d执行---")