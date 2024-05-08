#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
# File          : common
# Author        : Sun YiFan-Movoid
# Time          : 2024/2/21 19:22
# Description   : 
"""
import requests
from RobotFrameworkBasic import RobotBasic, RfError


class BasicCommon(RobotBasic):
    def requests(self, method, url, status=200, **kwargs):
        self.print(f'try to request')
        response = requests.request(method, url, **kwargs)
        self.print(f'get response success')
        if response.status_code == status:
            return response
        else:
            raise RfError(f'response status is {response.status_code}, not {status}.requests is {method},{url},{kwargs}')

    def post(self, url, status=200, **kwargs):
        return self.requests('POST', url, status, **kwargs)

    def get(self, url, status=200, **kwargs):
        return self.requests('GET', url, status, **kwargs)

    def requests_code(self, method, url, code=0, status=200, **kwargs):
        self.print(f'try to request')
        response = requests.request(method, url, **kwargs)
        self.print(f'get response success')
        if response.status_code == status:
            res_json = response.json()
            if res_json['code'] == code:
                return res_json['data']
            else:
                raise RfError(f'response code is {res_json["code"]}, not {code}.requests is {method},{url},{kwargs}')
        else:
            raise RfError(f'response status is {response.status_code}, not {status}.requests is {method},{url},{kwargs}')

    def post_code(self, url, code=0, status=200, **kwargs):
        return self.requests_code('POST', url, code, status, **kwargs)

    def get_code(self, url, code=0, status=200, **kwargs):
        return self.requests_code('GET', url, code, status, **kwargs)
