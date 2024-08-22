#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
# File          : __init__.py
# Author        : Sun YiFan-Movoid
# Time          : 2024/2/21 19:24
# Description   : 
"""
from RobotFrameworkBasic import robot_log_keyword
from movoid_function import decorate_class_function_exclude

from .action import RequestsAction


@decorate_class_function_exclude(robot_log_keyword, '^_')
class RobotRequestsBasic(RequestsAction):
    pass
