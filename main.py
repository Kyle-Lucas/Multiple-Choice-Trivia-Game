from kivy.app import App
from kivy.core.window import Window

Window.size = (480,860)

class FSTG(App):

    Round = 0
    Score = 0
    Timer = 0
    
    Questions = ["In which game do you use the 'Coiled Sword Fragment'\n to respawn at the last Check Point",
                 "What is required before you are able to Fast Travel \n in Dark souls (1)?",
                 "What is the Name of the Onion Knight\n in Dark Souls 3?"]

    Answers0 = ['Demons Souls', 'Dark Souls 2: SotFS', 'Dark Souls 3', 'Elden Ring']
    Answers1 = ['Restore Humanity', 'Defeat 4 Great Souls', 'Defeat Ornstein and Smough', 'Place the Lord Vessel' ]
    Answers2 = ['Siegward of Catarina', 'Siegmeyer of Catarina', 'Siegmayer of Catarina', 'Sieglinde of Catarina']

    def LoadAns(self,widget):
        pass

    def CheckAns(self, widget):
        if widget.text == 'Dark Souls 3':
            print(f'Correct Answer!')

if __name__ == '__main__':
    FSTG().run()

    

    # Creating a venv and installing kivy (Debian)
    # python3 -m venv Name
    # source ./Name/bin/activate
    # python -m pip install kivy[base] kivy_examples