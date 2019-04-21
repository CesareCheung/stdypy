"""
    _author=Crease
    功能：BMR计算器
    版本：1.0
    日期：19.04.07
"""


def main(gender,height,weight,age):
    '''
    主函数
    :return:
    '''
    # 性别
    # gender = '男'
    #
    # # 身高
    #
    # height = 175
    #
    # # 体重
    #
    # weight = 70
    #
    # # 年龄
    #
    # age = 20

    if gender == '男':
        bmr = (13.7 * weight) + (5.0 * height) - (6.8 * age) + 66
    elif gender == '女':
        bmr = (9.6 * weight) + (1.8 * height) - (4.7 * age) + 665

    else:
        bmr = -1
    if bmr != -1:
        print(f"基础代谢率为：{bmr}")
    else:
        print("暂不支持该性别！")

    pass


if __name__ == '__main__':
    main('男',165,50,26)
