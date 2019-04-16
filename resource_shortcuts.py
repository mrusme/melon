#!/usr/bin/env python3
# coding=utf8

import falcon
from tinydb import TinyDB, Query
import os

DB_SHORTCUTS = os.getenv("MELON_DB_SHORTCUTS", "melon-shortcuts.json")

class ResourceShortcuts(object):
    def __init__(self):
        self._db = TinyDB(DB_SHORTCUTS)

    def on_post(self, req, resp, shortcut_id):
        if req.context['request']:
            body = req.context['request']
            if 'do' in body:
                Shortcut = Query()
                self._db.upsert({'id': shortcut_id, 'do': body['do']}, Shortcut.id == shortcut_id)

                resp.status = falcon.HTTP_204
            else:
                resp.status = falcon.HTTP_400
        else:
            resp.status = falcon.HTTP_500

    def on_get(self, req, resp, shortcut_id):
        Shortcut = Query()
        shortcut = self._db.search(Shortcut.id == shortcut_id)

        if len(shortcut) == 1:
            resp.context['response'] = { 'do': shortcut[0]['do'] }
            resp.status = falcon.HTTP_200
        else:
            resp.status = falcon.HTTP_404

    def on_delete(self, req, resp, shortcut_id):
        Shortcut = Query()
        shortcut = self._db.search(Shortcut.id == shortcut_id)

        if len(shortcut) == 1:
            self._db.remove(doc_ids=[shortcut[0].doc_id])
            resp.status = falcon.HTTP_204
        else:
            resp.status = falcon.HTTP_404

class ResourceShortcutTriggers(object):
    def __init__(self, api=None):
        self._db = TinyDB(DB_SHORTCUTS)
        self._api = api

    def on_get(self, req, resp, shortcut_id):
        Shortcut = Query()
        shortcut = self._db.search(Shortcut.id == shortcut_id)

        if len(shortcut) == 1:
            resp.status = self._api.do_do(shortcut[0])
        else:
            resp.status = falcon.HTTP_404
