

import requests
import time
import random
import os
import re


bvids = []

bvids_bilibili_all = "BV1ut63YREk9,BV17NkhYFEE3,BV12ek2YsEqt,BV1mukpYWEu9,BV1wxBFY6Ejg,BV1dtBjYGEVr,BV1bZq8YKEeb,BV1R6qUY8EGg,BV1F3qKYnEEU,BV1UtqVYQETa,BV1MviRYNESG,BV1LEzzYrEu7,BV1okBiYeEKH,BV1SdUpYCEcK,BV1mfUFYVESk,BV1UxmaYwECv,BV11sDUYmEpX,BV1hDDWY9Emh,BV1CpSBYLEZ3,BV19iSoYEEmp,BV1fC17YiETa,BV1zp1TYgEL5,BV1h514Y7En8,BV1YFyUYVEBm,BV1uS1FYzErs,BV1saypYxEcq,BV1BDyLYFEar,BV1gzmMYKEiS,BV1a16GYwEM3,BV1Dq6bYrEMK,BV1QrC6YJEDM,BV1eZCrY4EUE,BV1wzCTYkE1B,BV1aTkSY6EsV,BV1AMkzYFEa3,BV1VJkcYMEj9,BV1sxBLYREoR,BV1mnq8YhE5x,BV1Q8q6YNEdH,BV1J4qAYkEvJ,BV1jGqsYaEei,BV15RizYKEYV,BV14uzmYSEBq,BV1t86FY9ECf,BV15uzYYWE5L,BV1Ssz5Y8Erc,BV1fpBtYLEih,BV1rLUZYZEKE,BV1a8mLYsEsQ,BV1x8CjYzEMT,BV1prk2YSEQo,BV1TABjY8EZc,BV1ccBMYfEDf,BV1kTqQYSEBs,BV11wqKY4EtA,BV1NLq5YSEp3,BV1LWioYnE7L,BV11ZBRYKEsQ,BV1H9yhYVEJo,BV1bHCUYNET2,BV1wryPYqE6J,BV1gzmMYKEiS,BV1NS2oYfENk,BV1g5mjYsEuR,BV1yc2rYjE7s,BV1yC2aYdEon,BV1iZ28YBEZf,BV1Tb2UY3EL3,BV1Qc2SYEEBK,BV1rE2VYwEai,BV1U12PYDErq,BV14c2pYeESF,BV17G1yYkE8g,BV1gZ1BYmEKM,BV1eo19YYEDp,BV1m34AejE4j,BV1uW4FerEYN,BV1cxxQeMEPB,BV1cxxQeMEHz,BV12x4uecEhu,BV1wxxhemEEr,BV1NcxCepEMY,BV1jixMerE79,BV1wCsdeEELS,BV1rrxjegEVh,BV1XhxVeJE1h,BV1sRsaeXEdr,BV1HasSeaE3A,BV12AtUeVEyJ,BV1Uv4SejEEC,BV1zM4fedE2R,BV1E6HheYEvC,BV1aTkSY6EsV,BV1AMkzYFEa3,BV1VJkcYMEj9,BV1sxBLYREoR,BV1mnq8YhE5x,BV1Q8q6YNEdH,BV1J4qAYkEvJ,BV1jGqsYaEei,BV15RizYKEYV,BV14uzmYSEBq,BV1t86FY9ECf,BV15uzYYWE5L,BV1Ssz5Y8Erc,BV1fpBtYLEih,BV1rLUZYZEKE,BV1LNDUYaER9,BV1riSJY9E7a,BV1CfCQYiEk1,BV1nd1qYFEc1,BV14u1XY2ELE,BV16AxDePEvw,BV115mdYZEvM"

bvids_bilibili_pro ="BV1mukpYWEu9,BV1wxBFY6Ejg,BV1dtBjYGEVr,BV1bZq8YKEeb,BV1R6qUY8EGg,BV1F3qKYnEEU,BV1UtqVYQETa,BV1MviRYNESG,BV1LEzzYrEu7,BV1okBiYeEKH,BV1SdUpYCEcK,BV1mfUFYVESk,BV1UxmaYwECv,BV11sDUYmEpX,BV1hDDWY9Emh,BV1CpSBYLEZ3,BV19iSoYEEmp,BV1fC17YiETa,BV1zp1TYgEL5,BV1h514Y7En8,BV1YFyUYVEBm,BV1uS1FYzErs,BV1saypYxEcq,BV1BDyLYFEar,BV1AMkzYFEa3,BV1VJkcYMEj9,BV1sxBLYREoR,BV1mnq8YhE5x,BV1Q8q6YNEdH,BV1J4qAYkEvJ,BV1jGqsYaEei,BV15RizYKEYV,BV14uzmYSEBq,BV1t86FY9ECf,BV15uzYYWE5L,BV1Ssz5Y8Erc,BV1fpBtYLEih,BV1rLUZYZEKE,BV1TABjY8EZc,BV1ccBMYfEDf,BV1kTqQYSEBs,BV11wqKY4EtA,BV1NLq5YSEp3,BV1LWioYnE7L,BV11ZBRYKEsQ,BV1a8mLYsEsQ,BV1gzmMYKEiS"

# bvids_bilibili_un = os.getenv("bvids_bilibili_un")
# bvids_bilibili_un = bvids_bilibili_un.replace('"','')
# bvids_bilibili_un = re.sub(r"[\s'\"]+", '', bvids_bilibili_un)
# if bvids_bilibili_un :
#     new_bvids = bvids_bilibili_un.split(",")
#     bvids.extend(new_bvids)

def strtolist(data_str):
    
    bvids = data_str.split(",")
    return bvids
    
def print_log(msg):
    # 直接print()在Docker中不会显示, 所以要家flush=True
    print(msg, flush=True)



headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Origin': 'https://www.bilibili.com',
    'Connection': 'keep-alive'
}





# 视频的基本参数
def buildData(bvids):
    reqdatas = []
    for bvid in bvids:
        stime = str(int(time.time()))
        resp = requests.get("https://api.bilibili.com/x/web-interface/view?bvid={}".format(bvid), headers=headers)
        try:
            rdata = resp.json()["data"]
        except Exception:
            print_log(f"{bvid}请求失败")
            continue
        data= {
            'aid':rdata["aid"],
            'cid':rdata["cid"],
            "bvid": bvid,
            'part':'1',
            'mid':rdata["owner"]["mid"],
            'lv':'6',
            "stime" :stime,
            'jsonp':'jsonp',
            'type':'3',
            'sub_type':'0',
            'title': rdata["title"]
        }
        reqdatas.append(data)
    return reqdatas

# random.shuffle(reqdatas)

def goPlay(url,data_str,n):
    count = 0
    #count < 30
    while count < n:
        try:
            reqdatas = buildData(strtolist(data_str))
            random.shuffle(reqdatas)
            #发起一个post请求，去请求这个页面，从而获得一次点击量
            for data in reqdatas:
                stime = str(int(time.time()))
                
                data["stime"]=stime
                headers["referer"]="https://www.bilibili.com/video/{}/".format(data.get("bvid"))
                
                print_log("bvid: {}, title: {}".format(data.get("bvid"), data.get("title")))
                
                requests.post(url, data=data, headers=headers)
                t = random.randint(6,8)

                time.sleep(t)

                #requests.post(VIDEO_HEARTBEAT, data=data, headers=headers)

                #time.sleep(6)

            count += 1
            print_log(count)
            localtime = time.asctime( time.localtime(time.time()) )
            print_log(localtime)
            # 刷一次要休息100s, 即使有连接池貌似也不能随便刷, 你可以研究下
            delay = random.randint(120,150)
            time.sleep(delay)
        except Exception as e:
            print_log(e)
            time.sleep(300)
            print_log('over')

url = "https://api.bilibili.com/x/click-interface/click/web/h5"

VIDEO_HEARTBEAT = "https://api.bilibili.com/x/click-interface/web/heartbeat"

# print_log("准备起飞啦~~~{}".format(bvids))
print_log("准备起飞啦~~~")

goPlay(url,bvids_bilibili_pro,25)
# delay = random.randint(120,180)
# time.sleep(delay)
goPlay(url,bvids_bilibili_all,5)
