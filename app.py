# -*- coding: utf-8 -*-
"""
MIT License

Copyright (c) 2019 MUYUSY
"""
import os
import sys

if not os.environ.get('APP_ENV'):
    os.environ.setdefault('APP_ENV', 'develop')
APP_ENV = os.environ.get('APP_ENV')


from flask import Flask, render_template
from flask_socketio import SocketIO
from config import config
from handle.socket_handle import MainNamespace


def main(config_name):
    if getattr(sys, 'frozen', False):
        template_folder = os.path.join(sys._MEIPASS, 'templates')
        static_folder = os.path.join(sys._MEIPASS, 'static')
        app = Flask(__name__, template_folder=template_folder, static_folder=static_folder, static_url_path='')
    else:
        app = Flask(__name__)
    app.config.from_object(config[config_name])
    socketio = SocketIO(app)
    socketio.init_app(app)

    @app.route('/')
    def index():
        return render_template('index.html')

    socketio.on_namespace(MainNamespace('/data'))

    return socketio, app


if __name__ == '__main__':
    socketio, app = main(config_name=APP_ENV)
    socketio.run(app)

