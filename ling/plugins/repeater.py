from nonebot import on_command, CommandSession
from nonebot import on_natural_language, NLPSession, IntentCommand

import random

__plugin_name__ = '复读姬'

# 命令名
@on_command('repeater')
async def repeater(session: CommandSession):
    say = await session.aget()
    await session.send(say)

# on_natural_language 装饰器将函数声明为一个自然语言处理器
# keywords 表示需要响应的关键词，类型为任意可迭代对象，元素类型为 str
# 如果不传入 keywords，则响应所有没有被当作命令处理的消息
@on_natural_language(keywords={}, only_to_me=False)
async def _(session: NLPSession):
    # 返回意图命令，前两个参数必填，分别表示置信度和意图命令名
    if random.random() > 0.99:
        return IntentCommand(61.0, 'repeater')
