"""
    _author=Cesare
    版本：V4.0
    日期：2019/04/21
    功能：输入某年某月某日，判断这一天是一年的第几天
"""

from datetime import datetime

def is_leap_year(years):
    """
    判断是否为闰年
    是，返回True
    否，返回False
    :param year:
    :return:
    """
    is_leap_year = False
    if (years % 4 == 0) or ((years % 4 == 0) and (years % 100 != 0)):
        is_leap_year = True
    return is_leap_year

def main():
    '''
    主函数
    :return:
    '''

    input_str_date = input("请输入日期(yyyy/mm/dd):")
    input_date = datetime.strptime(input_str_date, '%Y/%m/%d')
    print(input_date)
    years = input_date.year  # 拿到年份
    months = input_date.month  # 拿到月份
    # 月份-天数-字典
    moths_days_dict = {
        1: 31,
        2: 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }
    days = 0
    days += days
    for i in range(1, months):
        days += moths_days_dict[i]

    if is_leap_year(years) and months > 2:
        days += 1

    print(f"这是{years}年的第{days}天")


if __name__ == '__main__':
    main()
