import json
import requests


async def get_weather(city_name: str):
    # api地址（一套明确定义的各种软件组件之间的通信方法，例如如下的天气API，最后面加入城市代码就可以得到天气）
    url = 'http://t.weather.sojson.com/api/weather/city/'
    # 读取json文件（以二进制只读方式打开一个文件）
    f = open('city.json', 'rb')
    # 使用json模块的load方法加载json数据，返回一个字典 （将序列化的字符串转化为数据类型）
    cities = json.load(f)
    # 通过城市的中文获取城市代码
    city_name = cities.get(city_name)
    # 网络请求，传入请求api+城市代码
    if city_name is None:
        return -1
    response = requests.get(url + city_name)
    # 将数据以json形式返回，这个d就是返回的json数据
    return response.json()
    # 当返回状态码为200，输出天气状况


async def get_weather_of_city(city: str) -> str:
    output = "输入的城市有误！"
    a = await get_weather(city)
    if a == -1:
        return output
    else:
        d = a
    if d['status'] == 200:
        # 省份：d["cityInfo"]["parent"]
        # 城市：d["cityInfo"]["city"]
        # 年月日时间：d["time"]
        # 周几：d["data"]["forecast"][0]["week"]
        # 高温：d["data"]["forecast"][0]["high"]
        # 低温：d["data"]["forecast"][0]["low"]
        # 天气：d["data"]["forecast"][0]["type"]
        # 结语：d["data"]["forecast"][0]["notice"]
        forecast = d['data']['forecast'][:7]
        output = "城市：" + d["cityInfo"]["parent"] + d["cityInfo"]["city"] + "\n"
        for day in forecast:
            date = day['ymd']  # 日期
            week = day['week']  # 周几
            high = day['high']  # 最高温度
            low = day['low']  # 最低温度
            weather_type = day['type']  # 天气类型
            notice = day['notice']  # 天气提示
            output += "\n" + date + week + "\n温度：" + high + low + "\n天气：" + weather_type
        return output
    else:
        return "接口请求错误"


# json字典示例
var = {"message": "success感谢又拍云(upyun.com)提供CDN赞助", "status": 200, "date": "20230930",
       "time": "2023-09-30 19:23:52",
       "cityInfo": {"city": "北京市", "citykey": "101010100", "parent": "北京", "updateTime": "18:31"},
       "data": {"shidu": "26%", "pm25": 4.0, "pm10": 13.0, "quality": "优", "wendu": "23",
                "ganmao": "各类人群可自由活动", "forecast": [
               {"date": "30", "high": "高温 24℃", "low": "低温 15℃", "ymd": "2023-09-30", "week": "星期六",
                "sunrise": "06:09", "sunset": "17:59", "aqi": 42, "fx": "西北风", "fl": "3级", "type": "晴",
                "notice": "愿你拥有比阳光明媚的心情"},
               {"date": "01", "high": "高温 26℃", "low": "低温 16℃", "ymd": "2023-10-01", "week": "星期日",
                "sunrise": "06:10", "sunset": "17:57", "aqi": 49, "fx": "西风", "fl": "2级", "type": "晴",
                "notice": "愿你拥有比阳光明媚的心情"},
               {"date": "02", "high": "高温 25℃", "low": "低温 17℃", "ymd": "2023-10-02", "week": "星期一",
                "sunrise": "06:11", "sunset": "17:56", "aqi": 73, "fx": "西南风", "fl": "2级", "type": "多云",
                "notice": "阴晴之间，谨防紫外线侵扰"},
               {"date": "03", "high": "高温 26℃", "low": "低温 15℃", "ymd": "2023-10-03", "week": "星期二",
                "sunrise": "06:12", "sunset": "17:54", "aqi": 91, "fx": "西南风", "fl": "2级", "type": "晴",
                "notice": "愿你拥有比阳光明媚的心情"},
               {"date": "04", "high": "高温 25℃", "low": "低温 18℃", "ymd": "2023-10-04", "week": "星期三",
                "sunrise": "06:13", "sunset": "17:53", "aqi": 87, "fx": "北风", "fl": "3级", "type": "晴",
                "notice": "愿你拥有比阳光明媚的心情"},
               {"date": "05", "high": "高温 24℃", "low": "低温 15℃", "ymd": "2023-10-05", "week": "星期四",
                "sunrise": "06:14", "sunset": "17:51", "aqi": 64, "fx": "西北风", "fl": "2级", "type": "晴",
                "notice": "愿你拥有比阳光明媚的心情"},
               {"date": "06", "high": "高温 24℃", "low": "低温 15℃", "ymd": "2023-10-06", "week": "星期五",
                "sunrise": "06:15", "sunset": "17:50", "aqi": 58, "fx": "南风", "fl": "2级", "type": "阴",
                "notice": "不要被阴云遮挡住好心情"},
               {"date": "07", "high": "高温 24℃", "low": "低温 16℃", "ymd": "2023-10-07", "week": "星期六",
                "sunrise": "06:16", "sunset": "17:48", "aqi": 31, "fx": "西南风", "fl": "2级", "type": "阴",
                "notice": "不要被阴云遮挡住好心情"},
               {"date": "08", "high": "高温 25℃", "low": "低温 16℃", "ymd": "2023-10-08", "week": "星期日",
                "sunrise": "06:17", "sunset": "17:46", "aqi": 36, "fx": "西南风", "fl": "1级", "type": "多云",
                "notice": "阴晴之间，谨防紫外线侵扰"},
               {"date": "09", "high": "高温 26℃", "low": "低温 17℃", "ymd": "2023-10-09", "week": "星期一",
                "sunrise": "06:18", "sunset": "17:45", "aqi": 45, "fx": "南风", "fl": "1级", "type": "晴",
                "notice": "愿你拥有比阳光明媚的心情"},
               {"date": "10", "high": "高温 27℃", "low": "低温 17℃", "ymd": "2023-10-10", "week": "星期二",
                "sunrise": "06:19", "sunset": "17:43", "aqi": 45, "fx": "西南风", "fl": "2级", "type": "多云",
                "notice": "阴晴之间，谨防紫外线侵扰"},
               {"date": "11", "high": "高温 27℃", "low": "低温 18℃", "ymd": "2023-10-11", "week": "星期三",
                "sunrise": "06:20", "sunset": "17:42", "aqi": 67, "fx": "东风", "fl": "2级", "type": "多云",
                "notice": "阴晴之间，谨防紫外线侵扰"},
               {"date": "12", "high": "高温 27℃", "low": "低温 16℃", "ymd": "2023-10-12", "week": "星期四",
                "sunrise": "06:22", "sunset": "17:40", "aqi": 46, "fx": "西北风", "fl": "3级", "type": "晴",
                "notice": "愿你拥有比阳光明媚的心情"},
               {"date": "13", "high": "高温 24℃", "low": "低温 16℃", "ymd": "2023-10-13", "week": "星期五",
                "sunrise": "06:23", "sunset": "17:39", "aqi": 51, "fx": "西北风", "fl": "3级", "type": "阴",
                "notice": "不要被阴云遮挡住好心情"},
               {"date": "14", "high": "高温 22℃", "low": "低温 15℃", "ymd": "2023-10-14", "week": "星期六",
                "sunrise": "06:24", "sunset": "17:37", "aqi": 34, "fx": "北风", "fl": "3级", "type": "阴",
                "notice": "不要被阴云遮挡住好心情"}],
                "yesterday": {"date": "29", "high": "高温 27℃", "low": "低温 14℃", "ymd": "2023-09-29",
                              "week": "星期五", "sunrise": "06:08", "sunset": "18:01", "aqi": 31, "fx": "西北风",
                              "fl": "2级", "type": "多云", "notice": "阴晴之间，谨防紫外线侵扰"}}}
