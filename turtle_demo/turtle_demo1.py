"""
    _author = Cesare
    功能：五角星绘制
    版本：1.0
    日期：30/03/2019
    新增功能：加入循环操作绘制重复不同大小的图形
    新增功能：使用迭代函数绘制重复不同大小图形
"""

import turtle
# region turtle库使用方法

# # 画笔向前移动distance距离
# turtle.forward(distance)
# # 画笔向后移动distance距离
# turtle.backward(distance)
# # 绘制方向向右旋转degree度
# turtle.right(degree)
# # 点击关闭图形窗口
# turtle.exitonclick()

# turtle.penup()  #抬起画笔，之后移动画笔不会只形状
# turtle.pendown() #落下画笔，之后移动画笔绘制形状
# turtle.pensize() #设置笔宽度
# turtle.pencolor() #设置笔颜色，常用的颜色：whilte,black,grey,darkgreen,gold,violet,purple

# 形状绘制函数
def draw_pentagram(size):
    """
    绘制五角星
    :param size:
    :return:
    """
    for i in range(5):
        turtle.forward(size)
        turtle.right(144)

def draw_recursive_pentagram(size):
    """
    迭代绘制五角星
    :param size:
    :return:
    """
    for i in range(5):
        turtle.forward(size)
        turtle.right(144)

    # 绘制完五角星，更新参数
    size+=10
    if size<=300:
        draw_recursive_pentagram(size)
def main():
    """
    主程序
    :return:
    """
    turtle.penup()
    turtle.backward(200)
    turtle.pendown()
    turtle.pensize(2)
    turtle.pencolor("red")
    size=50
    draw_recursive_pentagram(size)

if __name__ == '__main__':
    main()



