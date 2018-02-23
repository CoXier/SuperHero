# coding: utf-8
import requests

url = 'https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic'
headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
}
params = {
    'access_token': '24.3943efe74848f2cacab6342a9649f0de.2592000.1521121428.282335-10682596'
}


def parse(image_decode):
    post_body = {
        "image": image_decode,
        "language_type": 'CHN_ENG',
    }
    response = requests.post(url, data=post_body, headers=headers, params=params).json()
    question_text = u' '
    for words_dict in response['words_result']:
        words = words_dict.get('words')
        question_text += words
    return question_text
