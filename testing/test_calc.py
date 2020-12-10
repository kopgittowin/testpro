#!/usr/bin/env python
# -*- coding: utf-8 -*-
import allure
import pytest
import yaml
from python_code.calc import Calculator


@allure.feature('测试计算器')
class Test_Calc:

    # def setup_class(self):
    #     # 实例化计算器类
    #     print('开始计算')
    #     self.calc = Calculator()
    #
    # def teardown_class(self):
    #     print('结束计算')

    # @pytest.mark.parametrize(
    #     'a, b, expected',
    #     add_data, ids=add_ids
    # )
    @pytest.mark.run(order=1)
    @allure.story('测试加法')
    def test_add(self, get_calc, get_add_datas):
        result = None
        # 调用 add 方法
        try:
            with allure.step('计算两数相加的和'):
                result = get_calc.add(get_add_datas[0], get_add_datas[1])
            if isinstance(result, float):
                result = round(result, 2)
        except Exception as e:
            print(e)
        # 得到结果之后，需要写断言
        assert result == get_add_datas[2]

    # @pytest.mark.parametrize(
    #     'c, d, expected_div',
    #     div_data, ids=div_ids
    # )
    @pytest.mark.run(order=4)
    @allure.story('测试除法')
    def test_div(self, get_calc, get_div_datas):
        result = None
        # 调用 div方法
        try:
            with allure.step('计算两数相除'):
                result = get_calc.div(get_div_datas[0], get_div_datas[1])
            if isinstance(result, float):
                result = round(result, 2)
        except Exception as e:
            print(e)
        assert result == get_div_datas[2]

    @pytest.mark.run(order=2)
    @allure.story('测试减法')
    def test_sub(self, get_calc, get_sub_datas):
        result = None
        # 调用 div方法
        try:
            with allure.step('计算两数相减'):
                result = get_calc.sub(get_sub_datas[0], get_sub_datas[1])
            if isinstance(result, float):
                result = round(result, 2)
        except Exception as e:
            print(e)
        assert result == get_sub_datas[2]

    @pytest.mark.run(order=3)
    @allure.story('测试乘法')
    def test_mul(self, get_calc, get_mul_datas):
        result = None
        # 调用 mul方法
        try:
            with allure.step('计算两数相乘'):
                result = get_calc.mul(get_mul_datas[0], get_mul_datas[1])
            if isinstance(result, float):
                result = round(result, 2)
        except Exception as e:
            print(e)
        assert result == get_mul_datas[2]
