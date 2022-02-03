import serial
import time
import keyboard


print("Start")
port="COM5"
bluetooth=serial.Serial(port, 9600)
print("Connected")
bluetooth.flushInput() #This gives the bluetooth a little kick
info = [0,0]
while True:
    info = [0,0]
    if keyboard.is_pressed("a"):
        info[0] = 1
    elif keyboard.is_pressed("d"):
        info[0] = 2
    if keyboard.is_pressed("w"):
        info[1] = 1
    time.sleep(.1)
    bluetooth.write(str.encode(f"{info[0]}{info[1]}"))
    # print(f"{info[0]}{info[1]}")
bluetooth.close() #Otherwise the connection will remain open until a timeout which ties up the /dev/thingamabob
print("Done")