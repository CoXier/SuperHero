# coding: utf-8
import requests
import base64
import os
import time
from PIL import Image

start = time.time()
current_dir = os.path.dirname(__file__)
screenshot_dir = os.path.join(current_dir, "screenshot")
if not os.path.exists(screenshot_dir):
    os.makedirs(screenshot_dir)
screenshot = os.path.join(screenshot_dir, 'screen.png')
os.system('adb exec-out screencap -p > {}'.format(str(screenshot)))
host = 'http://text.aliapi.hanvon.com'
path = '/rt/ws/v1/ocr/text/recg'
app_code = '7a32570c04784095a3fccc12cae98b1a' # put your appcode here
code = 'code=74e51a88-41ec-413e-b162-bd031fe0407e'
url = host + path + "?" + code

im = Image.open(screenshot)

img_size = im.size
w = im.size[0]
h = im.size[1]

region = im.crop((160, 340, w, 650))
clip_image = os.path.join(screenshot_dir, 'clip.png')
region.save(clip_image)

f = open(clip_image, 'rb')
ls_f = base64.b64encode(f.read())
f.close()
s = bytes.decode(ls_f)

post_body = "{\"uid\":\"118.12.0.12\",\"lang\":\"chns\",\"color\":\"color\",\"image\":\"" + s + "\"}"
headers = {
    'Content-Type': 'application/octet-stream',
    'Authorization': 'APPCODE ' + app_code
}

response = requests.post(url, data=post_body, headers=headers).json()
result = response['textResult'].encode('utf-8')
result = ''.join(result.split())
print("question:{}".format(result))

os.system("open -a Google\ Chrome http://www.baidu.com/s\?wd\={}".format(result))
end = time.time()
print('Time:{}s'.format(str((end - start) / 1000)))

