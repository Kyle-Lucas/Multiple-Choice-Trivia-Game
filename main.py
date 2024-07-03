from kivy.app import App
from kivy.core.window import Window
from kivy.clock import Clock

import random

Window.size = (480,860)

class FSTG(App):

    Round = 0
    Score = 0
    Timer = 0
    
    Data = open('Fromsoft-Trivia-Game/data.txt').readlines()
    Question = None
    Options = []
    Answer = None

    Time = 0    # To Keep track of how long it took to answer aswell as as a timer until next seconds loads in
    NotAnswered = True  # For Timer Functions 
    PrevAns = None  # To ensure the Button changes back to normal in next Question

    def UpdateTimer(self):
        Clock.schedule_interval(self.QuestionTimer,1)

    def QuestionTimer(self,dt):
        if self.NotAnswered == True:
            self.root.ids.temp.text = str(round(self.Time)) # the round function works wonders here
            self.Time += dt

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
            self.Options.append(self.Data[i])

        # In Data.txt the first option after the question is the right answer
        # Below will be randomly placed but Options[0] is the correct one
        self.Answer = self.Options[0]

        self.ShuffleOptions() # Quite Obvious
        self.UpdateTimer()  # Once the Question load in the Timer Starts

    # Randomly place Options to choose from
    def ShuffleOptions(self):
        Cache = []
        while len(Cache) < 4:
                RIndex = random.randint(0,len(self.Options) - 1)
                if self.Options[RIndex] not in Cache:
                    Cache.append(self.Options[RIndex])
            
        self.root.ids.opt0.text = Cache[0]
        self.root.ids.opt1.text = Cache[1]
        self.root.ids.opt2.text = Cache[2]
        self.root.ids.opt3.text = Cache[3]
        

    def CheckAns(self, widget):
        self.NotAnswered = False
        if widget.text == self.Answer:  # Correctly Answered
            widget.background_color = .2,1,.2,.6
        else:   # Wrong Answer
            widget.background_color = 1,.2,.2,.6

        self.PrevAns = widget.text  # To Remember which Button was pressed
        self.Reset()    # Quite Obvious

    # Reset everything that was loaded from data.txt and timer maybe?
    def Reset(self):   
        self.Question = None
        self.Options.clear()
        self.Answer = None
        

if __name__ == '__main__':
    FSTG().run()

    

    # Creating a venv and installing kivy (Debian)
    # python3 -m venv Name
    # source ./Name/bin/activate
    # python -m pip install kivy[base] kivy_examples