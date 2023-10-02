import requests


async def get_user_id():
    # api地址（一套明确定义的各种软件组件之间的通信方法，例如如下的天气API，最后面加入城市代码就可以得到天气）
    url = "http://127.0.0.1:6666/get_login_info"
    # 网络请求，传入请求api
    response = requests.get(url)
    return response.json()


async def get_id() -> str:
    profile = await get_user_id()
    if profile['retcode'] == 0:
        output = '昵称：' + profile["data"]['nickname'] + '\n' + 'qq号：' + str(profile["data"]['user_id'])
    else:
        output = profile['retcode']
    return output


var = {"data": {"nickname": "憨批pot", "user_id": 1125946787}, "message": "", "retcode": 0, "status": "ok"}
