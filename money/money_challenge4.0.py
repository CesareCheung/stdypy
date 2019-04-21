"""
    _author=Cesare
    功能：52周存钱挑战
    版本：4.0灵活设置每周存款数，增加的存款数及存款周数
    日期：09/04/2019
"""
import math

# 全局变量
saving=0

def save_mone_n_weeks(money_per_week,increase_money,total_week):
    """
    计算n周存入总金额
    :return:
    """
    global saving
    saving = 0  # 账户累计金额
    money_list = []  # 记录每周存款数的列表

    for i in range(total_week):
        money_list.append(money_per_week)
        saving=math.fsum(money_list)
        # 输出信息
        # print(f"第{i+1}周,存入:{money_per_week}元,累计账户：{saving}")
        money_per_week += increase_money
        # print('函数内部变量',saving)

    return saving


def main():
    '''
    主函数
    :return:
    '''
    money_per_week = float(input("请输入每周存入金额："))    # 每周的存入金额
    increase_money = float(input("请输入递增金额："))        # 递增金额
    total_week = int(input("请输入总共周数："))             # 总共周数
    #调用函数
    saving = save_mone_n_weeks(money_per_week,increase_money,total_week)

    print("总金额为",saving)


if __name__ == '__main__':
    main()
