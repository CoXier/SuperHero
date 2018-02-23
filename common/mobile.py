# coding: utf-8
import os
import sys


def screen_shot():
    """返回截图"""
    screenshot_dir = "{path}/screenshot".format(path=sys.path[0])
    if not os.path.exists(screenshot_dir):
        os.makedirs(screenshot_dir)
    screenshot = os.path.join(screenshot_dir, 'screen.png')
    os.system('adb exec-out screencap -p > {}'.format(str(screenshot)))
    return screenshot
