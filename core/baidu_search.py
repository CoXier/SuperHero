# coding: utf-8
import webbrowser
import urllib


def open(key_word):
    webbrowser.open('https://m.baidu.com/s?word=' + urllib.quote_plus(key_word))
