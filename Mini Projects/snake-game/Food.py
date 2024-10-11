import random
import turtle
from turtle import Turtle

FOOD_PIC = [
    "./food/apple.gif",
    "./food/banana.gif",
    "./food/blueberry.gif",
    "./food/candy.gif",
    "./food/cherry.gif",
    "./food/chocolate.gif",
    "./food/cupcake.gif",
    "./food/grape.gif",
    "./food/kiwi.gif",
    "./food/orange.gif",
    "./food/pie.gif",
    "./food/strawberry.gif",
    "./food/watermelon.gif",
]

for food in FOOD_PIC:
    turtle.addshape(food)


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape(random.choice(FOOD_PIC))
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("red")
        self.speed("fastest")
        random_x = random.randint(-250, 250)
        random_y = random.randint(-250, 250)
        self.goto(random_x, random_y)
        self.refresh()

    def refresh(self):
        self.shape(random.choice(FOOD_PIC))
        random_x = random.randint(-250, 250)
        random_y = random.randint(-250, 250)
        self.goto(random_x, random_y)