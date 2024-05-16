from buzzer_music import music
from time import sleep

from machine import Pin

class RunSong:


    def __init__(self, song):
        # Variables For Motor
        self.song = song

        self.mySong = music(song, pins=[Pin(22)])

        while True:
            print(self.mySong.tick())
            sleep(0.04)

