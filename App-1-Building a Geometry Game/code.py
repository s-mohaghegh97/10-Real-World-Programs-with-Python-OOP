from random import randint
import turtle


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def falls_in_rectangle(self, rectangle):
        if rectangle.lowleft.x < self.x < rectangle.upright.x \
                and rectangle.lowleft.y < self.y < rectangle.upright.y:
            return True
        else:
            return False

    def distance_from_point(self, point):
        return ((self.x - point.x) ** 2 + (self.y - point.y) ** 2) ** 0.5


class Rectangle:

    def __init__(self, lowleft, upright):
        self.lowleft = lowleft
        self.upright = upright

    def area(self):
        return (self.upright.x - self.lowleft.x) * (self.upright.y - self.lowleft.y)


class GuiRectangle(Rectangle):

    def draw(self, canvas):
        canvas.penup()
        canvas.goto(self.lowleft.x, self.lowleft.y)

        canvas.pendown()
        canvas.forward(self.upright.x - self.lowleft.x)
        canvas.left(90)
        canvas.forward(self.upright.y - self.lowleft.y)
        canvas.left(90)
        canvas.forward(self.upright.x - self.lowleft.x)
        canvas.left(90)
        canvas.forward(self.upright.y - self.lowleft.y)


class GuiPoint(Point):

    def draw(self, canvas, size=5):
        canvas.penup()
        canvas.goto(self.x, self.y)
        canvas.pendown()
        canvas.dot(size=size)


rec = GuiRectangle(Point(randint(0, 200), randint(0, 200)),
                   Point(randint(200, 400), randint(200, 400)))

print("Rectangle Coordinates: ",
      rec.lowleft.x, ",",
      rec.lowleft.y, "and",
      rec.upright.x, ",",
      rec.upright.y
      )

user_point = GuiPoint(
    float(input("Guess X: ")),
    float(input("Guess Y: "))
)

user_area = float(input("Guess rec area: "))

print("Your point was inside rec: ",
      user_point.falls_in_rectangle(rec))

print("Your area was off by: ",
      rec.area() - user_area)

myturtle = turtle.Turtle()
rec.draw(canvas=myturtle)
user_point.draw(canvas=myturtle)

turtle.done()
