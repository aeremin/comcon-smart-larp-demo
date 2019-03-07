import paho.mqtt.client as paho
from pyautogui import press, typewrite, hotkey

BROKER = 'raspberrypi'
BUTTON_ID = '0x00158d0002b0535d'


def on_message(client, userdata, message):
    payload = str(message.payload)
    if 'single' in payload:
        hotkey('right')
    if 'double' in payload:
        hotkey('left')


client = paho.Client('presentation-clicker')

client.on_message = on_message

print('Connecting to broker', BROKER)
client.connect(BROKER)
print('Subscribing...')
client.subscribe('zigbee2mqtt/' + BUTTON_ID)
client.loop_forever()
