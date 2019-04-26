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
    is_leap_year=False
    if (years % 4 == 0) or ((years % 4 == 0) and (years % 100 != 0)):
        is_leap_year=True
    return is_leap_year



def main():
    '''
    主函数
    :return:
    '''

    input_str_date = input("请输入日期(yyyy/mm/dd):")
    input_date = datetime.strptime(input_str_date, '%Y/%m/%d')
    print(input_date)
    years = input_date.year      # 拿到年份
    months = input_date.month    # 拿到月份
    days = input_date.day        # 拿到日期
    day_in_month_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap_year(years):
        day_in_month_list[1]=29
    sum_days = sum(day_in_month_list[:months - 1]) + days  # 计算到输入日期为止的所有天数


    print(f"这是{years}年的第{sum_days}天")



if __name__ == '__main__':
    main()


