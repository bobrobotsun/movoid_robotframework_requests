#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
# File          : type
# Author        : Sun YiFan-Movoid
# Time          : 2024/1/30 23:00
# Description   : 
"""
from movoid_function.type import Type, TypeInt, TypeDict
from abc import ABC, abstractmethod

from requests import Response


class TypeRequest(Type, ABC):
    def __init__(self, position='body', convert=True, **kwargs):
        super().__init__(convert=convert, **kwargs)
        self.position = position


class TypeResponse(Type, ABC):
    def __init__(self, convert=True, status=200, **kwargs):
        super().__init__(convert=convert, **kwargs)
        self.status = status

    @abstractmethod
    def check(self, response) -> bool:
        pass


class TypeRequestInt(TypeRequest, TypeInt):
    def __init__(self, position='body', limit='', convert=True, **kwargs):
        super().__init__(position=position, limit=limit, convert=convert, **kwargs)


class TypeResponseJson(TypeResponse, TypeDict):
    def __init__(self, length='', convert=False, status=200, code=0, **kwargs):
        super().__init__(length=length, convert=convert, status=status, **kwargs)
        self.code = code

    def check(self, response: Response) -> bool:
        res_status = response.status_code
        if res_status != self.status:
            raise Exception(f'错误的http状态码：{res_status}，预期为：{self.status}')
        if self.code is not None:
            res_json = response.json()
            res_code = res_json['code']
            if res_code != self.code:
                raise Exception(f'错误的结果码：{res_code}，预期为：{self.code}')
        return True
