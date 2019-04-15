#!/usr/bin/env python3
# coding=utf8

from phue import Bridge

# https://github.com/studioimaginaire/phue
class SmarthomeHue:
    def __init__(self):
        print("SmarthomeHue initialized!")

    def do(self, params):
        hue = Bridge(params['host'])
        hue.connect()

        if 'on' in params:
            hue.set_light(params['lights'], 'on', params['on'])

        if 'brightness' in params:
            hue.set_light(params['lights'], 'bri', params['brightness'])

        if 'hue' in params:
            hue.set_light(params['lights'], 'hue', params['hue'])

        if 'saturation' in params:
            hue.set_light(params['lights'], 'sat', params['saturation'])
