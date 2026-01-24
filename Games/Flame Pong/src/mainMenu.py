from typing import Literal
from backdrop import Backdrop
from constants import SCREEN_WIDTH, SCREEN_HEIGHT

class MainMenu:
    def __init__(self):
        self.buttons = []
        self.text = []
        self.backdrops = []
        self.active = False
        self.currentUI: Literal["Start", "Settings", "Game Selection"] = "Start"

    def updateMenu(self):
        if self.currentUI == "Start":
            main_menu_bg = Backdrop((100, 100), SCREEN_WIDTH - 200, SCREEN_HEIGHT - 200, (0, 0, 0), 0.1)
            self.backdrops.append(main_menu_bg)
        elif self.currentUI == "Game Selection":
            pass
        elif self.currentUI == "Settings":
            pass