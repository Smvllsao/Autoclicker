import pyautogui as ptg
import time
from pynput.mouse import Listener

class Tracker:
    def __init__(self):
        self.data_base = []

    def on_click(self, x, y, button, pressed):
        if pressed:
            self.x = x
            self.y = y
            self.button = button
            self.data_base.append((self.x, self.y, self.button))
    def update(self):
        try:
            with Listener(on_click=self.on_click) as listener:
                listener.join()
        except:
            raise ValueError('Error while joining listener')
    def append_list(self,list):
        list.append(self.data_base)
        self.data_base = []

mouse = Tracker()

while True:
    mouse.update()
    
