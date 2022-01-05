import win32gui
import screenshot
import logic
import engine


class Bot:
    def __init__(self, name_window, name_char):
        self.name_char = name_char
        self.name_window = name_window
        self._hwnd = None
        self.city = 'Гиран'
        self.seeds = 1

    def run(self):
        self.make_configs()
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

    def make_configs(self):
        print('Выберите город, в который будете сдавать семена \nГиран\nДион')
        self.city = input()
        print('Выберите номер семян для сдачи: \n')
        self.seeds = input()

    def _activate_window(self):
        self._hwnd = win32gui.FindWindow(self.name_window)
        win32gui.SetForegroundWindow(self._hwnd)


if __name__ == '__main__':
    bot = Bot('lineage2', 'name')
    bot.run()
