import serial
import time
import keyboard


print("Start")
port="COM5"
bluetooth=serial.Serial(port, 9600)
print("Connected")
bluetooth.flushInput() #This gives the bluetooth a little kick
while True:
    if keyboard.is_pressed("a"):
        bluetooth.write(b"1")
    if keyboard.is_pressed("d"):
        bluetooth.write(b"2")
    time.sleep(.1)
bluetooth.close() #Otherwise the connection will remain open until a timeout which ties up the /dev/thingamabob
print("Done")