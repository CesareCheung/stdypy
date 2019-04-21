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
    quit = input('是否退出程序Y/N：').upper()

    while quit == 'N':
        print('请输入以下信息，以空格分开！')
        try:
            input_str = input('性别, 体重(kg), 身高(cm), 年龄：')
            str_list = input_str.split(' ')  # 以空格为分割
            gender = str_list[0]
            weight = float(str_list[1])
            height = float(str_list[2])
            age = int(str_list[3])
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
        except ValueError:
            print('请输入正确信息！')
        except IndexError:
            print("输入信息过少！")
        except:
            print('程序异常，未知错误！')

        # 性别
        # gender = input('性别：')

        # # 体重
        # weight = input('体重(kg):')
        # weight = float(weight)
        #
        # # 身高
        # height = input('身高(CM)')
        # height = float(height)
        #
        # # 年龄
        # age = input('年龄：')
        # age = float(age)

        print("<<=======================================================>>")
        quit = input("是否退出程序Y/N:").upper()


if __name__ == '__main__':
    main()
