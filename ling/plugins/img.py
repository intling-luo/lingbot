from nonebot import on_command, CommandSession
from nonebot import on_natural_language, NLPSession, IntentCommand
import jieba

__plugin_name__ = '随机图片'

table = {
    '二次元': 'ycy', '萌版': 'moez', 'AI': 'ai', 'ai': 'ai', '原神': 'ysz', 'PC': 'pc', '风景': 'fj', '白底': 'bd'
}


@on_command('img', aliases=('图片', '随图'))
async def img(session: CommandSession):
    tag = session.current_arg_text.strip()
    if not tag:
        tag = (await session.aget(prompt='你想要哪个标签的图片喵\n关键词：二次元，萌版，AI，原神，PC，风景，白底')).strip()
        while not tag:
            tag = (await session.aget(prompt='要查询的标签不能为空喵，请重新输入喵')).strip()
    if tag in table:
        await session.send('[CQ:image,file=https://t.mwm.moe/' + table[tag] + ',cache=0,c=2]')
    else:
        await session.send(f'没有找到标签为{tag}的图喵')


# on_natural_language 装饰器将函数声明为一个自然语言处理器
# keywords 表示需要响应的关键词，类型为任意可迭代对象，元素类型为 str
# 如果不传入 keywords，则响应所有没有被当作命令处理的消息
@on_natural_language(keywords={'随图'}, only_to_me=False)
async def _(session: NLPSession):
    # 去掉消息首尾的空白符
    text = session.msg_text.strip()
    # 使用 jieba 分词
    words = jieba.cut(text)
    tags = None
    # 遍历分词结果
    for word in words:
        # 检查分词结果是否在输出表中
        if word in table:
            tags = word
            break
    # 如果找到匹配项，将相应的标签添加到输出列表
    # 返回意图命令，前两个参数必填，分别表示置信度和意图命令名
    return IntentCommand(90.0, 'img', current_arg=tags or '')
