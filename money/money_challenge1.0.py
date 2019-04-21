"""
    _author=Cesare
    功能：52周存钱挑战
    版本：1.0
    日期：09/04/2019
"""


def main():
    '''
    主函数
    :return:
    '''
    money_per_week = 10  # 每周的存入金额
    i = 1  # 记录周数
    increase_money = 10  # 递增金额
    total_week = 52  # 总共周数
    saving = 0  # 账户累计
    # 输出信息

    while i <= total_week:
        saving += money_per_week
        print(f"第{i}周,存入:{money_per_week}元,累计账户：{saving}")
        money_per_week += increase_money
        i += 1


if __name__ == '__main__':
    main()
