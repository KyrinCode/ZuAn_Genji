'''
['alt', 'alt_l', 'alt_r', 'backspace', 'caps_lock', 'cmd', 'cmd_r', 'ctrl', 'ctrl_l', 'ctrl_r', 'delete',
'down', 'end', 'enter', 'esc', 'f1', 'f10', 'f11', 'f12', 'f13', 'f14', 'f15', 'f16', 'f17', 'f18', 'f19', 'f2', 'f20',
'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'home', 'insert', 'left', 'menu', 'num_lock', 'page_down', 'page_up', 'pause',
'print_screen', 'right', 'scroll_lock', 'shift', 'shift_r', 'space', 'tab', 'up']
'''
import random
from pynput.keyboard import Key, Controller, Listener

keyboard = Controller()
D = []
cnt = 0

def on_press(key):
    try:
        print('alphanumeric key {0} pressed'.format(key))
    except AttributeError:
        print('special key {0} pressed'.format(key))

def on_release(key):
    try:
        print('alphanumeric key {0} released'.format(key))
        if key.char == '0':
            s = random_line()
            keyboard.type(s)
            keyboard.press(Key.enter)
            keyboard.release(Key.enter)
        if key.char == '9':
            with keyboard.pressed(Key.cmd):
                keyboard.press('a')
                keyboard.release('a')
            keyboard.press(Key.backspace)
            keyboard.release(Key.backspace)
    except AttributeError:
        print('special key {0} released'.format(key))

def random_line():
    i = random.randrange(0, cnt, 1)
    line =  D[i].replace("\n", "")
    return line

def main():
    filename = "fragrance.txt"
    with open(filename, 'r') as f:
        global D, cnt
        D = f.readlines()
        cnt = len(D)

    print("------------------------\n")
    print("<- (- 祖安源氏已上线 -) ->\n")
    print("------------------------\n")
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

if __name__ == "__main__":
    main()