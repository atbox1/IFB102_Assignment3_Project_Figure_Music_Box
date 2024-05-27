import sys
#sys.path.insert(1, '/home/atbox/Documents/IFB102_Assignment3_Project/buzzer_tunes/')
sys.path.insert(1, '/home/atbox/Documents/IFB102_Assignment3_Project/buzzer_tunes/')

from Modules import DriveMotor, Buzzer, LEDsystem

from buzzer_tunes import PlayMidi, SongsMidi, buzzer_music, machine
from gpiozero import Button
from time import sleep
from threading import Thread
from flask import Flask, render_template, request

PressButton = Button(26)

app = Flask(__name__)

#class

class RunFlask:
    def __init__(self):
        if __name__ == '__main__':
            app.run()

@app.route('/home', methods = ['GET', 'POST'])
def HomeScreen():
    
    if request.method == 'POST':
        print(request.form.get('motorSpeed'))
        print(request.form.get('lightPattern'))

    return render_template('home.html')



class Main:
#SimpleRhythme
#Chrismas_Music


    def __init__(self):
        self.MotorObject = DriveMotor(6, 5, 11)
        self.BuzzerObject = Buzzer(SongsMidi.Chrismas_Music , PressButton)
        self.LEDObject = LEDsystem(PressButton)
        self.RunInstance()
        self.FlaskInstance = RunFlask




    def RunInstance(self):
        while True:


            if PressButton.value == 1:

                self.BuzzerObject.mySong.restart()
                sleep(0.0001)

                LEDThread = Thread(target=self.LEDObject.PatternMaker, args=(8,), daemon=True)
                BuzzerThread = Thread(target=self.BuzzerObject.Play, daemon=True)

                self.MotorObject.Drive('B', 20)

                LEDThread.start()
                BuzzerThread.start()


                LEDThread.join()
                BuzzerThread.join()




            else:

                self.MotorObject.Stop()
                self.BuzzerObject.mySong.stop()

            continue





# if __name__ == '__main__':
#    app.run()
flaskThread = Thread(target=RunFlask, daemon=True)
Maininstance = Thread(target=Main, daemon=True)

flaskThread.start()
Maininstance.start()

flaskThread.join()
Maininstance.join()

#MainInstance = Main()




# RunFlask.start()
#MainInstance.start()



# RunFlask.join()

#MainInstance.join()












