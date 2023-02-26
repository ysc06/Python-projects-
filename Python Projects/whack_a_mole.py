"""
File: whack_a_mole.py
Name: 
---------------------------
This program plays a game called
"whack a mole" in which players 
clicking the popping moles 
on screen to gain scores 
"""

from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GLabel
from campy.graphics.gimage import GImage
from campy.gui.events.mouse import onmouseclicked
from campy.gui.events.timer import pause
import random

# Constants control the diameter of the window
WINDOW_WIDTH = 850
WINDOW_HEIGHT = 550

# Constant controls the pause time of the animation
DELAY = 700

# Global variables
# TODO:

window = GWindow(width = WINDOW_WIDTH, height = WINDOW_HEIGHT, title = "Whack a whole")
score = 0  #python 認為是常數，不能改，python不會看大小寫
score_label = GLabel("Score => " + str(score))

def main():
    score_label.font = "-80"  #font 大小必須有引號
    window.add(score_label, x = 0, y =score_label.height)  #必須加座標，因GLabel的初始座標在左下角，若不設定為0,label.height 就看不到label的字串
    onmouseclicked(remove_mole)
    while True:
        filepath = "mole.png"
        img = GImage(filepath)
        random_x = random.randint(0, window.width - img.width)
        random_y = random.randint(0, window.height - img.height)
        window.add(img, x=random_x, y = random_y)
        pause(DELAY)  #Without a pause(DELAYS), your laptop will be overloaded and will get frozen. Refer to handout pg. 12 about animation.


def remove_mole(mouse):
    global score # must let python know this variable is global variable ＃要改變的東西都要告訴python是全域變數
    maybe_obj = window.get_object_at(mouse.x, mouse.y)  #得到座標上的物件
    if maybe_obj is not None and maybe_obj is not score_label:   #None只有第一個字大寫
        window.remove(maybe_obj)
        score += 1
        score_label.text = "Score => "+str(score)    #把label裡的文字換掉：label.text = "new" 沒有括號 ＃變數要改，文字也要改


if __name__ == '__main__':
    main()
