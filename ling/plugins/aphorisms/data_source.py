import json
import requests


async def get_aphorisms_req():
    # api地址（一套明确定义的各种软件组件之间的通信方法，例如如下的天气API，最后面加入城市代码就可以得到天气）
    url = 'https://v1.hitokoto.cn'
    # 网络请求，传入请求api
    response = requests.get(url)
    # 将数据以json形式返回，这个d就是返回的json数据
    return response.json()


async def get_aphorisms() -> str:
    aphorisms = await get_aphorisms_req()
    if aphorisms['id'] != '':
        output = aphorisms['hitokoto'] + "\n——" + aphorisms['from']
    return output

# var = {"id": 1154, "uuid": "6c4047da-0f29-45ec-8e0e-a76d782381c6",
#      "hitokoto": "重要的人，不能忘记的人，不想忘记的人。 你，是谁？", "type": "a", "from": "你的名字", "from_who": null,
#      "creator": "谬蜀黍", "creator_uid": 280, "reviewer": 0, "commit_from": "web", "created_at": "1491019648",
#     "length": 25}
