"""
    _author=Cesare
    功能：郑塞子

"""
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
    result_list=[0]*6

    for i in range(totime):
        roll=roll_dice()   # 抛出来的点数
        for j in range(1,7):    # 能抛出来的点数
            if roll==j:            # 做对比
                result_list[j-1]+=1  #在对应的位置上加1做记录

    for i,result in enumerate(result_list):
        print(f"点数:{i+1},出现次数:{result},频率：{result/totime}")

        # print(roll_dice())
    # print(result_list)
if __name__ == '__main__':
    main()