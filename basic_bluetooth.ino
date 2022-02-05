#include "SoftwareSerial.h"
#include <Servo.h>

Servo servoblau;
SoftwareSerial serial_connection(10, 11);//Create a serial connection with TX and RX on these pins

char inData;
int winkel = 90;
int LED = 3;
int SCHRITT =  10;

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
  byte byte_count=serial_connection.available();//This gets the number of bytes that were sent by the python script
  if(byte_count)//If there are any bytes then deal with them
  {

    inData=serial_connection.read();
    Serial.println(inData);
    if(inData=='0'){
      digitalWrite(LED,0);
    }
    if(inData=='1'){
      if(winkel<180){
        winkel = winkel + SCHRITT;
      }
      digitalWrite(LED, 0);
    }
    if(inData=='2'){
      if(winkel>0){
        winkel = winkel - SCHRITT;
      }
      digitalWrite(LED, 0);
    }
    if(inData=='3'){
      digitalWrite(LED, 1);
    }
    if(inData=='4'){
      if(winkel<180){
        winkel = winkel + SCHRITT;
      }
      digitalWrite(LED, 1);
    }
    if(inData=='5'){
      if(winkel>0){
        winkel = winkel - SCHRITT;
      }
      digitalWrite(LED, 1);
    }
    servoblau.write(winkel);
    
  }
  delay(100);//Pause for a moment 
}