"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

Name: Yu-Shan Cheng
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

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
INITIAL_Y_SPEED = 5    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball

class BreakoutGraphics:
    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):
        # Create a graphical window, with some extra space
        self.paddle_width = PADDLE_WIDTH
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)
        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height)
        self.paddle.filled = True
        self.window.add(self.paddle, x=(self.window.width-self.paddle.width)/2, y=(self.window.height - paddle_offset))
        # Center a filled ball in the graphical window
        ball_radius = BALL_RADIUS
        self.ball = GOval(2 * ball_radius, 2 * ball_radius)
        self.ball.filled = True
        self.ball.fill_color = "black"
        self.window.add(self.ball, x=(self.window.width - ball_radius)/2, y=(self.window.height - ball_radius)/2)
        # Draw bricks
        for i in range(brick_rows):
            for j in range(brick_cols):
                self.brick = GRect(brick_width, brick_height)
                self.brick.filled = True
                position_x = j * (self.brick.width + brick_spacing)
                position_y = brick_offset + i * (self.brick.height + brick_spacing)
                if i % 10 < 2:
                    self.brick.color = "red"
                    self.brick.fill_color = "red"
                elif i % 10 < 4:
                    self.brick.color = "orange"
                    self.brick.fill_color = "orange"
                elif i % 10 < 6:
                    self.brick.color = "yellow"
                    self.brick.fill_color = "yellow"
                elif i % 10 < 8:
                    self.brick.color = "green"
                    self.brick.fill_color = "green"
                else:
                    self.brick.color = "blue"
                    self.brick.fill_color = "blue"
                self.window.add(self.brick, x=position_x, y=position_y)
        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = INITIAL_Y_SPEED
        # Initialize our mouse listeners
        self.is_brick = False
        self.is_paddle = False
        self.is_moving = False
        onmouseclicked(self.start)
        onmousemoved(self.move_paddle)
        self.check_collision()
        self.ball_bounce()
        self.ball_move()
        self.collision = 0
        self.collision_times = 0
        self.win_points = brick_cols * brick_rows
        # Labels for win or lose
        self.label_1 = GLabel('You Lose')
        self.label_1.font = '-50'
        self.label_2 = GLabel('You Win!')
        self.label_2.font = '-50'
    def start(self, event):
        self.is_moving = True


    def ball_move(self):
        ball_radius = BALL_RADIUS
        if self.ball.x <= 0 or self.ball.x + 2 * ball_radius >= self.window.width:
            self.__dx = -self.__dx
        if self.ball.y <= 0:
            self.__dy = -self.__dy
        self.ball.move(self.__dx, self.__dy)

    def move_paddle(self, drag):
        self.paddle.x = drag.x - self.paddle.width / 2
        if self.paddle.x < 0:
            self.paddle.x = 0
        if self.paddle.x + self.paddle.width > self.window.width:
            self.paddle.x = self.window.width - self.paddle.width


    def get_dx(self):
        return self.__dx

    def get_dy(self):
        return self.__dy

    def reset_ball(self):
        self.window.remove(self.ball)
        self.window.add(self.ball, x=(self.window.width-self.ball.width)/2,
                        y=(self.window.height-self.ball.height)/2)


    def hit_wall(self):
        if self.ball.x <= 0 or self.ball.x + self.ball.width > self.window.width:
            self.__dx = -self.__dx
        if self.ball.y <= 0 or self.ball.y + self.ball.height > self.window.height:
            self.__dy = -self.__dy

    def check_collision(self):
        for x in range(int(self.ball.x), int(self.ball.x + self.ball.width)+1, self.ball.width):
            for y in range(int(self.ball.y), int(self.ball.y + self.ball.height)+1, self.ball.height):
                point = self.window.get_object_at(x, y)
                if point is not None:
                    if point != self.paddle:
                        self.collision = 1
                        self.window.remove(point)
                        self.collision_times += 1

                    else:
                        self.collision = 2  # hit paddle
                    return self.collision



    def ball_bounce(self):
        # MAX_SPEED,MIN_Y_SPEED並沒有打算讓user改變，因此用常數（大寫）
        self.__dx = random.randint(1, MAX_X_SPEED)
        if random.random() > 0.5:
            self.__dx = -self.__dx
        if random.random() > 0.5:
            self.__dy = -self.__dy
        self.__dx = -self.__dx
        self.__dy = -self.__dy
        self.__dy -= 1
        self.ball.move(self.__dx, self.__dy)
