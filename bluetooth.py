import serial
import time

eingabe_helligkeit = input("Helligkeit: ")
# eingabe_winkel = input("Winkel: ")



print("Start")
port="COM5" #This will be different for various devices and on windows it will probably be a COM port.
bluetooth=serial.Serial(port, 9600)#Start communications with the bluetooth unit
print("Connected")
bluetooth.flushInput() #This gives the bluetooth a little kick
# bluetooth.write(str.encode(eingabe_helligkeit) + b";"  + str.encode(eingabe_winkel))
bluetooth.write(str.encode(eingabe_helligkeit))
bluetooth.close() #Otherwise the connection will remain open until a timeout which ties up the /dev/thingamabob
print("Done")