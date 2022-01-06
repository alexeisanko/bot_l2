import pyautogui
import win32gui
import win32con


def get_window_info():
    window_info = []
    win32gui.EnumWindows(set_window_coordinates, window_info)


def set_window_coordinates(hwnd, window_info):
    if win32gui.IsWindowVisible(hwnd):
        print(hwnd, win32gui.GetWindowText(hwnd))

def emulation(window):
    win32gui.ShowWindow(window, win32con.SW_SHOW)
    win32gui.SetForegroundWindow(window)
    pyautogui.move(100, 0)
    pyautogui.press('enter')
    pyautogui.write('fdfdfdddfdf')


if __name__ == '__main__':
    emulation(1311722)