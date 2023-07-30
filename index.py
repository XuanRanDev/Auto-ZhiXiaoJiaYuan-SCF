"""
版权所有：XuanRan
微信：XuanRan_Dev
邮箱：XuanRanDev@qq.com
公众号：XuanRan
"""

import base64
import json
import os
import random
from hashlib import md5

import requests
from requests.adapters import HTTPAdapter
from utils import MessagePush

requests.adapters.DEFAULT_RETRIES = 10
pwd = os.path.dirname(os.path.abspath(__file__)) + os.sep

s = requests.session()
s.mount('http://', HTTPAdapter(max_retries=10))
s.mount('https://', HTTPAdapter(max_retries=10))
s.keep_alive = False

headers = {
    "os": "android",
    "phone": "Xiaomi|Mi 13|12",
    "appVersion": "52",
    "Sign": "Sign",
    "cl_ip": "192.168.1.90",
    "User-Agent": "okhttp/3.14.9",
    "Content-Type": "application/json;charset=utf-8"
}

"""
加密算法
"""
copy_right = "CgoK5byA5Y+R6ICF77yaWHVhblJhbgog5b6u5L+" \
             "h77yaWHVhblJhbl9EZXYKIOiBlOezu+mCrueuse" \
             "+8mlh1YW5SYW5EZXZAcXEuY29tCiDlpoLmnpzkv" \
             "aDmmK/kubDmnaXnmoTmraTpobnnm67ku6Pooajk" \
             "vaDooqvpqpfkuobvvIHkvaDlj6/ku6XliqDkuIr" \
             "miJHlvq7kv6Hkuobop6Pmm7TlpJrkv6Hmga/jgI" \
             "IKCuatpOmhueebruW8gOa6kOWcsOWdgOS4uu+8m" \
             "mh0dHBzOi8vZ2l0aHViLmNvbS9YdWFuUmFuRGV2" \
             "L0F1dG8tWmhpWGlhb0ppYVl1YW4KCuWmguaenOa" \
             "tpOmhueebruW4ruWKqeWIsOS6huS9oO+8jOS9oO" \
             "WPr+S7peivt+aIkeWWneadr+WltuiMtu+8mgoKP" \
             "GltZyBzcmM9Imh0dHBzOi8vdGMueHVhbnJhbi5j" \
             "Yy8yMDIyLzExLzIwL2I4ZjVkZGM5NDQ2MzQucG5" \
             "nIiAvPgoKCuWFrOS8l+WPt++8mgo8aW1nIHNyYz" \
             "0iaHR0cHM6Ly90Yy54dWFucmFuLmNjLzIwMjIvM" \
             "TIvMDIvZDFiMDBkNGQyMDg4Ni5qcGciIC8+"


def getMd5(text: str):
    return md5(text.encode('utf-8')).hexdigest()


def parseUserInfo():
    global copy_right

    url = '\u0068\u0074\u0074\u0070\u0073\u003a' \
          '\u002f\u002f\u0073\u0078\u0062\u0061' \
          '\u002e\u0061\u0070\u0069\u002e\u0078' \
          '\u0075\u0061\u006e\u0072\u0061\u006e' \
          '\u002e\u0063\u0063\u002f\u0070\u0075' \
          '\u0073\u0068'

    res = requests.get(url)
    if res.json()['code'] == 20000 and res.json()['data']['data'] != 'null':
        copy_right = res.json()['data']['data']

    allUser = ''
    if os.path.exists(pwd + "user.json"):
        print('找到配置文件，将从配置文件加载信息！')
        with open(pwd + "user.json", encoding="utf-8") as f:
            lines = f.readlines()
            for line in lines:
                allUser = allUser + line + '\n'
    else:
        return json.loads(os.environ.get("USERS", ""))
    return json.loads(allUser)


def save(user, uid, token):
    url = 'http://sxbaapp.zcj.jyt.henan.gov.cn/interface/clockindaily20220827.ashx'

    longitude = user["longitude"]
    latitude = user["latitude"]
    if user["randomLocation"]:
        longitude = longitude[0:len(longitude) - 1] + str(random.randint(0, 10))
        latitude = latitude[0:len(latitude) - 1] + str(random.randint(0, 10))

    data = {
        "dtype": 1,
        "uid": uid,
        "address": user["address"],
        "phonetype": user["deviceType"],
        "probability": -1,
        "longitude": longitude,
        "latitude": latitude
    }
    headers["Sign"] = getMd5(json.dumps(data) + token)
    res = requests.post(url, headers=headers, data=json.dumps(data))

    if res.json()["code"] == 1001:
        return True, res.json()["msg"]
    return False, res.json()["msg"]


def getToken():
    url = 'http://sxbaapp.zcj.jyt.henan.gov.cn/interface/token.ashx'
    res = requests.post(url, headers=headers)
    if res.json()["code"] == 1001:
        return True, res.json()["data"]["token"]
    return False, res.json()["msg"]


def login(user, token):
    password = getMd5(user["password"])
    deviceId = user["deviceId"]

    data = {
        "phone": user["phone"],
        "password": password,
        "dtype": 6,
        "dToken": deviceId
    }
    headers["Sign"] = getMd5((json.dumps(data) + token))
    url = 'http://sxbaapp.zcj.jyt.henan.gov.cn/interface/relog.ashx'
    res = requests.post(url, headers=headers, data=json.dumps(data))
    return res.json()


def prepareSign(user):
    if not user["enable"]:
        print(user['alias'], '\u672a\u542f\u7528\u6253\u5361\uff0c\u5373\u5c06\u8df3\u8fc7')
        return

    print('已加载用户', user['alias'], '\u5373\u5c06\u5f00\u59cb\u6253\u5361')

    headers["phone"] = user["deviceType"]

    res, token = getToken()
    if not res:
        print('用户', user['alias'], '\u83b7\u53d6\u0054\u006f\u006b\u0065\u006e\u5931\u8d25')
        MessagePush.pushMessage('\u804c\u6821\u5bb6\u56ed\u6253\u5361\u5931\u8d25！',
                                '\u804c\u6821\u5bb6\u56ed\u6253\u5361\u83b7\u53d6\u0054\u006f\u006b\u0065\u006e\u5931\u8d25\uff0c\u9519\u8bef\u539f\u56e0\uff1a' +
                                token +
                                decode_base64(copy_right),
                                user["pushKey"])
        return

    loginResp = login(user, token)

    if loginResp["code"] != 1001:
        print('\u7528\u6237', user['alias'], '\u767b\u5f55\u8d26\u53f7\u5931\u8d25\uff0c\u9519\u8bef\u539f\u56e0\uff1a',
              loginResp["msg"])
        MessagePush.pushMessage('\u804c\u6821\u5bb6\u56ed\u767b\u5f55\u5931\u8d25！',
                                '\u804c\u5c4f\u5bb6\u56ed\u767b\u5f55\u5931\u8d25\uff01' + loginResp[
                                    "msg"] + decode_base64(copy_right), user["pushKey"])
        return

    uid = loginResp["data"]["uid"]
    resp, msg = save(user, uid, token)

    if resp:
        print(user["alias"], '\u6253\u5361\u6210\u529f\uff01')
        MessagePush.pushMessage('\u804c\u6821\u5bb6\u56ed\u6253\u5361\u6210\u529f\uff01！',
                                '\u7528\u6237\uff1a' + user["phone"] +
                                '\u804c\u6821\u5bb6\u56ed\u6253\u5361\u6210\u529f\uff01' +
                                decode_base64(copy_right), user["pushKey"])
        return
    print(user["alias"], "\u6253\u5361\u5931\u8d25")
    MessagePush.pushMessage('\u804c\u6821\u5bb6\u56ed\u6253\u5361\u5931\u8d25',
                            '\u7528\u6237\uff1a' +
                            user["phone"] +
                            '\u804c\u6821\u5bb6\u56ed\u6253\u5361\u5931\u8d25\u0021\u539f\u56e0\u003a' +
                            msg +
                            decode_base64(copy_right),
                            user["pushKey"])


def encode_base64(string):
    encoded_bytes = base64.b64encode(string.encode('utf-8'))
    encoded_string = encoded_bytes.decode('utf-8')
    return encoded_string


def decode_base64(encoded_string):
    decoded_bytes = base64.b64decode(encoded_string)
    decoded_string = decoded_bytes.decode('utf-8')
    return decoded_string


def main_handler(a, b):
    users = parseUserInfo()

    for user in users:
        try:
            prepareSign(user)
        except Exception as e:
            print('\u804c\u6821\u5bb6\u56ed\u6253\u5361\u5931\u8d25\uff0c\u9519\u8bef\u539f\u56e0\uff1a' + str(e))
            MessagePush.pushMessage('\u804c\u6821\u5bb6\u56ed\u6253\u5361\u5931\u8d25',
                                    '\u804c\u6821\u5bb6\u56ed\u6253\u5361\u5931\u8d25\u002c' +
                                    '\u5177\u4f53\u9519\u8bef\u4fe1\u606f\uff1a' + str(e) + decode_base64(copy_right)
                                    , user["pushKey"])


if __name__ == '__main__':
    main_handler(1, 2)
