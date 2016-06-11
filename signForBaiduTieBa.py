# -*- coding: utf-8 -*-

import requests
import re
import time

signWebsite = "http://tieba.baidu.com/f?kw=muv&fr=home&fp=0&ie=utf-8"
wa2ba = "http://tieba.baidu.com/f?kw=%e7%99%bd%e8%89%b2%e7%9b%b8%e7%b0%bf2&fr=home"
lbba = "http://tieba.baidu.com/f?kw=littlebusters&fr=home&fp=0&ie=utf-8"
Galgameba = "http://tieba.baidu.com/f?kw=galgame&fr=home"

def GetNowTime():
    return time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))


def writeLog(state):
    now = GetNowTime()
    state = state.encode('utf-8')
    f = open('galgame_TieBa_Log','a+b')
    f.write(now.encode('utf-8')+" "+state+"\n")
    f.close()
    return


def signForMe(website):
    state = "fail"
    kw_pattern = re.compile("kw=(.*)&fr")
    kwl = re.findall(kw_pattern,website)
    kw = kwl[0]
    # print(kw)
    Gba = requests.get(website)
    text = Gba.text
    # text = str(text.encode("utf-8"))
    p = "'tbs': \"(.*)\""
    tbs = re.findall(p,text)
    # print(tbs)


    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36",
               "Cookie":"BAIDUID=7AC33FCFBADCB07B0528A7C0C6395039:FG=1; BIDUPSID=188F0536043D0040CF4C5A5FE4DDC704; PSTM=1432644105; TIEBA_USERTYPE=39141a92142e8ab7d231778f; bdshare_firstime=1434002412650; TIEBAUID=7c2a3158879a6bdfc8f7d338; pgv_pvi=433069056; BDUSS=k90eFk5ZmZMYXBUWjFveWN1WENoUjVxM0dVSHRRUGhOS1lwY0l2NTd3ZWZuWUJYQVFBQUFBJCQAAAAAAAAAAAEAAABtuA8OyfHougAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAJ8QWVefEFlXZ; H_PS_PSSID=1437_20317_13548_17942_20075_19860_15795_12184_18243; LONGID=235911277; showCardBeforeSign=1",
               'Content-Length':'50',
               'X-Requested-With':'XMLHttpRequest',
               'Referer':website,

               }


    payload = {
        'ie':'utf-8',
        'kw':kw,
        'tbs':tbs[0]
    }

    # print(tbs[0])
    r = requests.post("http://tieba.baidu.com/sign/add",data=payload,headers=headers)
    writeLog(r.json()['error'])
    # print(r.text)
    # print(r.headers)
    # print(r.json()['error'])


signForMe(Galgameba)
