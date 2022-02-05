from re import I
import serial
import time
import keyboard


print("Start")
port="COM5"
bluetooth=serial.Serial(port, 9600)
print("Connected")
bluetooth.flushInput() #This gives the bluetooth a little kick
info_olt = 1
while True:
    info = 0
    if keyboard.is_pressed("a"):
        info += 1
    elif keyboard.is_pressed("d"):
        info += 2
    if keyboard.is_pressed("w"):
        info += 3
    time.sleep(.1)
    # if info != info_olt:
    #     info_olt = info
    #     # print(info_olt)
    #     bluetooth.write(str.encode(str(info_olt)))
    bluetooth.write(str.encode(str(info)))



bluetooth.close() #Otherwise the connection will remain open until a timeout which ties up the /dev/thingamabob
print("Done")