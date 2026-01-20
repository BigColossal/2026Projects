from text import Text
from backdrop import Backdrop

class Button:
    def __init__(self, text, backdrop_color, backdrop_transparency, text_color, width, height, pos, action):
        self.text = text
        self.backdrop_color = backdrop_color
        self.backdrop_transparency = backdrop_transparency
        self.text_color = text_color
        self.width = width
        self.height = height
        self.action = action

        self.text_object = Text(text, text_color)
        self.backdrop_object = Backdrop(pos, width, height, backdrop_color, backdrop_transparency)

    
    
