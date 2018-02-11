# -*- coding: utf-8 -*-
from __future__ import print_function

"""
    package.module
    ~~~~~~~~~~~~~~

    url : https://github.com/geekcomputers/Python/blob/master/youtube.py
"""

import webbrowser
import sys
import requests
from bs4 import BeautifulSoup

if sys.version_info[0] < 3:
    input = raw_input

'''
headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'}
'''
query = input('Enter the song to be played: ')

# search for the best similar matching video
url = 'http://www.soku.com/search_video/q_' + query

source_code = requests.get(url, timeout=15)
plain_text = source_code.text
soup = BeautifulSoup(plain_text, "html.parser")

# fetches the url of the video
songs = soup.findAll('div', {'class': 'v-meta-title'})
song = songs[0]
hrefs = song.findAll('a')[0]['href']

if hrefs.startswith('http://'):
    link = hrefs.replace('http://', '')
elif hrefs.startswith('//'):
    link = hrefs.replace('//', '')
else:
    link = hrefs

web = webbrowser.get('safari')
web.open(link)