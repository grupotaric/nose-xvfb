#-*- coding: utf-8 -*-

import logging

from nose.plugins import Plugin
from xvfbwrapper import Xvfb as XvfbWrapper

logger = logging.getLogger('nose.plugins.xvfb')


class Xvfb(Plugin):
    def begin(self):
        logger.info('Starting xvfb virtual display 1024x768')
        self.vdisplay = XvfbWrapper(width=1024, height=768)
        self.vdisplay.start()

    def finalize(self, result):
        logger.info('Stopping xvfb virtual display')
        self.vdisplay.stop()
