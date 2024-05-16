import sys
sys.path.insert(1, '/home/atbox/Documents/IFB102_Assignment3_Project/buzzer_tunes/')
import RPi.GPIO as GPIO
import random
from time import sleep
#Importing @... from foldar
from buzzer_tunes import PlayMidi, SongsMidi, buzzer_music, machine

#Confiration
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#Global Config

#LEDs = [14, 18, 5, 15, 16, 12, 20, 21]

# #L298n Pins
# Ena, In1, In2 = 6, 5, 11

#Peizo Buzzer
#22

#LEDs
#A: R 14, O 15, G 18, W 5
#B R 16, O 12

class DriveMotor:
    #Low High is backwards
    #High LOW is farward

    def __init__(self, enable, input1, input2):
        #Variables For Motor
        self.enable = enable
        self.input1 = input1
        self.input2 = input2

        #Defining motor as output
        GPIO.setup(self.enable, GPIO.OUT)
        GPIO.setup(self.input1, GPIO.OUT)
        GPIO.setup(self.input2, GPIO.OUT)

        #Setting PWM Speed
        self.PWM = GPIO.PWM(self.enable, 1000)
        self.PWM.start(0)  # Starting Duty %

    def Drive(self, polarity = 'B', speed=15):

        #IF/ELSE Statement for choosing between Forward or Backward motor.
        if polarity == 'F':
            GPIO.output(self.input1, GPIO.LOW)
            GPIO.output(self.input2, GPIO.HIGH)
        else:
            GPIO.output(self.input1, GPIO.HIGH)
            GPIO.output(self.input2, GPIO.LOW)
        self.PWM.ChangeDutyCycle(speed)

    def Stop(self):
        self.PWM.ChangeDutyCycle(0)

class Buzzer:
    def __init__(self, Song):
        self.Song = Song

    def Play(self):
        PlayMidi.RunSong(self.Song)

    def Stop(self):
        a = machine.Stop()

class Patterns:

    # def __init__(self, pattern):
    #     self.pattern = pattern
    def ModifyList(self, i = 0, ii = 0, iii = 0, iv = 0, v = 0, vi = 0, vii = 0, viii = 0, time = 0.1):

        InputList = [i, ii, iii, iv, v, vi, vii, viii]
        for LED in InputList:
            if LED != 0:
                GPIO.setup(LED, GPIO.OUT)
                GPIO.output(LED, GPIO.HIGH)
                sleep(time)
                GPIO.output(LED, GPIO.LOW)
            else:
                pass

class LEDsystem:
    def __init__(self):
        #self.Pattern = Pattern

        self.LEDs = [14, 18, 23, 15
                    , 16, 12, 20, 21]
        self.PowerState = [GPIO.LOW, GPIO.HIGH]
        self.LED = None


    def PowerStates (self, boolean):
        while True:
            for self.LED in self.LEDs:
                GPIO.setup(self.LED, GPIO.OUT)
                GPIO.output(self.LED, self.PowerState[boolean])

    # def CoolLookingThings (self, Pattern = 1, time = 1):
    #     while True:
    #         for self.LED in self.LEDs:
    #             GPIO.setup(self.LED, GPIO.OUT)
    #             GPIO.output(self.LED, GPIO.HIGH)
    #             sleep(time)
    #             GPIO.output(self.LED, GPIO.LOW)

    def PatternMaker(self, pattern):

        PatternObject = Patterns()
        delayList = [0.3, 0.4, 0.08, 1]

        match pattern:
            case 1:
                while True:
                #Sides Style
                    PatternObject.ModifyList(14, 18, 23, 15, delayList[0])
                    sleep(delayList[3])
                    PatternObject.ModifyList(16, 12, 20, 21, delayList[0])
            case 2:
                #Alternating between Colours
                while True:
                    PatternObject.ModifyList(14, 16, time = delayList[1])
                    PatternObject.ModifyList(18, 12, time = delayList[1])
                    PatternObject.ModifyList(23, 20, time = delayList[1])
                    PatternObject.ModifyList(15, 21, time = delayList[1])

            case 3:
                #Rotate through LEDs
                while True:
                    PatternObject.ModifyList(14, 18, 23, 15
                    , 21, 20, 12, 16, time=0.08)
            case 4:
                #Checkers
                while True:
                    PatternObject.ModifyList(14, 21, time = delayList[1])
                    sleep(delayList[5])
                    PatternObject.ModifyList(15, 16, time = delayList[1])
                    sleep(delayList[5])
                    PatternObject.ModifyList(18, 20, time = delayList[1])
                    sleep(delayList[5])
                    PatternObject.ModifyList(23, 12, time = delayList[1])

            case 5:
                #Random Order
                while True:
                    random.shuffle(self.LEDs)
                    print(self.LEDs)
                    PatternObject.ModifyList(self.LEDs[0], self.LEDs[1], self.LEDs[2], self.LEDs[3], self.LEDs[4], self.LEDs[5], self.LEDs[6], self.LEDs[7], time=delayList[1])
            case _:
                PatternObject.ModifyList(14, 18, 23, 15
                    , 16, 12, 20, 21, time=delayList[1])


# class Button:
#     def __init__(self, pin):
#         self.pin = pin
#         GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
#

class Main:
    MotorObject = DriveMotor(6, 5, 11)
    BuzzerObject = Buzzer(SongsMidi.RusAntheme)
    LEDObject = LEDsystem()
    GPIO.setup(26, GPIO.IN)
    #Test = Patterns(1)

    #MotorObject.Stop()


    while True:
        if GPIO.input(26) == GPIO.HIGH:


            MotorObject.Drive('F', 50 )
            #BuzzerObject.Play()

            # sleep(0.1)
            LEDObject.PatternMaker(5)
            #MotorObject.Stop()
            #sleep(0.1)
            #LEDObject.PowerStates[0]
        elif GPIO.input(26) == GPIO.LOW:
            LEDObject.PatternMaker(1)




    #MotorObject.Stop()
    #LEDObject.PowerStates(0)
    #GPIO.cleanup()




RunInstance = Main()

