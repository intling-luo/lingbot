from nonebot import on_command, CommandSession
from nonebot import on_natural_language, NLPSession, IntentCommand

__plugin_name__ = '帮助'


@on_command('help_s', aliases=('帮助', 'help'), only_to_me=False)
async def help_s(session: CommandSession):
    await session.send(
        f"功能列表：\n[CQ:face,id=145]一言(传递更多的感动)\n[CQ:face,id=161]随图(随机美图，可指定类型)\n[CQ:face,id=31]njt("
        f"帮你骂njt)\n[CQ:face,id=60]几点了(顾名思义)\n[CQ:face,id=74]查天气("
        f"查城市最近7天的天气)\n[CQ:face,id=210]其他功能(还在做…有想要的功能可以私信机器人提意见)")


