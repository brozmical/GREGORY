#OSC variables and libraries
from pythonosc import dispatcher
from pythonosc import osc_server
from pythonosc import osc_message_builder
from pythonosc import udp_client

import argparse

#sr libraries
import speech_recognition as sr
r =sr.Recognizer()
m = sr.Microphone()
stop_listening = None;

def callback(recognizer,audio):
    print("data recieved from thread")
    try:
        data = r.recognize_google(audio)
        print(data)
        client.send_message("/data",data)
    except sr.UnknownValueError:
        print("we didn't recognize that phrase")
    except sr.RequestError:
        print("No access to the API, check access to the API")


def calibrate_threshold(unused_addr,args):
    print("calibration received")
    client.send_message("/calibration", "Calibration commenced")
    try:
        with m as source:
            r.adjust_for_ambient_noise(source,duration =1.0)
            client.send_message("/calibration", "Minimum threshold set to {}".format(r.energy_threshold))
    except (KeyboardInterrupt):
        print("keyboard interrupt received")
        pass
 
def start_listening(unused_addr,args):
    global stop_listening
    print("start_listening")
    client.send_message("/startedListening","Listening thread started")
    stop_listening = r.listen_in_background(m,callback,phrase_time_limit =5.0)
    return
    
def stop_listening(unused_addr,args):
    global stop_listening
    print ("stopping")
    client.send_message("/stoppedListening","stopped microphone thread")
    stop_listening(wait_for_stop=False)
 
if __name__=="__main__":
    ip = "127.0.0.1"
    sendPort = 7000
    inPort = 8000
    
    #sending osc messages on
    client = udp_client.SimpleUDPClient(ip,sendPort)
    #catches osc messages
    dispatcher = dispatcher.Dispatcher()
    dispatcher.map("/calibrate",calibrate_threshold)
    dispatcher.map("/startListening",start_listening)
    dispatcher.map("/stopListening",stop_listening)
    
    
    #set up server to listen to OSC messages
    server =osc_server.ThreadingOSCUDPServer((ip,inPort),dispatcher)
    print("servering on {}".format(server.server_address))
    server.serve_forever()