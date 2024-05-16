from gpiozero import LED, TonalBuzzer, Button, Motor
from gpiozero.tones import Tone
from signal import pause
# led_yellow = LED(26)
# led_red = LED(6)
# led_white = LED(5)

motor = Motor(forward=5, backward=9)

ledA_red = LED(14)
ledA_orange = LED(15)
ledA_green = LED(18)
ledB_red = LED(16)
ledB_orange = LED(12)

button = Button(26)

buzzer = TonalBuzzer(22)

#buzzer.play(Tone(220.0))

#buzzer.stop()

while True:
    if button.is_pressed:
        ledA_red.blink()
        ledA_orange.blink()
        ledA_green.blink()
        #ledA_white.blink()
        ledB_red.blink()
        ledB_orange.blink()
led_yellow.blink()
led_red.blink()
led_white.blink()

motor.forward()
#pause()
