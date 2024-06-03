import kivy
import random

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class FirstPage(App):
    
    def build(self):
        self.window = FloatLayout()
        self.window.cols = 1
        self.window.size_hint = (0.6, 0.7)
        self.window.pos_hint = {'center_x': 0.5, 'center_y': 0.5}

        self.header = Label(text="Daily Planner",
                            size_hint = (0.2,0.2),
                            pos_hint = {'center_x': 0.5, 'center_y': 0.8},
                            valign = ('top'),
                            font_size = 128, 
                            bold = True,
                            color = '#745E59')
        
        self.button = Button(text="New Page",
                             #pos = (0, 7000),
                             size = (300, 100),
                             bold = True,
                             size_hint = (None, None),
                             font_size = 64,
                             pos_hint = {'center_x': 0.5, 'center_y': 0.2},
                             background_color = '#745E59',
                             background_normal = "")

        self.window.add_widget(self.header)
        self.window.add_widget(self.button)

        return self.window


if __name__ == '__main__':   
    FirstPage().run()