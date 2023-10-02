from nonebot import on_command, CommandSession
from nonebot import on_natural_language, NLPSession, IntentCommand
from random import choice

__plugin_name__ = '龙猫'


@on_command('longmao', aliases='阿姨', only_to_me=False)
async def sbidv(session: CommandSession):
    await session.send('[CQ:image,file=file:///root/lingbot/longmao.gif]')

