"""Module for the scoreboard"""
from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    """Class representing the scoreboard"""

    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-280, 250)
        self.update_scoreboard()

    def update_scoreboard(self):
        """Method to update the scoreboard"""
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def increase_level(self):
        """Method to increase the level"""
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        """Method to display the game over text"""
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)
