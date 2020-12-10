#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import os
import yaml

from python_code.calc import Calculator


@pytest.fixture(scope='session')
def connectDB():
    print('连接数据库')
    yield
    print('断开数据库')


@pytest.fixture(scope='class')
def get_calc():
    print('获取计算器实例')
    calc = Calculator()
    return calc


# 获取当前文件所在的绝对路径
yml_file_path = os.path.dirname(__file__) + '/datas/calc.yml'

with open(yml_file_path, encoding='utf-8') as f:
    datas = yaml.safe_load(f)
    datas_add = datas['add']
    add_data = datas_add['datas']
    add_ids = datas_add['myid_add']
    datas_div = datas['div']
    div_data = datas_div['datas_div']
    div_ids = datas_div['myid_div']
    datas_sub = datas['sub']
    sub_data = datas_sub['datas_sub']
    sub_ids = datas_sub['myid_sub']
    datas_mul = datas['mul']
    mul_data = datas_mul['datas_mul']
    mul_ids = datas_mul['myid_mul']


@pytest.fixture(params=add_data, ids=add_ids)
def get_add_datas(request):
    print('开始加法计算')
    data = request.param
    print(f'add方法测试数据{data}')
    yield data
    print('结束计算')


@pytest.fixture(params=div_data, ids=div_ids)
def get_div_datas(request):
    print('开始除法计算')
    data = request.param
    print(f'div方法测试数据{data}')
    yield data
    print('结束计算')


@pytest.fixture(params=sub_data, ids=sub_ids)
def get_sub_datas(request):
    print('开始减法计算')
    data = request.param
    print(f'sub方法测试数据{data}')
    yield data
    print('结束计算')


@pytest.fixture(params=mul_data, ids=mul_ids)
def get_mul_datas(request):
    print('开始乘法计算')
    data = request.param
    print(f'mul方法测试数据{data}')
    yield data
    print('结束计算')


def pytest_collection_modifyitems(session, config, items):
    '''called after collection is completed.
    you can modify the ``items`` list
    :param _pytest.main.Session session: the pytest session object
    :param _pytest.config.Config config: pytest config object
    :param List[_pytest.nodes.Item] items: list of item objects
    '''
    print('items')
    print(items)
    items.reverse()

    # 修改测试用例编码格式
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')
