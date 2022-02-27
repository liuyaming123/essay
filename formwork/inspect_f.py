# -*- coding:utf-8 -*-
"""自省"""

import inspect
from formwork import process_pool_f


'''找到一个模块中符合条件的函数'''
for name, f in inspect.getmembers(process_pool_f, inspect.isfunction):
    if name.startswith("co"):
        f(100)
