
import config
import requests
import json

def push_to_wechat(token,title,content):
    """
    通过PUSHPLUS将消息推送到微信
    :param token: PUSHPLUS_TOKEN
    :param text: 标题
    :param desp: 内容
    :return resp: json
    """
    url = 'http://pushplus.hxtrip.com/send'
    data = {
        "token":token,
        "title":title,
        "content":content
    }
    body=json.dumps(data).encode(encoding='utf-8')
    headers = {'Content-Type':'application/json'}
    r=requests.post(url,data=body,headers=headers)
    return r.json()


if __name__ == '__main__':
    resp = push_to_wechat(config.PUSHPLUS_TOKEN,'title','hello')
    print(resp)
