from nonebot import on_command, CommandSession
from nonebot import on_natural_language, NLPSession, IntentCommand

from .data_source import get_id


@on_command('qq_text')
async def qq_text(session: CommandSession):
    # 获取
    qqid = await get_id()
    # 向用户发送
    await session.send(qqid)


@on_natural_language(keywords={'你的qq','你的信息'})
async def _(session: NLPSession):
    # 返回意图命令，前两个参数必填，分别表示置信度和意图命令名
    return IntentCommand(90.0, 'qq_text')
