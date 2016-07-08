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
               "Cookie":"BAIDUID=9104BE7084CD8C1F2E226E6CA7420294:FG=1; PSTM=1467360652; BIDUPSID=EE65C5D5057A7AA046A163F8B2AD67A3; TIEBA_USERTYPE=b9c40c85487e87bc8654295f; TIEBAUID=7c2a3158879a6bdfc8f7d338; bdshare_firstime=1467372610395; Hm_lvt_287705c8d9e2073d13275b18dbd746dc=1467393244,1467393344,1467809412,1467809446; Hm_lpvt_287705c8d9e2073d13275b18dbd746dc=1467809446; wise_device=0; TOPMSG=1467945297-0; BDUSS=FFRY1dwV1VOZURTczFsbFhkZ3g1RnlNZVZUODRFaWREcnFQMnZrcGhrWmNucVpYQVFBQUFBJCQAAAAAAAAAAAEAAABtuA8OyfHougAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFwRf1dcEX9XV; H_PS_PSSID=19636_19683_1457_20516_18240_20537_20539_20415_20456_18134_17001_15191_12312_18243; LONGID=235911277 showCardBeforeSign=1",
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
