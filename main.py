import win32gui
import screenshot
import logic
import engine
import config
import win32con


class Bot:
    def __init__(self, name_window, name_char):
        self.name_char = name_char
        self.name_window = name_window
        self._hwnd = None
        self.city = ()
        self.seeds = ()
        self.count_seeds = 0

    def run(self):
        self.city, self.seeds, self.count_seeds = self._configure()
        self._activate_window()
        screen = screenshot.Screenshot(self.name_window)
        while True:
            engine.begin_dialog(self.name_char)
            img = screen.get_screen()
            cx, cy = logic.find_coord_donate_seeds(img)
            engine.click_mouse(cx, cy)
            img = screen.get_screen()
            check = logic.check_for_person(img)
            engine.work_keyboard(check)
            cx, cy = self.seeds
            engine.click_mouse(cx, cy)
            cx, cy = config.COORD_STEP['change']
            engine.click_mouse(cx, cy)
            cx, cy = config.COORD_STEP['choose_city']
            engine.click_mouse(cx, cy)
            cx, cy = self.city
            engine.click_mouse(cx, cy)
            cx, cy = config.COORD_STEP['count_seeds']
            engine.click_mouse(cx, cy)
            engine.work_keyboard(self.count_seeds)
            cx, cy = config.COORD_STEP['sell']
            engine.click_mouse(cx, cy)

    @staticmethod
    def _configure():
        return config.create_config()

    def _activate_window(self):
        self._hwnd = win32gui.FindWindow(self.name_window)
        win32gui.SetForegroundWindow(self._hwnd)
        win32gui.ShowWindow(self._hwnd, win32con.SW_SHOW)


if __name__ == '__main__':
    bot = Bot('lineage2', 'Manor Manager')
    bot.run()
