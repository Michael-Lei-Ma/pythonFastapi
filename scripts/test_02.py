# -*- coding: utf-8 -*-

# def setup_function():
#     print(f'执行函数级别前置操作')
#
# def teardown_function():
#     # 后置
#     print(f'执行函数级别后置操作')

def setup():
    print(f'执行函数级别前置操作')

def teardown():
    print(f'执行函数级别后置操作')


def test_example():
    # 测试用例
    print(f'执行测试用例')

