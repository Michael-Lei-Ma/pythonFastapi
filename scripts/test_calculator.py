# -*- coding: utf-8 -*-
import allure
import pytest
from tool_page.calculator import Calculator

@allure.feature("计算器")
class TestCalculator:
    @allure.story("加法")
    @allure.title("测试整数加法")
    def test_add(self):
        calc = Calculator()
        assert calc.add(2, 3) == 5

    @allure.story("除法")
    @allure.title("测试正常除法")
    def test_divide_ok(self):
        calc = Calculator()
        assert calc.divide(6, 3) == 2.0

    @allure.story("除法")
    @allure.title("测试除零异常")
    def test_divide_by_zero(self):
        calc = Calculator()
        with pytest.raises(ValueError, match="除数不能为零"):
            calc.divide(5, 0)