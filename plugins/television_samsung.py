#!/usr/bin/env python3
# coding=utf8

import samsungctl
import time

# https://github.com/Ape/samsungctl
class TelevisionSamsung:
    def __init__(self):
        print("TelevisionSamsung initialized!")

    def do(self, params):
        config = {
            "name": "melon",
            "description": "Melon",
            "id": "melon",
            "host": params['host'],
            "port": (params['port'] if 'port' in params else 55000),
            "method": (params['method'] if 'method' in params else "legacy"),
            "timeout": 10,
        }

        with samsungctl.Remote(config) as remote:
            remote.control(params['key'])
            time.sleep(0.5)
