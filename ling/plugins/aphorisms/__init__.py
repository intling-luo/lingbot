from nonebot import on_command, CommandSession
from nonebot import on_natural_language, NLPSession, IntentCommand

from .data_source import get_aphorisms


@on_command('aphorisms', aliases='一言', only_to_me=False)
async def aphorisms(session: CommandSession):

    # 获取
    aphorism = await get_aphorisms()
    # 向用户发送
    await session.send(aphorism)


