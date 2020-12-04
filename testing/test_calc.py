#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import yaml

from python_code.calc import Calculator

with open('./datas/calc.yml', encoding='utf-8') as f:
    datas = yaml.safe_load(f)
    datas_add = datas['add']
    add_data = datas_add['datas']
    add_ids = datas_add['myid_add']
    datas_div = datas['div']
    div_data = datas_div['datas_div']


class TestCalc_add:

    def setup_class(self):
        # 实例化计算器类
        print('开始计算：验证加法')
        self.calc = Calculator()

    def teardown_class(self):
        print('结束计算：验证加法')

    @pytest.mark.parametrize(
        'a, b, expected',
        add_data, ids=add_ids
    )
    def test_add(self, a, b, expected):
        # 调用 add 方法
        result = self.calc.add(a, b)
        if isinstance(result, float):
            result = round(result, 2)
        # 得到结果之后，需要写断言
        assert result == expected


class TestCalc_div:

    def setup_class(self):
        # 实例化计算器类
        print('开始计算：验证除法')
        self.calc = Calculator()

    def teardown_class(self):
        print('结束计算：验证除法')

    @pytest.mark.parametrize(
        'c, d, expected_div',
        div_data
    )
    def test_sub(self, c, d, expected_div):
        # 调用 div方法
        result = self.calc.div(c, d)
        if isinstance(result, float):
            result = round(result, 2)
        assert result == expected_div
