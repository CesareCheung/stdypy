"""
    _author=Cesare
    功能：投骰子，直方图可视化结果
    python数据可视化


"""

from matplotlib import pyplot
import random

# 解决中文输出乱码
pyplot.rcParams['font.sans-serif'] = ["SimHei"]
pyplot.rcParams['axes.unicode_minus'] = False


def roll_dice():
    roll = random.randint(1, 6)
    return roll


def main():
    """
    主函数
    :return:
    """
    totime = 1000
    # 初始化列表[0,0,0,0,0,0]
    result_list = [0] * 11  # 2到12所以为11个数

    # 记录骰子结果
    roll_list = []

    for i in range(totime):
        roll1 = roll_dice()  # 第一次抛出来的点数
        roll2 = roll_dice()  # 第二次

        roll_list.append(roll1 + roll2)

    # 数据可视化
    x = range(1, totime + 1)
    pyplot.hist(roll_list, range(2, 14), density=1, edgecolor='black', linewidth=1)
    pyplot.title("骰子点数统计")
    pyplot.xlabel('点数')
    pyplot.ylabel('频率')

    pyplot.show()


if __name__ == '__main__':
    main()
