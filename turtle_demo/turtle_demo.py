"""
    _author = Cesare
    功能：五角星绘制
    版本：1.0
    日期：30/03/2019
    新增功能：加入循环操作绘制重复不同大小的图形
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


# turtle.penup()  #抬起画笔，之后移动画笔不绘制形状
# turtle.pendown() #落下画笔，之后移动画笔绘制形状
# turtle.pensize() #设置笔宽度
# turtle.pencolor() #设置笔颜色，常用的颜色：whilte,black,grey,darkgreen,gold,violet,purple

# count = 1
# while count <=5:
#
#     turtle.forward(100)
#     turtle.right(144)
#     count+=1
# turtle.exitonclick()
# endregion

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
    while size<=300:
        draw_pentagram(size)
        size+=15

    turtle.exitonclick()



# turtle.color('red', 'yellow')
# turtle.begin_fill()
# while True:
#     turtle.forward(200)
#     turtle.left(170)
#     if abs(turtle.pos()) < 1:
#         break
# turtle.end_fill()
# turtle.done()

if __name__ == '__main__':
    main()



