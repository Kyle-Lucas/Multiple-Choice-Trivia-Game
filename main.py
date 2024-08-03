from kivy.app import App
from kivy.core.window import Window
from kivy.clock import Clock

import random

Window.size = (480,860)

class TriviaGame(App):

    Data = open('Fromsoft-Trivia-Game/data.txt').readlines()

    GameStart: bool = False
    Score: int = 0
    Score_Factor: int = 10
    RandomQuestions: bool = True
    
    Questions: list = [] # Stores all the Questions Asked
    Question: str = None 
    Options: list = []
    Answer: str = None

    Time: float = 0    # To Keep track of how long it took to answer aswell as a timer until next question loads in
    NotAnswered: bool = True  # For Timer Functions 
    
    @classmethod
    def nQuestions(self) -> int:   # Returns Total Questions in Data.txt
        n = 0
        for q in range(0, len(self.Data)):
            if self.Data[q] == '\n':
                n += 1
        return n

    # Interesting Bug i found with the kivy Clock.schedule_interval() function
    # If u dont unschedule it, it will just keep running
    # So if u call UpdateTimer below again it will run another instance of the callback everytime
    def UpdateTimer(self):
        Clock.schedule_interval(self.QuestionTimer,1)

    def QuestionTimer(self,dt):
        if self.NotAnswered == True:
            self.root.ids.temp.text = f'TIME\n{round(self.Time) + 1}' # the round function works wonders here
            self.Time += dt
        else:
            Clock.unschedule(self.QuestionTimer) # Here i make sure this instance of the callback is unscheduled

    def LoadQue(self):
        TriviaGame.GameStart = True
        self.Reset()

        if TriviaGame.RandomQuestions == False:
            if len(TriviaGame.Questions) == 0:
                Line = 0
                while self.Question == None:
                    if self.Data[Line] == '\n':
                        self.Question = self.Data[Line + 1]
                        TriviaGame.Questions.append(self.Question)
                        self.root.ids.que.text = self.Question
                    else:
                        Line += 1

                for i in range(Line + 2,Line + 6):
                    self.Options.append(self.Data[i])

                self.Answer = self.Options[0]
                self.ShuffleOptions() 
                self.UpdateTimer()  
                self.root.ids.remain.text = f'{len(self.Questions)}/{self.nQuestions()}'

            else:
                Line = self.Data.index(self.Questions[-1]) + 6
                self.Question = self.Data[Line]
                TriviaGame.Questions.append(self.Question)
                self.root.ids.que.text = self.Question

                for i in range(Line + 1,Line + 5):
                    self.Options.append(self.Data[i])

                self.Answer = self.Options[0]
                self.ShuffleOptions() 
                self.UpdateTimer()  
                self.root.ids.remain.text = f'{len(self.Questions)}/{self.nQuestions()}'

        else:
            while self.Question == None:
                RIndex = random.randint(0,len(self.Data) - 1)
                if self.Data[RIndex] == '\n' and self.Data[RIndex + 1] not in TriviaGame.Questions: #Check if we havent Asked this Questiom yet
                    self.Question = self.Data[RIndex + 1]
                    TriviaGame.Questions.append(self.Question)
                    self.root.ids.que.text = self.Question
    
            # The Answers will follow in the next 4 lines
            for i in range(RIndex + 2,RIndex + 6):
                self.Options.append(self.Data[i])
    
            # In Data.txt the first option after the question is the right answer
            # Below will be randomly placed but Options[0] is the correct one
            self.Answer = self.Options[0]
            self.ShuffleOptions()
            self.UpdateTimer() 
            self.root.ids.remain.text = f'{len(self.Questions)}/{self.nQuestions()}'

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

    def if_Wrong(self):
        if self.root.ids.opt0.text == self.Answer:
            self.root.ids.opt0.background_color = .2,1,.2,.6
        if self.root.ids.opt1.text == self.Answer:
            self.root.ids.opt1.background_color = .2,1,.2,.6
        if self.root.ids.opt2.text == self.Answer:
            self.root.ids.opt2.background_color = .2,1,.2,.6
        if self.root.ids.opt3.text == self.Answer:
            self.root.ids.opt3.background_color = .2,1,.2,.6

    def CheckAns(self, widget):
        # When an Answer is chosen
        if self.NotAnswered == True and TriviaGame.GameStart == True:
            self.NotAnswered = False
            if widget.text == self.Answer:  # Correctly Answered
                TriviaGame.Score += (TriviaGame.Score_Factor - round(self.Time))
                widget.background_color = .2,1,.2,.6
            else:   # Wrong Answer
                widget.background_color = 1,.2,.2,.6
                self.if_Wrong()

            self.root.ids.temp.text = f"It took you {round(self.Time)} seconds to answer\n Click Here to Load the Next Question"
            self.root.ids.score.text = str(TriviaGame.Score)

        #When one of the Option Buttons are pressed before Starting the Game
        if TriviaGame.GameStart == False:
            self.Settings(widget.text)

    def Settings(self,text):
        if 'ON' in text:
            TriviaGame.RandomQuestions = False
            self.root.ids.opt2.text = 'Randomized Questions: OFF'
            print(f'Randomized Questions: {TriviaGame.RandomQuestions}')
        elif 'OFF' in text: 
            TriviaGame.RandomQuestions = True
            self.root.ids.opt2.text = 'Randomized Questions: ON'
            print(f'Randomized Questions: {TriviaGame.RandomQuestions}')
        elif '+10' in text:
            TriviaGame.Score_Factor = 20
            self.root.ids.opt3.text = 'Score: +20 if Correct \n-1 For every Second you take to Answer'
            print(f'Change Score Setting/Difficulty')
        elif '+20' in text:
            TriviaGame.Score_Factor = 10
            self.root.ids.opt3.text = 'Score: +10 if Correct \n-1 For every Second you take to Answer'
            print(f'Change Score Setting/Difficulty')

    # Reset everything that was loaded from data.txt, timer and Button color that was changed
    def Reset(self):   
        self.Question = None
        self.Options.clear()
        self.Answer = None
        self.NotAnswered = True
        self.Time = 0

        # I should figure out how i can just change the button that was clicked
        self.root.ids.opt0.background_color = .2,.2,.2,.7
        self.root.ids.opt1.background_color = .2,.2,.2,.7
        self.root.ids.opt2.background_color = .2,.2,.2,.7
        self.root.ids.opt3.background_color = .2,.2,.2,.7

if __name__ == '__main__':
    TriviaGame().run()

    

    # Creating a venv and installing kivy (Debian)
    # python3 -m venv Name
    # source ./Name/bin/activate
    # python -m pip install kivy[base] kivy_examples