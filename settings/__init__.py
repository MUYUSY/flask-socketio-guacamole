# -*- coding: utf-8 -*-
"""
MIT License

Copyright (c) 2019 MUYUSY
"""

import os
from config import config

ENV = os.environ.get('APP_ENV')
config = config[ENV]

# guacd config
GUACD_PATH = config.GUACD_PATH
GUACD_PORT = config.GUACD_PORT
