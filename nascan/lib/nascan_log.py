# coding:utf-8
# author:daniel
import logging
import logging.config

logging.config.fileConfig('nascan-log.conf')
logger = logging.getLogger('nascan')
