#!/usr/bin/env python3
# coding=utf8

import falcon
import importlib

class ResourceApi(object):
    def __init__(self):
        self._loaded_modules = {}

    def on_post(self, req, resp):
        if req.context['request']:
            body = req.context['request']
            print(body)

            if 'do' in body:
                return_status = falcon.HTTP_204

                for idx in range(0, len(body['do'])):
                    do_entry = body['do'][idx]

                    if 'module' not in do_entry:
                        return_status = falcon.HTTP_400
                        break

                    module_name = do_entry['module']
                    module_name_cc = module_name.title().replace(" ", "").replace("-", "").replace("_", "")

                    if ("plugins." + module_name) not in globals() and module_name_cc not in self._loaded_modules:
                        module_path = "plugins." + module_name
                        module_object = importlib.import_module(module_path)
                        self._loaded_modules[module_name_cc] = getattr(module_object, module_name_cc)()

                    self._loaded_modules[module_name_cc].do(do_entry)

                resp.status = return_status
            else:
                resp.status = falcon.HTTP_400
        else:
            resp.status = falcon.HTTP_500
