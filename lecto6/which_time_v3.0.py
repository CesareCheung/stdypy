"""
    _author=Cesare
    版本：V2.0
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
    days = input_date.day  # 拿到日期
    # 包含30天 月份集合
    _30_days_set = {4, 6, 9, 11}
    _31_days_set = {1, 3, 5, 7, 8, 10, 12}
    days=0
    days+=days
    for i in range(1,months):
        if i in _30_days_set:
            days+=30
        elif i in _31_days_set:
            days+=31
        else:
            days+=28

    if is_leap_year(years) and months>2:
        days+=1
    sum_days =  days  # 计算到输入日期为止的所有天数

    print(f"这是{years}年的第{sum_days}天")


if __name__ == '__main__':
    main()
