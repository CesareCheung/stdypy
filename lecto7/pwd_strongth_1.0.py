"""
    _author=Cesare_Zhang
    功能：判断密码强度
    日期：19/04/27

"""

def check_number_exist(password_str):
    """
    判断字符串中是否包含数字
    :param password:
    :return:
    """
    for c in password_str:
        if c.isnumeric():
            return True
    return False

def check_letter_exist(password_str):
    """
    判断字符串中是否包含字母
    :param password:
    :return:
    """
    for c in password_str:
        if c.isalpha():
            return True
    return False



def main():
    '''
    主函数
    :return:
    '''
    password = input('请输入密码：')

    # 密码强度
    strong_level = 0

    # 规则1，判断密码位数是否大于等于8位

    if len(password)>=8:
        strong_level+=1
    else:
        print("密码位数小于8位数")

    # 规则2，判断密码中是否包含数字
    if check_number_exist(password):
        strong_level+=1
    else:
        print("密码要求包含数字")

    # 规则3，判断密码中是否包含字符串
    if check_letter_exist(password):
        strong_level+=1
    else:
        print("密码要求包含字母")

    if strong_level==3:
        print("恭喜！密码强度合格！")
    else:
        print("抱歉！密码强度不合格！")




if __name__ == '__main__':
    main()
