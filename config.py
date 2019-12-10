# -*- coding: utf-8 -*-
"""
MIT License

Copyright (c) 2019 MUYUSY
"""

import os
import logging
from logging.handlers import TimedRotatingFileHandler

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class BaseConfig:
    LOG_PATH = os.path.join(BASE_DIR, 'logs')
    LOG_PATH_INFO = os.path.join(LOG_PATH, 'log.log')

    def __init__(self):
        log_path = os.path.join(BASE_DIR, 'logs')
        if not os.path.exists(log_path):
            os.makedirs(log_path)

    @classmethod
    def init_app(cls, app):
        # Formatter
        formatter = logging.Formatter(
            '%(asctime)s %(levelname)s %(process)d %(thread)d %(threadName)s '
            '%(pathname)s %(lineno)s %(message)s')

        file_handler_info = TimedRotatingFileHandler(
            filename=cls.LOG_PATH_INFO, when="D", interval=1, backupCount=30)
        file_handler_info.suffix = "%Y-%m-%d.log"
        file_handler_info.setFormatter(formatter)
        file_handler_info.setLevel(logging.INFO)
        app.logger.addHandler(file_handler_info)


class DevelopConfig(BaseConfig):
    DEBUG = True
    GUACD_PATH = 'localhost'
    GUACD_PORT = 4822


class ProductConfig(BaseConfig):
    DEBUG = False


config = {
    'develop': DevelopConfig(),
    'product': ProductConfig()
}
