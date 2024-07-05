"""Module for the player"""

from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    """Class representing the player"""

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.go_to_start()
        self.setheading(90)

    def move_up(self):
        """Method to move the player up"""
        self.forward(MOVE_DISTANCE)

    def go_to_start(self):
        """Method to reset the player to the starting position"""
        self.goto(STARTING_POSITION)

    def is_at_finish_line(self):
        """Method to detect when the player is at the finish line"""
        if self.ycor() > FINISH_LINE_Y:
            return True
        return False
