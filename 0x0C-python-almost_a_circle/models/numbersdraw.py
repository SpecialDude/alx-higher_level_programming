def draw_number(num, pen):
    if num == 0:
        #Draw zero
        pen.rt(90)
        pen.down()
        pen.fd(15)
        pen.rt(90)
        pen.fd(30)
        pen.rt(90)
        pen.fd(15)
        pen.rt(90)
        pen.fd(30)
        pen.rt(90)
        pen.fd(15)
        pen.rt(90)
        pen.fd(30)
        pen.lt(90)
        #End of Draw Zero
    elif num == 1:
        #Draw One
        pen.up()
        pen.rt(90)
        pen.fd(7.5)
        pen.lt(90)
        pen.down()
        pen.rt(180)
        pen.rt(30)
        pen.fd(5)
        pen.rt(180)
        pen.fd(5)
        pen.rt(150)
        pen.fd(30)
        pen.rt(90)
        pen.fd(7.5)
        pen.rt(180)
        pen.fd(15)
        #End of Draw One
    elif num == 2:
        #Draw Two
        pen.down()
        pen.rt(90)
        pen.fd(15)
        pen.rt(90)
        pen.fd(15)
        pen.rt(90)
        pen.fd(15)
        pen.lt(90)
        pen.fd(15)
        pen.lt(90)
        pen.fd(15)
        #End of Draw Two
    elif num == 3:
        #Draw Three
        pen.up()
        pen.rt(180)
        pen.fd(5)
        pen.rt(180)
        pen.down()
        pen.fd(5)
        pen.rt(90)
        pen.fd(15)
        pen.rt(90)
        pen.fd(15)
        pen.rt(90)
        pen.fd(15)
        pen.rt(180)
        pen.fd(15)
        pen.rt(90)
        pen.fd(15)
        pen.rt(90)
        pen.fd(15)
        pen.rt(90)
        pen.fd(5)
        pen.rt(180)
        pen.fd(5)
        pen.lt(90)
        pen.fd(15)
        #End of Draw three
    elif num == 4:
        #Draw Four
        pen.rt(180)
        pen.down()
        pen.fd(15)
        pen.lt(90)
        pen.fd(15)
        pen.lt(90)
        pen.fd(15)
        pen.rt(180)
        pen.fd(30)
        pen.lt(90)
        #End of Draw four
    elif num == 5:
        #Draw Five
        pen.rt(90)
        pen.down()
        pen.fd(15)
        pen.rt(180)
        pen.fd(15)
        pen.lt(90)
        pen.fd(15)
        pen.lt(90)
        pen.fd(15)
        pen.rt(90)
        pen.fd(15)
        pen.rt(90)
        pen.fd(15)
        pen.rt(180)
        pen.fd(15)
        #End of Draw five
    elif num == 6:
        #Draw six
        pen.rt(180)
        pen.down()
        pen.fd(30)
        pen.lt(90)
        pen.fd(15)
        pen.lt(90)
        pen.fd(15)
        pen.lt(90)
        pen.fd(15)
        pen.lt(90)
        pen.fd(15)
        pen.lt(90)
        pen.fd(15)
        #End of Draw six
    elif num == 7:
        #Draw seven
        pen.rt(90)
        pen.down()
        pen.fd(15)
        pen.rt(90)
        pen.fd(30)
        pen.lt(90)
        #End of Draw seven
    elif num == 8:
        #Draw eight
        pen.rt(90)
        pen.down()
        pen.fd(15)
        pen.rt(90)
        pen.fd(15)
        pen.rt(90)
        pen.fd(15)
        pen.rt(90)
        pen.fd(15)
        pen.rt(180)
        pen.fd(30)
        pen.lt(90)
        pen.fd(15)
        pen.lt(90)
        pen.fd(15)
        pen.lt(180)
        pen.fd(15)
        pen.lt(90)
        #End of Draw eight
    elif num == 9:
        #Draw nine
        pen.rt(90)
        pen.down()
        pen.fd(15)
        pen.rt(90)
        pen.fd(15)
        pen.rt(90)
        pen.fd(15)
        pen.rt(90)
        pen.fd(15)
        pen.rt(90)
        pen.fd(15)
        pen.rt(90)
        pen.fd(30)
        pen.lt(90)
        #End of Draw nine
    else:
        pen.rt(90)
        pen.fd(50)
        pen.lt(90)


def space_between(pen, space):
    pen.up()
    pen.fd(10)
    pen.lt(90)
    pen.fd(30)

def write_digits(num, pen, heading=90, **kwargs):
    size =  kwargs.get("size") or 2
    space =  kwargs.get("space") or 30

    old_size = pen.pensize()

    pen.pensize(size)

    for i in str(num):
        pen.setheading(heading)
        draw_number(int(i), pen)
        space_between(pen, space)

    pen.pensize(old_size)
