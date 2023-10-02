from nonebot import on_command, CommandSession
from nonebot import on_natural_language, NLPSession, IntentCommand
from random import choice

__plugin_name__ = 'sbidv'

replies = ['我再也不玩第五人格了']


@on_command('sbidv')
async def sbidv(session: CommandSession):
    await session.send('我再也不玩第五人格了')


# on_natural_language 装饰器将函数声明为一个自然语言处理器
# keywords 表示需要响应的关键词，类型为任意可迭代对象，元素类型为 str
# 如果不传入 keywords，则响应所有没有被当作命令处理的消息
@on_natural_language(keywords={'我再也不玩第五人格了'}, only_to_me=False)
# keywords={'sbnjt', ' tmd尼基塔', 'cnmnjt', '尼基塔你', 'njt你', 'njt服务器', 'njt妈妈', 'njt父母', '傻逼njt','傻逼尼基塔', '服务器炸了'}
async def _(session: NLPSession):
    # 返回意图命令，前两个参数必填，分别表示置信度和意图命令名
    return IntentCommand(90.0, 'sbidv')
