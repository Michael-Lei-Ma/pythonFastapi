# -*- coding: utf-8 -*-
# file name：test001.py
import pytest


@pytest.mark.smoke
def test_login():
    # 测试登录功能
    assert True


@pytest.mark.regression
def test_registration():
    # 测试注册功能
    assert True


@pytest.mark.smoke
def test_add_to_cart():
    # 测试添加到购物车功能
    assert True


@pytest.mark.regression
def test_checkout():
    # 测试结账功能
    assert True


@pytest.mark.skip  #标记为跳过的用例
def test001():
    print("001")

@pytest.mark.hailey
def test_test_002():
    print("添加一个标签后然后运行")