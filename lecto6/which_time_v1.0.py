"""
    _author=Cesare
    版本：V1.0
    日期：2019/04/21
    功能：输入某年某月某日，判断这一天是一年的第几天
"""

from datetime import datetime


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

    day_in_month_tup = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

    print(day_in_month_tup[:months-1])                  # 拿到对应月份前的所有对应月份的天数
    sum_days=sum(day_in_month_tup[:months-1])+days      # 计算到输入日期为止的所有天数

    # 判断闰年
    if (years % 4 == 0) or ((years % 4 == 0) and (years % 100 !=0)):
        if months > 2:
            sum_days+=1

    print(f"这是第{sum_days}天")



if __name__ == '__main__':
    main()


