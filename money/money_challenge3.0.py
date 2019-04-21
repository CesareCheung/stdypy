"""
    _author=Cesare
    功能：52周存钱挑战
    版本：3.0使用循环直接计数
    日期：09/04/2019
"""
import math

def main():
    '''
    主函数
    :return:
    '''
    money_per_week = 10     # 每周的存入金额

    increase_money = 10     # 递增金额
    total_week = 52         # 总共周数
    saving = 0              # 账户累计
    money_list = []         # 记录每周存款数的列表

    for i in range(total_week):
        money_list.append(money_per_week)
        saving=math.fsum(money_list)
        # 输出信息
        print(f"第{i+1}周,存入:{money_per_week}元,累计账户：{saving}")
        money_per_week += increase_money


if __name__ == '__main__':
    main()
