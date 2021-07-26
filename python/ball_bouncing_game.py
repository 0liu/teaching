#!/usr/bin/env python3

import time
import random
from tkinter import Tk, Canvas


class Ball:
    def __init__(self, canvas, paddle, color):
        self.canvas = canvas
        self.paddle = paddle
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)  # save oval(ball)'s id
        self.canvas.move(self.id, 245, 100)  # initialize ball's position at (245, 100)

        # self.x = 0  # moving step on X-axis, horizontally
        # self.y = -1  # moving step on Y-axis, vertically

        # Initialize the starting moving steps on X-axis and Y-axis
        starts = [-3, -2, -1, 1, 2, 3]
        random.shuffle(starts)
        self.x = starts[0]  # Generate a random starting moving step for X-axis
        self.y = -3

        # Attributes to save the canvas upper and right-side boundary
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()

        # A state variable to mark if the ball hits the bottom.
        # If so, it means the ball drops down to the ground and the player fails, and
        # the game engine stops updating the animation.
        self.hit_bottom = False

    def draw(self):
        """
        Move the ball by 1 step, and then check if it's out of canvas boundary
        and if it hits the paddle.
        """
        # Move the ball by 1 step on both directions
        self.canvas.move(self.id, self.x, self.y)

        # Get coordinates (position) of the ball: x1, y1, x2, y2
        # (x1, y1) are the coordinates of the upper-left point of the ball
        # (x2, y2) are the coordinates of the bottom-right point of the ball
        pos = self.canvas.coords(self.id)

        # Check if the ball goes over upper boundary or lower boundary
        # The origin point of the upper-left canvas has coordinates (0, 0)
        if pos[1] <= 0:  # y1 negative means ball is out of upper bound
            self.y = 3
        if pos[3] >= self.canvas_height:  # y2 is out of lower bound
            self.y = -3

        # Check and mark if the ball hits bottom
        if pos[3] >= self.canvas_height:
            self.hit_bottom = True

        # Check if the ball hits paddle. If so, bounce up.
        if self.hit_paddle(pos) == True:
            self.y = -3

        # Check if the ball crosses left  boundary or right boundary
        if pos[0] <= 0:  # x1 negative means ball is out of left bound
            self.x = 3
        if pos[2] >= self.canvas_width:  # x2 out of right bound
            self.x = -3

    def hit_paddle(self, pos):  # pos: ball's position
        """
        Check if ball's position crosses paddle's position
        """
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:  # compare X coordinates
            if (
                pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]
            ):  # compare Y coordinates
                return True
        return False


class Paddle:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)  # save paddle's id
        self.canvas.move(
            self.id, 200, 300
        )  # initialize paddle's position at (200, 300)

        self.x = 0  # Initialize the moving step on x axis to 0, meaning NOT moving.
        self.canvas_width = self.canvas.winfo_width()  # save canvas' right boundary.

        # Bind Left and Right arrow keys to the two methods.
        self.canvas.bind_all("<KeyPress-Left>", self.turn_left)
        self.canvas.bind_all("<KeyPress-Right>", self.turn_right)

    def draw(self):
        """
        Move the paddle along X-axis by 1 step, according to the step set by key event.
        If the paddle touches the left or right bounds of the canvas, stop moving by setting
        the moving step to 0.
        """
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:  # paddle touches left bound
            self.x = 0  # stop move the paddle
        elif pos[2] >= self.canvas_width:  # paddle touches right bound
            self.x = 0

    def turn_left(self, evt):
        """
        Triggered by a keyboard event. Set the moving step to negative so that the paddle moves
        to the left side.
        """
        self.x = -2

    def turn_right(self, evt):
        """
        Triggered by a keyboard event. Set the moving step to negative so that the paddle moves
        to the right side.
        """
        self.x = 2


# --- Execution code stats here. --- #

# Instantiate a Tkinter window
tk = Tk()
tk.title("Bouncing Game")
tk.resizable(0, 0)  # fix the window size
tk.wm_attributes("-topmost", 1)  # place the window in front of all

# Instantiate a canvas on our window tk
canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
canvas.pack()  # resize canvas to the specified width and height

# Tells tkinter to initialize itself for the animation.
tk.update()

# Instantiate a paddle and a ball
paddle = Paddle(canvas, "blue")
ball = Ball(canvas, paddle, "red")

# A loop as the main game engine keeps redrawing the screen.
while True:
    if ball.hit_bottom == False:  # stop animation if ball hits the bottom
        ball.draw()
        paddle.draw()

    tk.update_idletasks()
    tk.update()

    time.sleep(0.01)  # pause for 10ms
