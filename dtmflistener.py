"""
Caleb Begly
dtmflistener
Created for CS370 Independent Project
"""
import sys
import time
import getopt
import alsaaudio
import struct
from DtmfDetectorStream import DtmfDetectorStream
import phonePatch

#Code below for basic read modified from documentation example
card = "default"
detector.inp = alsaaudio.PCM(alsaaudio.PCM_CAPTURE, alsaaudio.PCM_NONBLOCK, card)

# Set attributes: Mono, 8000 Hz, 16 bit little endian samples
detector.inp.setchannels(1)
detector.inp.setrate(8000)
detector.inp.setformat(alsaaudio.PCM_FORMAT_S16_LE)

# The period size controls the internal number of frames per period.
detector.inp.setperiodsize(160) 
# End code from documentation

#Include detector
detector = DtmfDetectorStream()
detector.setCharacterListener(phonePatch.phoneListener) #Attach listener to the stream detector

#Read dtmf tones
while True:
    # Read data from device
    packet, data = detector.inp.read()
      
    if packet:
        samples = [data[i:i+2] for i in range(0, len(data), 2)] #Break into samples
	for sample in samples:
	    (point,) = struct.unpack("h", sample)
	    detector.goertzel(point)
        time.sleep(.001)
