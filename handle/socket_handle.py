# -*- coding: utf-8 -*-
"""
MIT License

Copyright (c) 2019 MUYUSY
"""

from flask_socketio import Namespace, emit
from flask import current_app
from guacamole.client import GuacamoleClient
from settings import GUACD_PATH, GUACD_PORT


class MainNamespace(Namespace):
    def __init__(self, namespace):
        super(MainNamespace, self).__init__(namespace)
        self.remote_ip = None
        self.remote_protocol = None
        self.remote_port = None
        self.username = None
        self.width = None
        self.height = None
        self.password = None
        self.client = None
        self.connect_status = False

    def on_connect(self):
        current_app.logger.debug('Socket connected.')
        self.client = GuacamoleClient(GUACD_PATH, GUACD_PORT)

    def on_disconnect(self):
        self.client.close()

    def on_remote(self, data):
        print('111')
        self.remote_ip = data.get('ip')
        self.remote_protocol = data.get('protocol')
        self.remote_port = data.get('port')
        self.width = data.get('width')
        self.height = data.get('height')
        self.username = data.get('username')
        self.password = data.get('password')

        if self.username and self.password:
            self.client.handshake(protocol='ssh', hostname='47.104.100.145', port=22,
                                  width=self.width, height=self.height,
                                  username=self.username, password=self.password)
        else:
            self.client.handshake(protocol='ssh', hostname='47.104.100.145', port=22,
                                  width=self.width, height=self.height)
        self.connect_status = True
        # emit('connect_status', {'status': self.connect_status}, Namespace='/data')
        while True:
            instruction = self.client.receive()
            if instruction:
                if 'disconnect' in instruction:
                    emit('connect_status', {'status': False}, Namespace='/data')
                    break
                emit('message', instruction, namespace='/data')

    def on_message(self, message):
        if self.connect_status:
            self.client.send(message)
