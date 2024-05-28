import sys
sys.path.insert(1, '/home/atbox/Documents/IFB102_Assignment3_Project/buzzer_tunes/')

from Modules import DriveMotor, Buzzer, LEDsystem
from inspect import getmembers, isfunction

from buzzer_tunes import PlayMidi, SongsMidi, buzzer_music, machine
from gpiozero import Button
from time import sleep
from threading import Thread
from flask import Flask, render_template, request, session, g




PressButton = Button(26)

app = Flask(__name__)
app.secret_key = 'secret!'




#class

class RunFlask:
    def __init__(self):
        if __name__ == '__main__':
            app.run()
        

@app.route('/HOME', methods = ['GET', 'POST'])
def HomeScreen():
    InstanceOptionsDict = {
        "state": [],
        "MotorSpeed": [],
        "Polarity": [],
        "LightPattern": [],
        "BuzzerTone": []
    }
    
    
    MusicList = dir(SongsMidi)
    RemoveList = ['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__']    
    
    for Word in range(0, len(RemoveList)):
        MusicList.remove(RemoveList[Word])
    
    session["A"] = InstanceOptionsDict

    session["A"]["state"].append(request.form.get('instanceState'))
    session["A"]["MotorSpeed"].append(request.form.get('motorSpeed'))
    InstanceOptionsDict["Polarity"].append(request.form.get('inlineRadioOptions'))
    InstanceOptionsDict["LightPattern"].append(request.form.get('lightPattern'))
    InstanceOptionsDict["BuzzerTone"].append(request.form.get('MusicSelect'))
    
    
    
    return render_template('home.html', MusicList = MusicList), InstanceOptionsDict
@app.route('/', methods=['GET'])
class Main:
#SimpleRhythme
#Chrismas_Music


    def __init__(self):
        self.MotorObject = DriveMotor(6, 5, 11)
        self.BuzzerObject = Buzzer(SongsMidi.Chrismas_Music , PressButton)
        self.LEDObject = LEDsystem(PressButton)
        self.RunInstance()
        
    def RunInstance(self):
        while True:
                        
            if PressButton.value == 1:
                #self.song = Chrismas_Music
                self.BuzzerObject.mySong.restart()
                sleep(0.04)

                LEDThread = Thread(target=self.LEDObject.PatternMaker, args=(8,), daemon=True)
                BuzzerThread = Thread(target=self.BuzzerObject.Play, daemon=True)

                self.MotorObject.Drive('B', 20)

                LEDThread.start()
                BuzzerThread.start()


                LEDThread.join()
                BuzzerThread.join()


            else:
                self.BuzzerObject.mySong.stop()
                self.MotorObject.Stop()
                print(session.get("A"))
            continue




# if __name__ == '__main__':
#    app.run()
flaskThread = Thread(target=RunFlask, daemon=True)
#Maininstance = Thread(target=Main, daemon=True)

flaskThread.start()
#Maininstance.start()

flaskThread.join()
#Maininstance.join()

#MainInstance = Main()




# RunFlask.start()
#MainInstance.start()



# RunFlask.join()

#MainInstance.join()












