"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

Name: Yu-Shan Cheng
"""
from campy.gui.events.mouse import onmouseclicked
from campy.gui.events.timer import pause

from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 10         # 100 frames per second
NUM_LIVES = 3			# Number of attempts

is_moving = False
is_brick = False
is_paddle = False

def main():
    # Add the animation loop here!
    # update, check, pause
    graphics = BreakoutGraphics()
    global is_moving
    dy = graphics.get_dy()
    dx = graphics.get_dx()
    life = NUM_LIVES
    while True:
        pause(FRAME_RATE)
        if graphics.is_moving:
            graphics.ball_move()
            while True:
                collisions = graphics.check_collision()
                if collisions == 1:
                    dy = -dy
                if collisions == 2:
                    if dy > 0:
                        dy = -dy
                    else:
                        dy = dy
                if graphics.ball.x <= 0 or graphics.ball.x + graphics.ball.width >= graphics.window.width:
                    dx = -dx
                if graphics.ball.y <= 0:
                    dy = -dy
                if graphics.ball.y + graphics.ball.height  >= graphics.window.height:
                    life -= 1
                    graphics.reset_ball()
                    break
                if graphics.collision_times >= graphics.win_points:
                    break
                graphics.ball.move(dx, dy)
                pause(FRAME_RATE)
            graphics.is_moving = False
        elif graphics.collision_times >= graphics.win_points:
            graphics.window.remove(graphics.paddle)
            graphics.window.remove(graphics.ball)
            graphics.window.add(graphics.label_2, x=(graphics.window.width - graphics.label_2.width) / 2,
                                y=(graphics.window.height - graphics.label_2.height))
            print('YOU WIN')
            break
        elif life <= 0:
            graphics.window.remove(graphics.ball)
            graphics.window.remove(graphics.paddle)
            graphics.window.add(graphics.label_1, x=(graphics.window.width - graphics.label_1.width) / 2,
                                y=(graphics.window.height - graphics.label_1.height))
            print('YOU LOSE')
            break
        else:
            pass
        pause(FRAME_RATE)


if __name__ == '__main__':
    main()
