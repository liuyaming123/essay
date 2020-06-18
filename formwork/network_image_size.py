# -*- coding:utf-8 -*-

import io
from PIL import Image
import requests


class PLImage(object):
    def __init__(self, img_url):
        self.url = img_url
        self.content = requests.get(img_url).content
        self.width = 0
        self.height = 0

    def set_size(self):
        tmpIm = io.BytesIO(self.content)
        im = Image.open(tmpIm)
        self.width, self.height = im.size
        return self.width, self.height


pil_image = PLImage('https://pinlantest.blob.core.chinacloudapi.cn/ai-ylt-test/data/marketplace/banner/img/4.png')

print(pil_image.set_size())
