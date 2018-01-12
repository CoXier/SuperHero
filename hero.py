# coding: utf-8
import requests
import base64
import os
import time
import urllib
from PIL import Image

start = time.time()
current_dir = os.path.dirname(__file__)
screenshot_dir = os.path.join(current_dir, "screenshot")
if not os.path.exists(screenshot_dir):
    os.makedirs(screenshot_dir)
screenshot = os.path.join(screenshot_dir, 'screen.png')
os.system('adb exec-out screencap -p > {}'.format(str(screenshot)))
url = 'https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic'

im = Image.open(screenshot)

img_size = im.size
w = im.size[0]
h = im.size[1]

region = im.crop((130, 360, w, 730))
clip_image = os.path.join(screenshot_dir, 'clip.png')
region.save(clip_image)

f = open(clip_image, 'rb')
ls_f = base64.b64encode(f.read())
f.close()
s = bytes.decode(ls_f)

post_body = {
    "image": s,
    "language_type":'CHN_ENG',
}
headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
}
params = {
    'access_token': '24.a2ab2e0cadef8bec9b0404e2073d43c8.2592000.1518349462.282335-10682596'
}
response = requests.post(url, data=post_body, headers=headers, params=params).json()
question_text = u' '
for words_dict in response['words_result']:
    words = words_dict.get('words')
    question_text += words
question_text = str(question_text.encode('utf-8')).strip()
print(question_text)
command = "open -a Google\ Chrome http://www.baidu.com/s\?wd\=" + urllib.quote_plus(question_text)
print(command)
os.system(command)
end = time.time()
print('Time:{}s'.format(str((end - start) / 1000)))

