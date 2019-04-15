#!/usr/bin/env python3
# coding=utf8

import os
import falcon

from middleware_json import MiddlewareJson

from resource_api import ResourceApi

class Melon:
    def __init__(self):
        self._app = falcon.API(middleware=[
            MiddlewareJson(),
        ])

        self._api = ResourceApi()
        self._app.add_route('/api', self._api)

melon = Melon()
app = melon._app
