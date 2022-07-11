"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

# Constant Variables
BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Height of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # Create a graphical window, with some extra space
        self.window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        self.window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=self.window_width, height=self.window_height, title=title)

        # Create a paddle
        self.paddle = GRect(width=paddle_width, height=paddle_height)
        self.paddle_offset = PADDLE_OFFSET
        self.paddle.filled = True
        self.window.add(self.paddle, x=(self.window_width-paddle_width)/2,
                        y=self.window_height-paddle_offset-paddle_height)

        # Center a filled ball in the graphical window
        self.ball = GOval(width=ball_radius*2, height=ball_radius*2)
        self.ball.filled = True
        self.window.add(self.ball, x=(self.window_width-self.ball.width)/2, y=(self.window_height-self.ball.height)/2)

        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = 0

        # Check point
        self.start = False            # Check the game is start or not
        self.touch_paddle = False     # Check the ball is touch the paddle last time

        # Initialize our mouse listeners
        onmouseclicked(self.ball_moving)
        onmousemoved(self.paddle_control)

        # Draw bricks
        brick_x = 0
        brick_y = 0
        self.brick_num = brick_rows * brick_cols   # Total brick number
        for i in range(brick_rows):
            for j in range(brick_cols+1):
                self.brick = GRect(width=brick_width, height=brick_height)
                self.brick.filled = True
                if i < 2:
                    self.brick.fill_color = 'red'
                elif i < 4:
                    self.brick.fill_color = 'orange'
                elif i < 6:
                    self.brick.fill_color = 'yellow'
                elif i < 8:
                    self.brick.fill_color = 'green'
                else:
                    self.brick.fill_color = 'blue'
                self.window.add(self.brick, x=brick_x, y=brick_y)
                brick_x = j*(brick_width+brick_spacing)
                brick_y = i*(brick_height+brick_spacing)

    def paddle_control(self, event):
        """
        This function controls paddle moving by mouse
        :param event: Mouse event, this controls mouse moving
        """
        paddle_x = event.x - self.paddle.width/2    # This controls paddle value when moving mouse
        paddle_y = self.window.height-self.paddle_offset-self.paddle.height  # Paddle y value
        if paddle_x < 0:  # If mouse move out of the left site of window
            paddle_x = 0
        if paddle_x > self.window.width-self.paddle.width:  # If mouse move out of the right site of window
            paddle_x = self.window.width - self.paddle.width
        self.window.add(self.paddle, x=paddle_x, y=paddle_y)

    def ball_velocity(self):
        """
        This define the ball velocity.
        """
        self.__dx = random.randint(1, MAX_X_SPEED)
        self.__dy = INITIAL_Y_SPEED
        if random.random() > 0.5:
            self.__dx = -self.__dx

    def ball_x(self):
        """
        :return: Ball x velocity
        """
        return self.__dx

    def bounce_x(self, new_dx):
        """
        :return: Ball bouncing x velocity
        """
        self.__dx = new_dx

    def ball_y(self):
        """
        :return: Ball y velocity
        """
        return self.__dy

    def bounce_y(self):
        """
        :return: Ball bouncing y velocity
        """
        self.__dy *= -1

    def ball_moving(self, event):
        """
        Making ball start moving while clicking mouse.
        :param event: MouseEvent, happens while clicking mouse.
        """
        if not self.start:        # Check ball is moving or not.
            self.start = True
            self.ball_velocity()

    def reset_ball(self):
        """
        After ball touch the button of window, reset ball to start again.
        """
        self.window.add(self.ball, x=(self.window_width - self.ball.width) / 2,
                        y=(self.window_height - self.ball.height) / 2)

    def game_over(self):
        """
        If there's no life to play game, print 'Game over' on window.
        """
        text = GLabel('Game Over')
        text.font = '-40'
        text.color = 'gray'
        self.window.add(text, x=(self.window.width - text.width) / 2, y=(self.window.height / 2 + text.height))

    def break_game(self):
        """
        If clean all bricks, print 'You Win' on window.
        """
        text = GLabel('You Win!!!')
        text.font = '-60'
        text.color = 'red'
        self.window.add(text, x=(self.window.width - text.width) / 2, y=(self.window.height / 2 + text.height))