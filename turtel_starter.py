import turtle as t
eternal_slave=t.Turtle()
def draw_branch(len):
    if len > 5:
        for i in range(3):
            eternal_slave.forward(len)
            draw_branch(len/3)
            eternal_slave.backward(len)
            eternal_slave.right(50)
eternal_slave.color("cyan")
eternal_slave.penup()
eternal_slave.teleport(0,0)
eternal_slave.pendown()
eternal_slave.speed(0)
itera=0
while eternal_slave.pos()!=(0,0) and itera >1:
    itera=1
    draw_branch(100)
    eternal_slave.right(60)
eternal_slave.hideturtle()