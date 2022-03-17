#################################################### IMPORTS ##################################################
from midiutil import MIDIFile
import utilities

print("-------------------")
print("Arpeggiator")

#################################################### USER DATA ################################################
print("-------------------")
bpm = int(input("BPM: "))
key = input("Key: ")
rate = input("Rate: ")
distance = int(input("Distance (en semitonos): "))
numNotas = int(input("Número de notas: "))
notas = []
for i in range(numNotas):
	nota = input("Nota "+ str(i+1) + " (en notación musical): ")
	notas.append(utilities.getMidiFromNote(nota))

#################################################### MIDI PROCESSING ##########################################
midiFile = MIDIFile(1)
midiFile.addTempo(0, 0, bpm)

tiempo = 0
duration = utilities.getDurationFromNotation(rate)
intervalTimes = 4/duration

for i in range(numNotas):
	nota = notas[i]
	for j in range(int(intervalTimes)):
		utilities.addNote(midiFile, nota, 127, tiempo, duration)
		tiempo += duration
		nota += distance

################################################# GENERATE MIDI ###############################################
with open("Arp.mid", "wb") as myOutputMIDIClip:
    midiFile.writeFile(myOutputMIDIClip)

print("-------------------")
print("Archivo MIDI generado")
print("-------------------")