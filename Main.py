import sys
sys.path.insert(1, '/home/atbox/Documents/IFB102_Assignment3_Project/buzzer_tunes/')
from Modules import DriveMotor, Buzzer, LEDsystem

from buzzer_tunes import PlayMidi, SongsMidi, buzzer_music, machine

from gpiozero import Button
from time import sleep
import threading

PressButton = Button(26)

#class



class Main:
#SimpleRhythme
#Chrismas_Music


    def __init__(self):
        self.MotorObject = DriveMotor(6, 5, 11)
        self.BuzzerObject = Buzzer(SongsMidi.SimpleRhythme, PressButton)
        self.LEDObject = LEDsystem(PressButton)
        self.RunInstance()


    def RunInstance(self):
        while True:


            if PressButton.value == 1:
                self.BuzzerObject.mySong.restart()
                sleep(0.04)
                LEDThread = threading.Thread(target=self.LEDObject.PatternMaker, args=(1,))
                BuzzerThread = threading.Thread(target=self.BuzzerObject.Play)
                self.MotorObject.Drive('B', 25)

                LEDThread.start()
                BuzzerThread.start()

                LEDThread.join()
                BuzzerThread.join()

                #sleep(0.5)

            else:
                #sleep(0.5)
                self.MotorObject.Stop()
                self.BuzzerObject.mySong.stop()

                continue










MainInstance = Main()
