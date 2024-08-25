#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
# File          : test_init
# Author        : Sun YiFan-Movoid
# Time          : 2024/8/18 1:08
# Description   : 
"""
from RobotFrameworkRequests import RobotFrameworkRequests, RobotRequestsBasic


class Test_init:
    def test_init(self):
        rfr = RobotFrameworkRequests()
        rrb = RobotRequestsBasic()
        rrb.get_ori('http://www.baidu.com')
