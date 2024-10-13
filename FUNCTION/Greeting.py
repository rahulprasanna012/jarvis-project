import random
from Data.brain_data.DLG import welcomedlg
from Head.Mouth  import speak


def welcome():
    welcome = random.choice(welcomedlg)
    speak(welcome)
    return