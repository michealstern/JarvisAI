from pynput.keyboard import key, Controller

from time import sleep

keyboard = Controller()

def volumeup():
    for i in range(5):
        keyboard.press(key.media_valume_up)
        keyboard.release(key.media_valume_up)
        sleep(0.1)

def volumdown():
    for i in range(5):
        keyboard.press(key.media_valume_down)
        keyboard.release(key.media_valume_down)
        sleep(0.1)