from gtts import gTTS
import os
from betterplaysound import betterplaysound, playsound


def announcement(announcements):
    voice=gTTS(text=announcements,lang='en',slow=False)
    voice.save("announcement.mp3")
    playsound("announcement.mp3")
    os.remove("announcement.mp3")



