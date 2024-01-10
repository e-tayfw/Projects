from turtle import Turtle
import random

class Enemy(Turtle):
    def __init__(self):
        super().init()

        self.shape('turtle')
        self.penup()
        self.color('red')
        self.speed(0)
        self.spawn()

    
    def spawn(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
        