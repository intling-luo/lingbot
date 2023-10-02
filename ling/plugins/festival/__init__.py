from nonebot import on_command, CommandSession
from nonebot import on_natural_language, NLPSession, IntentCommand
from .data_source import say_festival


@on_command('festival', aliases=('节日祝福', '节日播报'))
async def festival(session: CommandSession):
    sayfestival = await say_festival()
    await session.send(sayfestival)


# on_natural_language 装饰器将函数声明为一个自然语言处理器
# keywords 表示需要响应的关键词，类型为任意可迭代对象，元素类型为 str
# 如果不传入 keywords，则响应所有没有被当作命令处理的消息
@on_natural_language(keywords={'中秋快乐', '节日快乐', '国庆快乐', '节快乐', '年快乐', '安康'}, only_to_me=False)
async def _(session: NLPSession):
    # 返回意图命令，前两个参数必填，分别表示置信度和意图命令名
    return IntentCommand(90.0, 'festival')
