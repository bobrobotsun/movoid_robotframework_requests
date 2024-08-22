#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
# File          : common
# Author        : Sun YiFan-Movoid
# Time          : 2024/2/21 19:22
# Description   : 
"""
import json

import psutil
import requests
from RobotFrameworkBasic import RobotBasic, RfError


class BasicCommon(RobotBasic):
    def __init__(self):
        super().__init__()
        net_if_addresses = psutil.net_if_addrs()
        network_info = []
        for interface_name, interface_info in net_if_addresses.items():
            for info in interface_info:
                if info.family == 2:  # 只处理IPv4地址
                    network_info.append({'address': info.address, 'netmask': info.netmask})
        self.headers = {
            'Uinetworkinfo': json.dumps(network_info)
        }
        self._request_param = {}

    def requests_ori(self, method, url, status=200, **kwargs):
        kwargs.setdefault('headers', self.headers)
        self._request_param = {'method': method, 'url': url, **kwargs}
        print(f'try to request:{self._request_param}')
        response = requests.request(method, url, **kwargs)
        print(f'get response success')
        if response.status_code == status:
            print(f'response text:{response.text}')
            return response
        else:
            raise RfError(f'response status is {response.status_code}, not {status}.response is {response.text}.requests is {self._request_param}')

    def post_ori(self, url, status=200, **kwargs):
        return self.requests_ori('POST', url, status, **kwargs)

    def get_ori(self, url, status=200, **kwargs):
        return self.requests_ori('GET', url, status, **kwargs)

    def requests(self, method, url, code=0, status=200, **kwargs):
        response = self.requests_ori(method, url, status, **kwargs)
        res_json = response.json()
        if res_json['code'] == code:
            return res_json['data']
        else:
            raise RfError(f'response code is {res_json["code"]}, not {code}.response json is {res_json}.requests is {self._request_param}')

    def post(self, url, code=0, status=200, **kwargs):
        return self.requests('POST', url, code, status, **kwargs)

    def get(self, url, code=0, status=200, **kwargs):
        return self.requests('GET', url, code, status, **kwargs)
