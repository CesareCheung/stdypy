"""
    _author=Cesare
    日期：03/05/2019
    功能：AQI计算
    版本：1.0
"""


def cal_linear(iaqi_lo, iaqi_hi, bp_lo, bp_hi, cp):
    """
    缩放范围
    :param iaqi_lo:
    :param iaqi_hi:
    :param bp_lo:
    :param bp_hi:
    :param cp:
    :return:
    """
    iaqi = (iaqi_hi - iaqi_lo) * (cp - bp_lo) / (bp_hi - bp_lo) + iaqi_lo

    return iaqi


def cal_pm_aqi(pm_value):
    '''
    计算PM2.5的AQI
    :param pm_value:
    :return:
    '''
    if 0 <= pm_value < 36:
        iaqi = cal_linear(0, 50, 0, 35, pm_value)

    elif 36 <= pm_value < 76:
        iaqi = cal_linear(50, 100, 35, 75, pm_value)

    elif 76 <= pm_value < 116:
        iaqi = cal_linear(100, 150, 75, 115, pm_value)

    else:
        pass


def cal_co_aqi(co_value):
    '''
    计算co的AQI
    :param co_value:
    :return:
    '''
    if 0 <= co_value < 3:
        iaqi = cal_linear(0, 50, 0, 3, co_value)

    elif 3 <= co_value < 5:
        iaqi = cal_linear(50, 100, 2, 4, co_value)

    else:
        pass


def cal_aqi(params_list):
    '''
    AQI计算
    :return:
    '''
    pm_value = params_list[0]
    co_value = params_list[1]

    pm_iaqi = cal_pm_aqi(pm_value)
    co_iaqi = cal_co_aqi(co_value)

    iaqi_list = []
    iaqi_list.append(pm_iaqi)
    iaqi_list.append(co_iaqi)

    return iaqi_list


def main():
    """
    主函数
    :return:
    """
    print("请输入以下数据,以空格分割：")
    input_list = input("(1)PM2.5 (2)CO:")
    str_list = input_list.split(' ')
    pm_value = float(str_list[0])
    co_value = float(str_list[1])

    param_list = []
    param_list.append(pm_value)
    param_list.append(co_value)

    # 调用cal_aqi()计算函数
    aqi_value = cal_aqi(param_list)
    print(f'空气质量指数为：{aqi_value}')


if __name__ == '__main__':
    main()
