"""
    _author=Cesare
    版本：v2.0
    功能：BMR计算器
    日期:07/04/19

"""


def main():
    '''
    主函数
    :return:
    '''
    quit=input('是否退出程序Y/N：').upper()

    while quit == 'N':

        # 性别
        gender = input('性别：')

        # 体重
        weight = input('体重(kg):')
        weight = float(weight)

        # 身高
        height = input('身高(CM)')
        height = float(height)

        # 年龄
        age = input('年龄：')
        age = float(age)

        if gender == '男':
            bmr = (13.7 * weight) + (5.0 * height) - (6.8 * age) + 66
        elif gender == '女':
            bmr = (9.6 * weight) + (1.8 * height) - (4.7 * age) + 665
        else:
            bmr = -1
        if bmr != -1:
            print(f"基础代谢率为：{bmr}")
        else:
            print(f"暂不支持{gender}性别")
        print("<<=======================================================>>")
        quit=input("是否退出程序Y/N:").upper()


if __name__ == '__main__':
    main()


