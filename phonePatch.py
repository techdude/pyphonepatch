"""
Caleb Begly
phonePatch
Created for CS370 Independent Project
"""
import subprocess
import time

def phoneListener(char):
    print "Recieved Character: "+char
    if(phoneListener.state == 0):
        print "State 0"
        if(char == "*"):
            phoneListener.state = 1
    elif(phoneListener.state == 1):
        print "State 1"
        if(char == "1"):
            phoneListener.state = 2
        else:
            phoneListener.state = 0
    elif(phoneListener.state == 2):
        print "State 2"
        if(char == "1"):
            phoneListener.state = 3
        else:
            phoneListener.state = 0
    elif(phoneListener.state == 3):
        print "State 3"
        if(char == "#"):
            phoneListener.numberBuffer = "" #Reset the buffer
            phoneListener.state = 4
        else:
            phoneListener.state = 0
    elif(phoneListener.state == 4): # Read in the number and store it
        print "State 4"
        if(char == "#"): #Done entering
            #Call Number
	    print "Calling "+phoneListener.numberBuffer
	    phoneListener.connection = subprocess.Popen(['/bin/bash', '-c', '/usr/bin/linphonec -c /home/pi/.linphonerc -s '+phoneListener.numberBuffer])
            phoneListener.state = 5
        else:
            phoneListener.numberBuffer += char #add to buffer
    elif(phoneListener.state == 5):
        print "State 5"
        if(char == "*"):
            phoneListener.state = 6
    elif(phoneListener.state == 6):
        print "State 6"
        if(char == "2"):
            phoneListener.state = 7
        else:
            phoneListener.state = 5
    elif(phoneListener.state == 7):
        print "State 7"
        if(char == "2"):
            phoneListener.state = 8
        else:
            phoneListener.state = 5
    elif(phoneListener.state == 8):
        print "State 8"
        if(char == "#"): #End the phone call
	    phoneListener.connection.terminate()
            phoneListener.state = 0
        else:
            phoneListener.state = 5
        
#Init
phoneListener.state = 0  
phoneListener.numberBuffer = ""
phoneListener.connection = None

"""
#Tests
phoneListener("*")
phoneListener("1")
phoneListener("1")
phoneListener("#")
phoneListener("1")
phoneListener("7")
phoneListener("2")
phoneListener("0")
phoneListener("3")
phoneListener("4")
phoneListener("0")
phoneListener("7")
phoneListener("7")
phoneListener("6")
phoneListener("5")
phoneListener("#")
phoneListener("#")
phoneListener("#")
time.sleep(5)
phoneListener("*")
phoneListener("2")
phoneListener("2")
phoneListener("#")
phoneListener("#")
phoneListener("#")
phoneListener("#")
"""
