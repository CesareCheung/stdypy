# 汇率
usd_vs_rmb = 6.77

i = 0

# 输入带单位的货币

currency_str_value = input("请输入带货币单位金额,输入Q退出程序：")

while currency_str_value != 'Q':
    i += 1
    print(f'运行第{i}次')

    unit = currency_str_value[-3:]
    # 输入为人民币
    if unit == 'CNY':
        rmb_str_value = currency_str_value[:-3]
        # 将字符串转换成数字
        rmb_value = eval(rmb_str_value)

        usd_value = rmb_value / usd_vs_rmb

        print("美元金额为：", usd_value)
    # 输入为美元
    elif unit == 'USD':

        usd_str_value = currency_str_value[:-3]

        usd_value = eval(usd_str_value)

        rmb_value = usd_value * usd_vs_rmb
        print("人民币金额为：", rmb_value)

    else:
        print("该种货币暂不支持！")
    currency_str_value = input("请输入带货币单位金额,输入Q退出程序：")

print('程序已退出！')
