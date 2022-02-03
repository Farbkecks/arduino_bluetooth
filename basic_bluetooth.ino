#include "SoftwareSerial.h"
#include <Servo.h>

Servo servoblau;

SoftwareSerial serial_connection(10, 11);//Create a serial connection with TX and RX on these pins
#define BUFFER_SIZE 64//This will prevent buffer overruns.
char inData[BUFFER_SIZE];//This is a character buffer where the data sent by the python script will go.
char a2[BUFFER_SIZE-1];
char inChar=-1;//Initialie the first character as nothing
int i=0;

int winkel = 90;


int LED = 3;

void setup()
{
  Serial.begin(9600);//Initialize communications to the serial monitor in the Arduino IDE
  serial_connection.begin(9600);//Initialize communications with the bluetooth module
  serial_connection.println("Ready!!!");//Send something to just start comms. This will never be seen.
  Serial.println("Started");//Tell the serial monitor that the sketch has started.
  pinMode(LED, OUTPUT);
  servoblau.attach(8);
}
void loop()
{
  //This will prevent bufferoverrun errors
  byte byte_count=serial_connection.available();//This gets the number of bytes that were sent by the python script
  if(byte_count)//If there are any bytes then deal with them
  {
    Serial.println("Incoming Data");//Signal to the monitor that something is happening
    int first_bytes=byte_count;//initialize the number of bytes that we might handle. 
    int remaining_bytes=0;//Initialize the bytes that we may have to burn off to prevent a buffer overrun
    if(first_bytes>=BUFFER_SIZE-1)//If the incoming byte count is more than our buffer...
    {
      remaining_bytes=byte_count-(BUFFER_SIZE-1);//Reduce the bytes that we plan on handleing to below the buffer size
    }
    for(i=0;i<first_bytes;i++)//Handle the number of incoming bytes
    {
      inChar=serial_connection.read();//Read one byte
      inData[i]=inChar;//Put it into a character string(array)
    }
    inData[i]='\0';//This ends the character array with a null character. This signals the end of a string
    for(i=0;i<remaining_bytes;i++)//This burns off any remaining bytes that the buffer can't handle.
    {
      inChar=serial_connection.read();
    }

    if(inData[0] == '1' && winkel < 180){
      winkel = winkel + 10;
    }

     if(inData[0] == '2' && winkel > 0){
      winkel = winkel - 10;
    }

    Serial.print("Winkel: ");
    Serial.println(winkel);

    // analogWrite(LED, String(inData).toInt());
    servoblau.write(winkel);

  }
  delay(100);//Pause for a moment 
}