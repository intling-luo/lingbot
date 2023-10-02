from random import choice

replies = ['SCP，启动！', '把电脑还给我----我要打奢侈品~~~~', '少爷，该启动SCP了。', '奢侈品时间到！！！','再不玩奢侈品我就要死啦~~']


async def play_scp() -> str:
    return choice(replies)
