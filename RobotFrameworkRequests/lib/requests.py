#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
# File          : requests
# Author        : Sun YiFan-Movoid
# Time          : 2024/1/31 0:07
# Description   : 
"""
from requests import Response

from typing import Dict

from movoid_function import wraps_func
from movoid_function.type import Type
from RobotFrameworkBasic import RfError

import requests


def simple_check_response_status(response_status: int = 200):
    _response_status = 200 if response_status is None else int(response_status)

    def dec(func):
        @wraps_func(func)
        def wrapper(kwargs, check_response_status=_response_status):
            response = func(**kwargs)  # type:Response
            if response.status_code != check_response_status:
                raise RfError(f'response status is {response.status_code} != {check_response_status}')
            return response

        return wrapper

    return dec


def simple_check_response_json_code(response_json_code: int = 0):
    _response_json_code = 200 if response_json_code is None else int(response_json_code)

    def dec(func):
        @wraps_func(func)
        def wrapper(kwargs, check_response_json_code=_response_json_code):
            response = func(**kwargs)  # type:Response
            response_json = response.json()
            if response_json['code'] != check_response_json_code:
                raise RfError(f'response json code is {response_json["code"]} != {check_response_json_code}')
            return response_json

        return wrapper

    return dec


def auto_requests_check_parameter_and_response(url: str, method: str = 'post'):
    def dec(func):
        annotations = func.__annotations__
        param_annotations: Dict[str, TypeRequest] = {i: v for i, v in annotations.items() if isinstance(v, TypeRequest) and i != 'return'}

        @wraps_func(func)
        def wrapper(kwargs):
            request_dict = {}
            for i, v in param_annotations.items():
                print(v.position)
                request_key = v.position
                request_dict.setdefault(request_key, {})
                request_dict[request_key][i] = kwargs[i]
            response = requests.request(method, url, **request_dict)
            if 'return' in annotations:
                return_type = annotations['return']
                if isinstance(return_type, TypeResponse):
                    return_type.check(response)

        for i, v in annotations.items():
            if isinstance(v, Type):
                annotations[i] = v.annotation
        wrapper.__annotations__ = {i: v.annotation for i, v in annotations.items() if isinstance(v, Type)}
        return wrapper

    return dec
