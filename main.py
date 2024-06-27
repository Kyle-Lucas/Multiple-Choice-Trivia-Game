from kivy.app import App
from kivy.core.window import Window

import random

Window.size = (480,860)

class FSTG(App):

    Round = 0
    Score = 0
    Timer = 0
    
    Question = None
    Answers = []

    def LoadQue(self):
        RandQue: str = random.choice(self.Questions)
        self.root.ids.que.text = RandQue

    def CheckAns(self, widget):
        if widget.text == 'Dark Souls 3':
            print(f'Correct Answer!')

if __name__ == '__main__':
    FSTG().run()

    

    # Creating a venv and installing kivy (Debian)
    # python3 -m venv Name
    # source ./Name/bin/activate
    # python -m pip install kivy[base] kivy_examples