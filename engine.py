import pyautogui
import win32gui
import time


def begin_dialog(name):
    pass


def click_mouse(cx, cy, fast=True):
    if fast:
        pyautogui.moveTo(cx, cy)
    else:
        slow_move(cx, cy)
        pass
    pyautogui.click()


def work_keyboard(text):
    pyautogui.write(text)
    pyautogui.press('enter')


def draw_line(x1=0, y1=0, x2=0, y2=0):
    coordinates = []
    dx = x2 - x1
    dy = y2 - y1
    sign_x = 1 if dx > 0 else -1 if dx < 0 else 0
    sign_y = 1 if dy > 0 else -1 if dy < 0 else 0
    if dx < 0:
        dx = -dx
    if dy < 0:
        dy = -dy
    if dx > dy:
        pdx, pdy = sign_x, 0
        es, el = dy, dx
    else:
        pdx, pdy = 0, sign_y
        es, el = dx, dy
    x, y = x1, y1
    error, t = el / 2, 0
    coordinates.append([x, y])
    while t < el:
        error -= es
        if error < 0:
            error += el
            x += sign_x
            y += sign_y
        else:
            x += pdx
            y += pdy
        t += 1
        coordinates.append([x, y])
    return coordinates


# Smooth move mouse from current pos to xy
def slow_move(x, y):
    flags, hcursor, (startX, startY) = win32gui.GetCursorInfo()
    coordinates = draw_line(startX, startY, x, y)
    x = 0
    for dot in coordinates:
        x += 1
        if x % 2 == 0 and x % 3 == 0:
            time.sleep(0.01)
        pyautogui.moveTo(dot[0], dot[1])


if __name__ == '__main__':
    pyautogui.moveTo(100, 100)
