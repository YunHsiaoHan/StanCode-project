"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics
from campy.graphics.gobjects import GLabel

# Constant variables
FRAME_RATE = 1000 / 120  # 120 frames per second
NUM_LIVES = 3			 # Number of attempts

# Global variables
score = 0                # Score of the game.
score_label = GLabel('Score: ' + str(score))


def main():
    """
    This program create breakout game.
    """
    global score
    graphics = BreakoutGraphics()
    score_label.font = '-20'
    graphics.window.add(score_label, x=0, y=graphics.window.height)
    lives = NUM_LIVES

    # Add the animation loop here!
    while True:
        pause(FRAME_RATE)
        vx = graphics.ball_x()    # Ball moving x velocity.
        vy = graphics.ball_y()    # Ball moving y velocity.
        if graphics.start:
            graphics.ball.move(vx, vy)

            # Find object while ball touched.
            obj1 = graphics.window.get_object_at(graphics.ball.x, graphics.ball.y)
            obj2 = graphics.window.get_object_at(graphics.ball.x, graphics.ball.y+graphics.ball.width)
            obj3 = graphics.window.get_object_at(graphics.ball.x+graphics.ball.height, graphics.ball.y)
            obj4 = graphics.window.get_object_at(graphics.ball.x+graphics.ball.height,
                                                 graphics.ball.y+graphics.ball.width)

            # Check the ball four corners.
            # Top left corner.
            if obj1 is not None:                   # When ball touching an object.
                if obj1 is not graphics.paddle and obj1 is not score_label:        # Ball touching brick.
                    graphics.window.remove(obj1)
                    # vy = graphics.bounce_y()
                    graphics.bounce_y()
                    score += 1
                    score_label.text = 'Score: ' + str(score)
                elif obj1 == graphics.paddle and not graphics.touch_paddle:  # While ball touching paddle.
                    # vy = graphics.bounce_y()
                    graphics.bounce_y()
                    graphics.touch_paddle = True  # This check point prevent ball touch paddle continuously.
                if graphics.ball.y + graphics.ball.height < graphics.paddle.y:
                    graphics.touch_paddle = False

            # Bottom left corner.
            elif obj2 is not None:
                if obj2 is not graphics.paddle and obj2 is not score_label:
                    graphics.window.remove(obj2)
                    # vy = graphics.bounce_y()
                    graphics.bounce_y()
                    score += 1
                    score_label.text = 'Score: ' + str(score)
                elif obj2 == graphics.paddle and not graphics.touch_paddle:
                    # vy = graphics.bounce_y()
                    graphics.bounce_y()
                    graphics.touch_paddle = True
                if graphics.ball.y + graphics.ball.height < graphics.paddle.y:
                    graphics.touch_paddle = False

            # Top right corner.
            elif obj3 is not None:
                if obj3 is not graphics.paddle and obj3 is not score_label:
                    graphics.window.remove(obj3)
                    # vy = graphics.bounce_y()
                    graphics.bounce_y()
                    score += 1
                    score_label.text = 'Score: ' + str(score)
                elif obj3 == graphics.paddle and not graphics.touch_paddle:
                    # vy = graphics.bounce_y()
                    graphics.bounce_y()
                    graphics.touch_paddle = True
                if graphics.ball.y + graphics.ball.height < graphics.paddle.y:
                    graphics.touch_paddle = False

            # Bottom right corner.
            elif obj4 is not None:
                if obj4 is not graphics.paddle and obj4 is not score_label:
                    graphics.window.remove(obj4)
                    # vy = graphics.bounce_y()
                    graphics.bounce_y()
                    score += 1
                    score_label.text = 'Score: ' + str(score)
                elif obj4 == graphics.paddle and not graphics.touch_paddle:
                    # vy = graphics.bounce_y()
                    graphics.bounce_y()
                    graphics.touch_paddle = True
                if graphics.ball.y + graphics.ball.height < graphics.paddle.y:
                    graphics.touch_paddle = False

            # While ball touching the edge of window.
            # Ball touch the right and left walls.
            if graphics.ball.x <= 0 or graphics.ball.x + graphics.ball.width >= graphics.window.width:
                # vx = graphics.bounce_x()
                graphics.bounce_x(-vx)
            if graphics.ball.y <= 0:      # Ball touch the top of the window.
                # vy = graphics.bounce_y()
                graphics.bounce_y()
            if graphics.ball.y + graphics.ball.height >= graphics.window.height:  # Ball touch the bottom of the window.
                graphics.reset_ball()
                graphics.start = False
                lives -= 1

            if lives == 0:                    # There's no life to play the game.
                graphics.game_over()
                break

            if score == graphics.brick_num:   # Clean all bricks.
                graphics.break_game()
                break


if __name__ == '__main__':
    main()
