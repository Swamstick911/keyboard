from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from keymap import keymap 

keyboard = KMKKeyboard()

keyboard.col_pins = (board.GP8, board.GP9, ..., board.GP22)
keyboard.row_pins = (board.GP2, boardGP3, ..., board.GP7)

keyboard.diode_orientation = DiodeOrientation.COL2ROW
keyboard.keymap = keymap

if __name__ == "__main__":
    keyboard.go
    