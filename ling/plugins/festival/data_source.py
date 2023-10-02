import datetime

# 定义一个包含节日日期的字典
holidays = {
    "中秋节": (9, 29),
    "国庆节": (10, 1),
    "重阳节": (10, 23),
    "万圣节": (10, 31),
    "圣诞节": (12, 25),
    "新年": (1, 1),
}


async def say_festival() -> str:
    today = datetime.date.today()
    today_month = today.month
    today_day = today.day
    is_holiday = False
    for holiday, (month, day) in holidays.items():
        if today_month == month and today_day == day:
            is_holiday = True
            break
    if is_holiday:
        return f'{holiday}快乐！'
