#百度通用翻译API,不包含词典、tts语音合成等资源，如有相关需求请联系translate_api@baidu.com
# coding=utf-8

import http.client
import hashlib
import urllib
import random
import json

appid = '20200622000503989'  # 填写你的appid
secretKey = 'xIdznCSmvk2xNG520AsT'  # 填写你的密钥

httpClient = None
myurl = '/api/trans/vip/translate'

fromLang = 'auto'   #原文语种
toLang = 'auto'   #译文语种 见链接https://api.fanyi.baidu.com/doc/21
salt = random.randint(32768, 65536)
q= input('your word:')
sign = appid + q + str(salt) + secretKey
sign = hashlib.md5(sign.encode()).hexdigest()
myurl = myurl + '?appid=' + appid + '&q=' + urllib.parse.quote(q) + '&from=' + fromLang + '&to=' + toLang + '&salt=' + str(
salt) + '&sign=' + sign

try:
    httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')
    httpClient.request('GET', myurl)

    # response是HTTPResponse对象
    response = httpClient.getresponse()
    result_all = response.read().decode("utf-8")
    result = json.loads(result_all)


    print (f"输入:{result['trans_result'][0]['src']}")
    print (f"输出:{result['trans_result'][0]['dst']}")

except Exception as e:
    print (e)
finally:
    if httpClient:
        httpClient.close()