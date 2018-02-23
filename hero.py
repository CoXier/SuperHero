# coding: utf-8
import base64
import time
from PIL import Image
import io

from common import mobile
from core import image_parser
from core import baidu_search


def _start():
    start = time.time()
    screenshot = mobile.screen_shot()
    im = Image.open(screenshot)
    region = im.crop((160, 340, 1024, 650))
    with io.BytesIO() as tmp_file:
        region.save(tmp_file, format="PNG")
        ls_f = base64.b64encode(tmp_file.getvalue())
        s = bytes.decode(ls_f)

    # 调用百度文字识别
    question_text = image_parser.parse(s)
    question_text = str(question_text.encode('utf-8')).strip()
    print(question_text)

    # 打开浏览器搜索
    baidu_search.open(question_text)

    end = time.time()
    print('Time:{}s'.format(str((end - start))))


if __name__ == '__main__':
    _start()
