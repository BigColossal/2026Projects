from typing import Literal

class mainMenu:
    def __init__(self):
        self.buttons = []
        self.text = []
        self.currentUI: Literal["Start", "Settings", "Game Selection"] = "Start"

    def updateMenu(self):
        if self.currentUI == "Start":
            pass
        elif self.currentUI == "Game Selection":
            pass
        elif self.currentUI == "Settings":
            pass

    def start_background_game(self):
        pass