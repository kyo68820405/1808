import re
import os
import wget
from urllib.error import HTTPError

def get_url(fname, patt, encoding=None):
    url_list = []
    cpatt = re.compile(patt)
    with open(fname) as fobj:
        for line in fobj:
            for m in cpatt.finditer(line):    # [匹配对象，匹配对象]
                url_list.append(m.group())
    return url_list

if __name__ == '__main__':
    net_url = 'http://pic.sogou.com/pics?query=%E5%A4%A7%E9%B1%BC%E6%B5%B7%E6%A3%A0%E5%A3%81%E7%BA%B8&ie=utf-8&bh=1&w=05002600'
    fname = '/tmp/dayu.html'
    url_patt = '(http|https)://[-\w./]+\.(png|jpg|jpeg|gif)'
    wget.download(net_url, fname)
    url_list = get_url(fname, url_patt)
    folder = '/tmp/dayu/'   # 保存图片的本地目录
    if not os.path.exists(folder):
        os.mkdir(folder)
    for url in url_list:
        try:
            wget.download(url, folder)
        except HTTPError:
            print(url)
