from kivy.app import App
from kivy.core.window import Window

import random

Window.size = (480,860)

class FSTG(App):

    Round = 0
    Score = 0
    Timer = 0
    
    Data = open('Fromsoft-Trivia-Game/data.txt').readlines()
    Question = None
    Answers = []

    def LoadQue(self):
        # While we havnt found a question, find a line in Data.txt that only has a /n
        # The Line following that /n will be our question
        while self.Question == None:
            RIndex = random.randint(0,len(self.Data) - 1)
            if self.Data[RIndex] == '\n':
                self.Question = self.Data[RIndex + 1]
                self.root.ids.que.text = self.Question
        # The Answers will follow in the next 4 lines
        for i in range(RIndex + 2,RIndex + 6):
            self.Answers.append(self.Data[i])

        # In Data.txt the first option after the question is the right answer
        # Below will be randomly placed but Answers[0] is the correct one
        self.root.ids.opt0.text = self.Answers[0]
        self.root.ids.opt1.text = self.Answers[1]
        self.root.ids.opt2.text = self.Answers[2]
        self.root.ids.opt3.text = self.Answers[3]

    def CheckAns(self, widget):
        if widget.text == self.Answers[0]:
            print(f'Correct Answer!')

if __name__ == '__main__':
    FSTG().run()

    

    # Creating a venv and installing kivy (Debian)
    # python3 -m venv Name
    # source ./Name/bin/activate
    # python -m pip install kivy[base] kivy_examples