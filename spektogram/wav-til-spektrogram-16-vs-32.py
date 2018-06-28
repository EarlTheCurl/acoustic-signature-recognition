#import the pyplot and wavfile modules 

import matplotlib.pyplot as plot
from scipy.io import wavfile

 

# Read the wav file (mono)

samplingFrequency16, signalData16 = wavfile.read('test16bit.wav')
samplingFrequency32, signalData32 = wavfile.read('test32bit.wav')
 

# Plot the signal read from wav file

plot.subplot(211)
plot.title('16 bits')
plot.specgram(signalData16,Fs=samplingFrequency16)
plot.xlabel('Tid')
plot.ylabel('Frekvens')

plot.subplot(212)
plot.title('32 bits')
plot.specgram(signalData32,Fs=samplingFrequency32)
plot.xlabel('Tid')
plot.ylabel('Frekvens')

plot.show()