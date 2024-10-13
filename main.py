from Head.Mouth import *
from Head.Ear import *
from Head.brain import *
from FUNCTION.Wish import *
from FUNCTION.Greeting import *

def jarvis():
    wish()

    while True:
        text=listen().lower()
        if "jarvis" in text:
            welcome()

jarvis()