from nonebot import on_command, CommandSession
from nonebot import on_natural_language, NLPSession, IntentCommand

import datetime


@on_command('time', aliases=('查时间', '几点了'),only_to_me=False)
async def time(session: CommandSession):
    now = datetime.datetime.now()
    now_time = now.strftime("%Y-%m-%d %H:%M:%S")
    await session.send(f'现在的时间是：\n{now_time}')

