"""
    _author=Cesare
    利用递归函数绘制分形树
    版本：1.0
    日期：31/03/19
"""
import turtle

def draw_branch(branch_length):
    """
    绘制分形树函数
    :param branch_length:长度
    :return:
    """

    if branch_length>5:
        turtle.pencolor("green")
        # 绘制右侧树枝
        turtle.forward(branch_length)
        print(f"向前{branch_length}")
        turtle.right(20)
        print("右转20度")
        # 调用自身
        draw_branch(branch_length-5)

        #向左转40度后绘制左侧树枝
        turtle.left(40)
        print("左转40度")
        draw_branch(branch_length-5)

        #返回之前的树枝节点上
        turtle.right(20)
        print('右转20度')
        turtle.backward(branch_length)
        turtle.pencolor('brown')
        print(f"向后{branch_length}")



def main():
    """
    主函数
    :return:
    """


    turtle.pensize(2)
    turtle.left(90)
    turtle.penup()
    turtle.backward(200)
    turtle.pendown()
    draw_branch(60)
    turtle.exitonclick()

if __name__ == '__main__':
    main()