#include <ESP8266WiFi.h>
#include <WiFiUdp.h>
#include <OSCBundle.h>
#include <OSCBundle.h>
#include <OSCData.h> 
OSCErrorCode error;
// OSC STUFF

char ssid[] = "********";                 // your network SSID (name)
char pass[] = "********";              // your network password
WiFiUDP Udp;                           // A UDP instance to let us send and receive packets over UDP
const unsigned int localPort =10005;

#include <Wire.h> //Library which allows I2C communication.

 
  
void setup(){
Serial.begin(9600);
WiFi.config(IPAddress(192,168,1,105),IPAddress(192,168,1,1), IPAddress(255,255,255,0)); //first address is for the esp32, second is for the router, third is default

    // Connect to WiFi network
    Serial.println();
    Serial.print("Connecting to ");
    Serial.println(ssid);
    WiFi.begin(ssid, pass);

    while (WiFi.status() != WL_CONNECTED) {
        delay(500);
        Serial.print(".");
    }
    
    Serial.println("");
    Serial.println("WiFi connected");
    Serial.println("IP address: ");
    Serial.println(WiFi.localIP());

    Serial.println("Starting UDP");
    Udp.begin(localPort);
    Serial.print("Local port: ");
    Serial.println(Udp.localPort());



}
 
void loop(){ 
OSCMessage msgIN;
int size;
  if((size = Udp.parsePacket())>0){
    while(size--)
      msgIN.fill(Udp.read());
    if(!msgIN.hasError()){
      msgIN.dispatch("/sync",sync);
    }
  }
}

void sync(OSCMessage &msg) {
  if (msg.isFloat(0)){
    float val =msg.getFloat(0);//THIS IS IMPORTANT
    //int v1State =val;//THIS IS ALSO IMPORTANT
  Serial.print("/sync1: ");
  Serial.println(val);
 }
}


 
