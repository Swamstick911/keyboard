from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners import DiodeOrientation
from kmk.modules.layers import Layers
from kmk.keys import KC

import keymap

keyboard = KMKKeyboard()
keyboard.modules.append(Layers())

# GPIO pin setup
keyboard.row_pins = (GP2, GP3, GP4, GP5, GP6, GP7)
keyboard.col_pins = (GP8, GP9, GP10, GP9, GP10, GP11, GP12, GP13, GP14, GP15, GP16, GP17, GP18, GP19, GP20, GP21, GP22)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.keymap = keymap.keymap

if __name__ == '__main__':
    keyboard.go()
