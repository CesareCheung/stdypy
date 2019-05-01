"""
    _author=Cesare_Zhang
    功能：定义一个文件工具类
    日期：19/04/27

"""


class PasswordTool:
    """
        密码工具类

    """

    # 类的属性
    def __init__(self, password):
        self.password = password
        self.strong_level = 0

    def process_password(self):
        # 规则1，判断密码位数是否大于等于8位

        if len(self.password) >= 8:
            self.strong_level += 1
        else:
            print("密码位数小于8位数")

        # 规则2，判断密码中是否包含数字
        if self.check_number_exist():
            self.strong_level += 1
        else:
            print("密码要求包含数字")

        # 规则3，判断密码中是否包含字符串
        if self.check_letter_exist():
            self.strong_level += 1
        else:
            print("密码要求包含字母")

    # 类的方法
    def check_number_exist(self):
        """
        判断字符串中是否包含数字
        :param password:
        :return:
        """
        has_letter = False
        for c in self.password:
            if c.isnumeric():
                has_letter = True
                break
        return has_letter

    def check_letter_exist(self):
        """
        判断字符串中是否包含字母
        :param password:
        :return:
        """

        for c in self.password:
            if c.isalpha():
                return True
        return False

class FileTool:
    """
        文件工具类
    """
    def __init__(self,filepath):
        self.filepath=filepath

    def write_to_file(self,line):
        f=open(self.filepath,"a",encoding='utf-8')
        f.write(line)
        f.close()

    def read_from_file(self):
        f=open(self.filepath,'r',encoding='utf-8')
        lines=f.readlines()
        f.close()
        return lines


def main():
    '''
    主函数
    :return:
    '''
    try_time = 5

    filepath='password_6.0.txt'
    file_tool = FileTool(filepath)
    while try_time > 0:
        password = input('请输入密码：')
        password_tool = PasswordTool(password)
        password_tool.process_password()

        dict_level = {0:"弱",1: "较弱", 2: "中", 3: "强"}
        # 将密码写入文件
        # 调用文件工具类进行写操作

        line=f"密码：{password_tool.password}，强度：{dict_level[password_tool.strong_level]}\n"
        file_tool.write_to_file(line)

        if password_tool.strong_level == 3:
            print("恭喜！密码强度合格！")
            break
        else:
            print("抱歉！密码强度不合格！")
            try_time -= 1

    if try_time <= 0:
        print("尝试次数过多，设置密码失败！")

    lines=file_tool.read_from_file()
    print(lines)


if __name__ == '__main__':
    main()
