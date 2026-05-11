from gpiozero import Button, LED
from signal import pause

# Initialize LED on GPIO pin 14 and Button on GPIO pin 4
led = LED(14)
button = Button(4)

# Define event handlers for button actions
button.when_pressed = led.on   # Turn the LED on when the button is pressed
button.when_released = led.off # Turn the LED off when the button is released

# Keep the program running to listen for events
pause()