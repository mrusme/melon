#!/usr/bin/env python3
# coding=utf8

from soco import SoCo
import socket

# http://docs.python-soco.com/en/latest/getting_started.html
class SpeakerSonos:
    def __init__(self):
        print("SpeakerSonos initialized!")

    def do(self, params):
        speaker = SoCo(socket.gethostbyname(params['host']))
        print(speaker.groups)

        if 'volume' in params:
            speaker.volume = params['volume']

        if 'clear_queue' in params:
            speaker.clear_queue()

        if 'add_playlist_id_to_queue' in params:
            playlist = speaker.get_sonos_playlists()[params['add_playlist_id_to_queue']]
            speaker.add_uri_to_queue(playlist.resources[0].uri)

        if 'switch_to_tv' in params:
            speaker.switch_to_tv()

        if 'next' in params:
            speaker.next()
        elif 'previous' in params:
            speaker.previous()

        if 'play' in params:
            speaker.play()
        elif 'pause' in params:
            speaker.pause()

        if 'set_sleep_timer' in params:
            speaker.set_sleep_timer(params['set_sleep_timer'] * 60)
