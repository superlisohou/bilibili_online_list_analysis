#!/usr/local/bin/python3
#-*-coding:utf-8-*-

from html.parser import HTMLParser
import re
import argparse

class MyHTMLParser(HTMLParser): 
    def __init__(self):
        HTMLParser.__init__(self)
        self.videos = []
    def handle_starttag(self, tag, attrs):
        if len(attrs) == 0:
            pass
        else:
            variable_list = list(zip(*attrs))[0]
            value_list = list(zip(*attrs))[1]
            
            if tag == 'a' and {'href', 'title'}.issubset(variable_list):
                for (variable, value) in attrs:
                    if variable == 'href' and value.startswith('/video/'):
                        # extract the av number
                        self.videos.append((re.findall(r'^/video/av(.+)/$',value)[0]))
if __name__ == '__main__': 
    
    # read the input data
    parser = argparse.ArgumentParser()
    parser.add_argument('--file_name', type=str)
    args = parser.parse_args()
    
    # extract the av number
    html_code = (open(args.file_name, 'r', encoding = 'UTF-8')).read()
    hp = MyHTMLParser()
    hp.feed(html_code)
    hp.close()
    
    # output to standard stream
    for i in range(20):
        print(args.file_name[:10]+','+str(i+1)+','+hp.videos[i])

