#!/usr/local/bin/python3
#-*- coding: utf-8 -*-
import urllib.request
import gzip
import io 

if __name__ == '__main__':
    # Real time top video being watched should be retrived from the following url
    url = 'https://www.bilibili.com/video/online.html'
    req = urllib.request.Request(url)
    
    # Read html, depress and decode
    html_compressed = urllib.request.urlopen(req).read()
    html_decompressed = gzip.decompress(html_compressed)
    html_decoded = html_decompressed.decode('utf-8')

    # Output to standard stream
    print(html_decoded)

