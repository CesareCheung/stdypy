"""
    _author=Cesare
    功能：投骰子，直方图可视化结果
    python数据可视化


"""

from matplotlib import pyplot
import random
import numpy

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

    # 记录骰子结果
    roll1_arr = numpy.random.randint(1, 7, size=totime)
    roll2_arr = numpy.random.randint(1, 7, size=totime)
    result_list = roll1_arr + roll2_arr

    # 数据可视化
    pyplot.hist(result_list, range(2, 14), density=1, edgecolor='black', linewidth=1)
    pyplot.title("骰子点数统计")
    pyplot.xlabel('点数')
    pyplot.ylabel('频率')

    pyplot.show()


if __name__ == '__main__':
    main()
