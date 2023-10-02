from nonebot import on_command, CommandSession
from nonebot import on_natural_language, NLPSession, IntentCommand
from random import choice
import random

__plugin_name__ = 'njt辱骂器'

replies = ['sbnjt', 'njt妈妈の消失', 'njt真该死啊你', '查询njt的妈妈失败',
           'njt🐎又炸了', '尼基塔在给他妈咪上坟', 'njt臭傻逼', '每有一个玩家被头眼，地图里就会生成一个njt的🐎',
           'njt脑子抽了吧', 'njt没有母亲', 'njt你看看你做的逼ai', 'njtnmlgcbwywcnmdsb',
           'njt你坏事做尽', 'njt正在sm.JPG']


@on_command('sbnjt', aliases=('sbnjt', 'njt辱骂器'))
async def sbnjt(session: CommandSession):
    if random.random() < 0.5:
        await session.send(choice(replies))


# on_natural_language 装饰器将函数声明为一个自然语言处理器
# keywords 表示需要响应的关键词，类型为任意可迭代对象，元素类型为 str
# 如果不传入 keywords，则响应所有没有被当作命令处理的消息
@on_natural_language(keywords={'njt', '尼基塔'}, only_to_me=False)
# keywords={'sbnjt', ' tmd尼基塔', 'cnmnjt', '尼基塔你', 'njt你', 'njt服务器', 'njt妈妈', 'njt父母', '傻逼njt','傻逼尼基塔', '服务器炸了'}
async def _(session: NLPSession):
    # 返回意图命令，前两个参数必填，分别表示置信度和意图命令名
    return IntentCommand(90.0, 'sbnjt')
