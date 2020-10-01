#!/usr/bin/python
# coding=utf8
## Verhalten von / wie in Python 3    a/b  = float

from __future__ import division, print_function
from future.builtins import input

from math import pi

### Audio-Module

import pyaudio
from scipy.io import wavfile

###  Fourier, Numerik

import numpy.fft as FFT
import numpy as np


##############

# Graphik

import matplotlib.pyplot as plt


###

CHANNELS=1
RATE=44100
DAUER=1
ANZAHL=DAUER*RATE # ANZAHL der Frames,

# globale Variablen, schlechter Programmierstil, hier aber ganz
# praktisch: Nach Aufnahme oder Lesen werden diese Variablen 
# entsprechend gesetzt.


def recordsnd(filename, time):
	'''
	Nimmt eine  time  Sekunden lange Schallsequenz
	auf (mit der Samplerate 48000 Hz) auf und speichert,
	speichert sie in der Datei filename und gibt die
	Aufnahme als numpy-array mit Werten zwischen -1 und 1 zurück
	'''
	global ANZAHL
	global RATE
	global DAUER
	global CHANNELS 
	
	DAUER=time
	ANZAHL=int(RATE*DAUER)
	
	
	p = pyaudio.PyAudio()
	input("Aufnehmen  "+str(time)+ " Sekunden): Eingabetaste druecken...")
	
	stream = p.open(format =pyaudio.paInt16 ,
                channels = CHANNELS,
	                rate = RATE,
	                input = True,
	                frames_per_buffer = 1024)#ANZAHL)
	
	
	yy=stream.read(ANZAHL)
	y=np.fromstring(yy,dtype=np.short)
	if CHANNELS==2:
		y=y.reshape((y.shape[0]//2,2))

	print(("Aufgenomen: " + str(ANZAHL) + " Frames"))
	stream.close()
	p.terminate()
	yy=np.array(y,dtype='d')/32768.0
	if filename!=None:
		wavwrite(filename, yy)
		
	return yy


def wavwrite(filename, y):
	'''Schreibt ein wav-File aus einem numpy-array'''
	wavfile.write(filename, RATE, np.array(y*2**15, dtype=int))
	
	
def wavread(filename):
	'''Liest ein wav-File in ein numpy-Array'''
	global ANZAHL
	global RATE
	global DAUER
	global CHANNELS 
	
	RATE,y=wavfile.read(filename)
	ANZAHL=y.shape[0]
	if len(y.shape)==2:
		CHANNELS=y.shape[1]
	else:
		CHANNELS=1
	DAUER=ANZAHL/RATE
	
	return np.array(y,dtype=np.float)/2**15
		
				
	
				
				
def playsnd(y, r):
	'''
	spielt das numpy-array (bzw. Vektor) y als Klang 
	mit der Samplerate r  [Hz] ab.
	'''
	def callback(in_data, frame_count, time_info, status):
		data = (32767*klanggen.generate(frame_count/RATE)).astype(np.int16)
		return (data.copy(), pyaudio.paContinue)
	
	
	p = pyaudio.PyAudio()

	CHUNK=2**12
	
	stream = p.open(format =pyaudio.paInt16 ,
			channels = CHANNELS,
			rate = r,
			output = True,
			frames_per_buffer=CHUNK)
			#callback=callback)#ANZAHL)
		
	
	yy=np.array(y.flatten()*2**15,dtype=np.short)
	for i in range(0,len(yy),CHUNK):
		stream.write(yy[i:i+CHUNK].tostring(order='F'))
	stream.close()
	p.terminate()
	


def inspectsnd(y):
	'''Zeigt einen Plot von y'''
	
	n=y.shape[0]
	fig=plt.Figure(figsize=(6,4),dpi=100)
	ax=fig.add_subplot(111)
	x=np.arange(0,n,1)/np.float32(RATE)
	plt.plot(x,y)
	
	plt.show()



def inspectspec(y):
	'''zeigt einen Plot des DFT-Spektrums von y'''
	global RATE
	
	#  Vorbereitungen, um ein Fenster zum Plotten zu kriegen
	plt.figure(1)

	n=len(y)
	window=np.blackman(n)
	sumw=sum(window*window)
	
	A=FFT.fft(y*window) 
	B2=(A*np.conjugate(A)).real
	sumw*=2.0   
	sumw/=1/np.float(RATE)  # sample rate
	B2=B2/sumw
	
	
	x=np.arange(0,n/2,1)/np.float(n)*RATE
	
	
	eps=1e-8
	plt.plot(x, np.log10(B2[0:n/2]+eps))
	plt.show()
	
def sinewave(f,r,d):
	'''erzeugt die Daten einer Sinusschwingung mit Frequenz f, Dauer d
	und Samplerate r'''
	global RATE
	global DAUER
	global ANZAHL
	
	RATE=r
	DAUER=d
	ANZAHL=DAUER*RATE
	y=np.zeros(r*d)
	for i in range(0,r*d):
		y[i]=np.sin(2*pi*f*i/float(r))
	return y
			
	
	
