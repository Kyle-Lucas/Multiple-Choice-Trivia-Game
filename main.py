from kivy.app import App
from kivy.core.window import Window

Window.size = (480,860)

class FSTG(App):
    
    Questions = ["In which game do you use the 'Coiled Sword Fragment'\n to respawn at last check point",
                 "Who is Solaire of Astora?"]

    Answers = ['Demons Souls', 'Dark Souls 2: SotFS', 'Dark Souls 3', 'Elden Ring']

if __name__ == '__main__':
    FSTG().run()

    

    # Creating a venv and installing kivy (Debian)
    # python3 -m venv Name
    # source ./Name/bin/activate
    # python -m pip install kivy[base] kivy_examples