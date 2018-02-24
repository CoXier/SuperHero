# coding: utf-8
import time

from common import argparser
from core import image_parser
from core import baidu_search

from common.mobile import Mobile
from pynput import keyboard

mobile = None


def _start():
    start_time = time.time()
    s = mobile.screen_shot()
    # 调用百度文字识别
    question_text = image_parser.parse(s)
    question_text = str(question_text.encode('utf-8')).strip()
    print(question_text)

    # 打开浏览器搜索
    baidu_search.open(question_text)

    end_time = time.time()
    print('Time:{}s'.format(str((end_time - start_time))))


def on_press(key):
    if key == keyboard.Key.esc:
        return False
    else:
        _start()


if __name__ == '__main__':
    app_name = argparser.parse_args()
    mobile = Mobile(app_name)
    with keyboard.Listener(
            on_press=on_press) as listener:
        listener.join()
