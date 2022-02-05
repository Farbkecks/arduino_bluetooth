#include "SoftwareSerial.h"
#include <Servo.h>

Servo servoblau;
SoftwareSerial serial_connection(10, 11);//Create a serial connection with TX and RX on these pins

char inData;
int WINKEL = 90;
int LED = 3;
int SCHRITT =  10;

void setup()
{
  // Serial.begin(9600);//Initialize communications to the serial monitor in the Arduino IDE
  serial_connection.begin(9600);//Initialize communications with the bluetooth module
  // Serial.println("Started");//Tell the serial monitor that the sketch has started.
  pinMode(LED, OUTPUT);
  servoblau.attach(8);
}
void loop()
{
  byte byte_count=serial_connection.available();//This gets the number of bytes that were sent by the python script
  if(byte_count)//If there are any bytes then deal with them
  {
    inData=serial_connection.read();
    // Serial.println(inData);
    if(inData=='0'){
      digitalWrite(LED,0);
    }
    if(inData=='1'){
      if(WINKEL<180){
        WINKEL = WINKEL + SCHRITT;
      }
      digitalWrite(LED, 0);
    }
    if(inData=='2'){
      if(WINKEL>0){
        WINKEL = WINKEL - SCHRITT;
      }
      digitalWrite(LED, 0);
    }
    if(inData=='3'){
      digitalWrite(LED, 1);
    }
    if(inData=='4'){
      if(WINKEL<180){
        WINKEL = WINKEL + SCHRITT;
      }
      digitalWrite(LED, 1);
    }
    if(inData=='5'){
      if(WINKEL>0){
        WINKEL = WINKEL - SCHRITT;
      }
      digitalWrite(LED, 1);
    }
    servoblau.write(WINKEL);
  }
  delay(100);//Pause for a moment 
}