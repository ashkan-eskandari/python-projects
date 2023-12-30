from turtle import Turtle
import random
COLORS = ["blue","yellow",'red',"green"]
class Blocks(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.all_blocks=[]
    def create_blocks(self):
        for i in range(-214, 250, 60):

            for j in range(230, 0, -30):
                block = Turtle()
                block.penup()
                block.shape("square")
                block.color(random.choice(COLORS))
                block.shapesize(stretch_wid=1, stretch_len=2.5)
                block.goto(i, j)
                self.all_blocks.append(block)
