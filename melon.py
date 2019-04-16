#!/usr/bin/env python3
# coding=utf8

import os
import falcon

from middleware_json import MiddlewareJson

from resource_api import ResourceApi
from resource_shortcuts import ResourceShortcuts
from resource_shortcuts import ResourceShortcutTriggers

class Melon:
    def __init__(self):
        self._app = falcon.API(middleware=[
            MiddlewareJson(),
        ])

        self._api = ResourceApi()
        self._app.add_route('/api', self._api)

        self._shortcuts = ResourceShortcuts()
        self._app.add_route('/shortcuts/{shortcut_id}', self._shortcuts)

        self._shortcuts = ResourceShortcutTriggers(api=self._api)
        self._app.add_route('/triggers/{shortcut_id}', self._shortcuts)

melon = Melon()
app = melon._app
