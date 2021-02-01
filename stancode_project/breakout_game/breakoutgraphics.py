"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40       # Height of a brick (in pixels).
BRICK_HEIGHT = 15      # Height of a brick (in pixels).
BRICK_ROWS = 10        # Number of rows of bricks.
BRICK_COLS = 10        # Number of columns of bricks.
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10       # Radius of the ball (in pixels).
PADDLE_WIDTH = 75      # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels).
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels).

INITIAL_Y_SPEED = 7.0  # Initial vertical speed for the ball.
MAX_X_SPEED = 5      # Maximum initial horizontal speed for the ball.


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH,
                 paddle_height=PADDLE_HEIGHT, paddle_offset=PADDLE_OFFSET,
                 brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS,
                 brick_width=BRICK_WIDTH, brick_height=BRICK_HEIGHT,
                 brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING,
                 title='Breakout'):
        # Create a graphical window, with some extra space.
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.game_start = False
        self.window = GWindow(width=window_width, height=window_height, title=title)
        # Create a paddle.
        self.paddle = GRect(width=paddle_width, height=paddle_height)
        self.paddle.filled = True
        self.paddle_offset = paddle_offset
        self.window.add(self.paddle, (window_width-paddle_width)/2, window_height-paddle_offset)
        # Center a filled ball in the graphical window.
        self.ball = GOval(ball_radius*2, ball_radius*2)
        self.ball.filled = True
        self.window.add(self.ball, window_width/2-ball_radius, window_height/2-ball_radius)
        # Default initial velocity for the ball.
        self.__dy = 0
        self.__dx = 0
        # Calculate times of removing brick
        self.count = 0
        # Draw bricks.
        self.brick_rows = brick_rows
        self.brick_cols = brick_cols
        for i in range(self.brick_rows):
            for j in range(self.brick_cols):
                self.brick = GRect(brick_width, brick_height)
                self.brick.filled = True
                if j == 0 or j == 1:
                    color = 'red'
                elif j == 2 or j == 3:
                    color = 'gold'
                elif j == 4 or j == 5:
                    color = 'yellow'
                elif j == 6 or j == 7:
                    color = 'green'
                else:
                    color = 'blue'
                self.brick.fill_color = color
                self.brick.color = color
                self.window.add(self.brick, (brick_spacing+brick_width)*i, (brick_spacing+brick_height)*j+brick_offset)
        # Initialize our mouse listeners.
        onmousemoved(self.paddle_move)
        onmouseclicked(self.initialize_velocity)

    def set_dx(self):
        self.__dx = -self.__dx

    def set_dy(self):
        self.__dy = -self.__dy

    def reset_ball(self):
        self.window.add(self.ball, self.window.width / 2 - self.ball.width, self.window.height / 2 - self.ball.width)
        self.__dy = 0
        self.__dx = 0
        self.game_start = False

    def initialize_velocity(self, mouse):
        if not self.game_start:
            self.set_ball_velocity()
            self.game_start = True

    def set_ball_velocity(self):
        self.__dx = random.randint(1, MAX_X_SPEED)
        self.__dy = INITIAL_Y_SPEED
        if random.random() > 0.5:
            self.__dx = -self.__dx

    def ball_out_of_window(self):
        is_ball_out_of_window = self.ball.y >= self.window.height
        return is_ball_out_of_window

    def paddle_move(self, mouse):
        if 0 <= mouse.x <= self.window.width-self.paddle.width:
            self.window.add(self.paddle, mouse.x, self.window.height - self.paddle_offset)

    def get_dx(self):
        return self.__dx

    def get_dy(self):
        return self.__dy

    def count(self):
        self.count += 1
        return self.count

    def check_ball(self):
        # Name 4 point of ball
        maybe_1 = self.window.get_object_at(self.ball.x, self.ball.y)
        maybe_2 = self.window.get_object_at(self.ball.x + self.ball.width, self.ball.y)
        maybe_3 = self.window.get_object_at(self.ball.x, self.ball.y + self.ball.width)
        maybe_4 = self.window.get_object_at(self.ball.x + self.ball.width, self.ball.y + self.ball.width)
        # Check if one of point hit paddle or brick
        if maybe_1 is not None:
            # Check if first point hit brick because only bottom of ball will hid paddle
            if maybe_1 is not self.paddle:
                self.set_dy()
                self.window.remove(maybe_1)
                self.count += 1
        else:
            if maybe_2 is not None:
                # Check if second point hit brick because only bottom of ball will hid paddle
                if maybe_2 is not self.paddle:
                    self.set_dy()
                    self.window.remove(maybe_2)
                    self.count += 1
            else:
                if maybe_3 is not None:
                    if maybe_3 is self.paddle:
                        self.set_dy()
                    else:
                        self.set_dy()
                        self.window.remove(maybe_3)
                        self.count += 1
                else:
                    if maybe_4 is not None:
                        if maybe_4 is self.paddle:
                            self.set_dy()
                        else:
                            self.set_dy()
                            self.window.remove(maybe_4)
                            self.count += 1

    def all_clear(self):
        is_all_clear = self.count == self.brick_cols*self.brick_rows
        return is_all_clear

    def remove_ball(self):
        self.window.remove(self.ball)

    def game_over(self):
        game_over = GLabel('Game Over')
        game_over.font = 'Georgia-50-Bold'
        self.window.add(game_over, (self.window.width-game_over.width)/2, (self.window.height-game_over.height)/2)
