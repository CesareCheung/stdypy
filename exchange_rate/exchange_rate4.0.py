def convert_currency(inmoney, exchangerate):
    """
    汇率兑换函数
    :param inmoney: 货币金额
    :param exchangerate: 汇率
    :return:
    """
    out = inmoney * exchangerate
    return out


# 汇率
usd_vs_rmb = 6.77

# 输入带单位的货币

currency_str_value = input("请输入带货币单位金额：")

unit = currency_str_value[-3:]
# 输入为人民币
if unit == 'CNY':
    exchange_rate = 1 / usd_vs_rmb

# 输入为美元
elif unit == 'USD':
    exchange_rate = usd_vs_rmb

else:
    exchange_rate = -1

if exchange_rate != -1:
    in_money = eval(currency_str_value[:-3])
    out_money = convert_currency(in_money, exchange_rate)
    print(f'转换后的金额：{out_money}')
else:
    print('不支持该种货币！')
