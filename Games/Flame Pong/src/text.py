import pygame as pg

class Text:
    def __init__(self, text, color):
        self.font = pg.font.SysFont('Arial', 32)
        self.text = text
        self.color = color
        
    
    def create_text(self):
        return self.font.render(self.text, True, self.color)

    