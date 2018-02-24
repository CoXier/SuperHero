# coding: utf-8
import os
import sys
from PIL import Image
import io
import base64

from config.config import open_accordant_config


class Mobile(object):
    _position = (0, 0, 0, 0)

    def __init__(self, app_name):
        data = open_accordant_config(app_name)
        self._position = (data.get("left"), data.get("top"), data.get("right"), data.get("bottom"))
        pass

    def screen_shot(self):
        """返回截图"""
        screenshot_dir = "{path}/screenshot".format(path=sys.path[0])
        if not os.path.exists(screenshot_dir):
            os.makedirs(screenshot_dir)
        screenshot = os.path.join(screenshot_dir, 'screen.png')
        os.system('adb exec-out screencap -p > {}'.format(str(screenshot)))
        im = Image.open(screenshot)
        region = im.crop(self._position)
        with io.BytesIO() as tmp_file:
            region.save(tmp_file, format="PNG")
            ls_f = base64.b64encode(tmp_file.getvalue())
            s = bytes.decode(ls_f)
        return s
