"""
    _author=Cesare
    功能：52周存钱挑战
    版本：5.0：根据用户输入的日期，判断是一年中的第几周，然后输出相应的存款金额
    日期：09/04/2019
"""
import math
import datetime


# datetime.datetime.strptime("2019/04/21", format("%Y/%m/%d"))   日期解析
# datetime.datetime.strftime("2019/04/21", "%Y/%m/%d")    日期格式化

def save_mone_n_weeks(money_per_week, increase_money, total_week):
    """
    计算n周内的存入总金额
    :return:
    """

    money_list = []  # 记录每周存款数的列表

    saved_money_list = []  # 记录每周账户累计金额

    for i in range(total_week):
        money_list.append(money_per_week)
        saving = math.fsum(money_list)
        saved_money_list.append(saving)
        # 输出信息
        # print(f"第{i+1}周,存入:{money_per_week}元,累计账户：{saving}")
        money_per_week += increase_money
        # print('函数内部变量',saving)

    return saved_money_list


def main():
    '''
    主函数
    :return:
    '''
    money_per_week = float(input("请输入每周存入金额："))  # 每周的存入金额
    increase_money = float(input("请输入递增金额："))  # 递增金额
    total_week = int(input("请输入总共周数："))  # 总共周数
    # 调用函数
    saved_money_list = save_mone_n_weeks(money_per_week, increase_money, total_week)

    input_date_str = input("请输入yyyy/mm/dd格式日期：")

    input_date = datetime.datetime.strptime(input_date_str, format("%Y/%m/%d"))  # 拿到日期并解析
    week_num = input_date.isocalendar()[1]  # 拿到对应日期的周数

    print(f"第几周的存款金额为{saved_money_list[week_num - 1]}")


if __name__ == '__main__':
    main()
