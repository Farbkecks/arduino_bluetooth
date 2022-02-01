import serial
import time
import keyboard


print("Start")
port="COM5"
bluetooth=serial.Serial(port, 9600)
print("Connected")
bluetooth.flushInput() #This gives the bluetooth a little kick


winkel = 90
bluetooth.write(str.encode(str(winkel)))

winkel_new = winkel
while True:
    if winkel != winkel_new:
        winkel = winkel_new
        bluetooth.write(str.encode(str(winkel_new)))
    if keyboard.is_pressed("a") and winkel_new > 0:
        winkel_new -= 10
    if keyboard.is_pressed("d") and winkel_new < 180:
        winkel_new += 10
    time.sleep(.1)
bluetooth.close() #Otherwise the connection will remain open until a timeout which ties up the /dev/thingamabob
print("Done")