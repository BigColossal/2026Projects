from typing import Literal

class MainMenu:
    def __init__(self):
        self.buttons = []
        self.text = []
        self.active = False
        self.currentUI: Literal["Start", "Settings", "Game Selection"] = "Start"

    def updateMenu(self):
        if self.currentUI == "Start":
            pass
        elif self.currentUI == "Game Selection":
            pass
        elif self.currentUI == "Settings":
            pass