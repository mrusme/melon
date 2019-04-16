#!/usr/bin/env python3
# coding=utf8

from py_irsend import irsend

# https://github.com/ChristopherRogers1991/python-irsend
class Irda:
    def __init__(self):
        print("Irda initialized!")

    def do(self, params):
        irsend.send_once(params['device'], params['key'])
