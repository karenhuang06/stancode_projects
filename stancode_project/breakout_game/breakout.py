"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 1000 / 120  # 120 frames per second.
NUM_LIVES = 3


def main():
    graphics = BreakoutGraphics()
    # Add animation loop here!
    lives = NUM_LIVES
    while True:
        dx = graphics.get_dx()
        dy = graphics.get_dy()
        pause(FRAME_RATE)
        # Restart the game when the ball is out of window
        if graphics.all_clear():
            graphics.remove_ball()
            break
        if graphics.ball_out_of_window():
            lives -= 1
            if lives > 0:
                graphics.reset_ball()
            else:
                break
        graphics.ball.move(dx, dy)
        # Change direction when ball hit the wall
        if graphics.ball.x <= 0 or graphics.ball.x+graphics.ball.width >= graphics.window.width:
            graphics.set_dx()
        if graphics.ball.y <= 0:
            graphics.set_dy()
        graphics.check_ball()
    graphics.game_over()


if __name__ == '__main__':
    main()
