import pygame as pg

class Backdrop:
    def __init__(self, width, height, color, transparency):
        self.width = width
        self.height = height
        self.color = color
        self.transparency = transparency

        self.backdrop_object = self.create_backdrop()

    def create_backdrop(self):
        backdrop = pg.Surface((self.width, self.height), pg.SRCALPHA)
        r, g, b = self.color
        backdrop.fill((r, g, b, self.transparency))
        return backdrop

