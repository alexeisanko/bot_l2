import win32gui
from PIL import ImageGrab
import numpy as np


class Screenshot:

    def __init__(self, name_window):
        self.name_window = name_window
        self.window_info = {}

    def _get_window_info(self):
        win32gui.EnumWindows(self._set_window_coordinates, self.window_info)

    def _set_window_coordinates(self, hwnd, window_info):
        if win32gui.IsWindowVisible(hwnd) and self.name_window in win32gui.GetWindowText(hwnd):
            rect = win32gui.GetWindowRect(hwnd)
            window_info['x1'] = rect[0]
            window_info['y1'] = rect[1]
            window_info['x2'] = rect[2]
            window_info['y2'] = rect[3]
            window_info['name'] = win32gui.GetWindowText(hwnd)

    def get_screen(self):
        self._get_window_info()
        box = (self.window_info['x1'],
               self.window_info['y1'],
               self.window_info['x2'],
               self.window_info['y2'])
        return np.array(ImageGrab.grab(bbox=box))
