from nonebot import on_command, CommandSession
from nonebot import on_natural_language, NLPSession, IntentCommand
from random import choice
import datetime

__plugin_name__ = '寒暄'


morning1 = ['起得真早，早安早安!', '，早上好,今天也很有元气呢!', '早安哦~']
morning2 = ['小懒虫~太阳都晒屁股啦']
morning3 = '喂喂喂！都几点了'
morning4 = '明明该晚安了呀'
night1 = ['保重身体哦，早点休息~', '已经很晚了哦，好好休息吧~']
night2 = ['晚安啦~', '今晚也会做好梦哦~']
night3 = '睡个好觉吧~'
gadada = ['我是嘎哒哒!有何吩咐!', '你好你好!', '喵喵喵？']


@on_natural_language(keywords={'早安', '早上好'}, only_to_me=False)
async def _(session: NLPSession):
    hour = datetime.datetime.now().strftime("%H")
    hour = int(hour)
    if 5 <= hour < 10:
        return IntentCommand(100.0, 'echo', args={'message': choice(morning1)})
    elif 10 <= hour < 13:
        return IntentCommand(100.0, 'echo', args={'message': choice(morning2)})
    elif 13 <= hour < 21:
        return IntentCommand(100.0, 'echo', args={'message': morning3})
    else:
        return IntentCommand(100.0, 'echo', args={'message': morning4})


@on_natural_language(keywords={'晚安'}, only_to_me=False)
async def _(session: NLPSession):
    hour = datetime.datetime.now().strftime("%H")
    hour = int(hour)
    if 20 <= hour < 24:
        return IntentCommand(100.0, 'echo', args={'message': choice(night2)})
    elif 0 <= hour < 6:
        return IntentCommand(100.0, 'echo', args={'message': choice(night1)})
    else:
        return IntentCommand(100.0, 'echo', args={'message': night3})


@on_natural_language(keywords={'嘎哒哒'}, only_to_me=False)
async def _(session: NLPSession):
    return IntentCommand(100.0, 'echo', args={'message': choice(gadada)})


@on_natural_language(keywords={'嘎嘎哒'}, only_to_me=False)
async def _(session: NLPSession):
    return IntentCommand(100.0, 'echo', args={'message': '嘎哒哒不是嘎嘎哒'})
