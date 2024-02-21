#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
# File          : __init__.py
# Author        : Sun YiFan-Movoid
# Time          : 2024/1/30 21:16
# Description   : 
"""
from .main import RobotRequestsBasic
from .lib import simple_check_response_json_code, simple_check_response_status


class RobotFrameworkSelenium(RobotRequestsBasic):
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
