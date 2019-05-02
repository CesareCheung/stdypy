
"""
    _author=Cesare
    功能：郑塞子
    python数据可视化

"""


from matplotlib import pyplot
import random


def roll_dice():
    roll=random.randint(1,6)
    return roll

def main():
    """
    主函数
    :return:
    """
    totime=20
    # 初始化列表[0,0,0,0,0,0]
    result_list=[0]*11    # 2到12所以为11个数


    # 初始化列表点数
    roll_list=list(range(2,12))

    roll_dict=dict(zip(roll_list,result_list))

    # 记录骰子结果
    roll1_list=[]
    roll2_list=[]

    for i in range(totime):
        roll1=roll_dice()   # 第一次抛出来的点数
        roll2 = roll_dice()  #第二次

        roll1_list.append(roll1)
        roll2_list.append(roll2)
        for j in range(2,12):    # 能抛出来的点数
            if (roll1+roll2)==j:            # 做对比
                roll_dict[j]+=1  #在对应的位置上加1做记录

    for i,result in roll_dict.items():
        print(f"点数:{i},出现次数:{result},频率：{result/totime}")


    # 数据可视化
    x=range(1,totime+1)
    pyplot.scatter(x,roll1_list,alpha=0.5,color='red')
    pyplot.scatter(x,roll2_list,alpha=0.5,color='green')
    pyplot.show()


if __name__ == '__main__':
    main()