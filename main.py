#################################################### IMPORTS ################################################
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

#################################################### MIDI PROCESSING ################################################
midiFile = MIDIFile(1)
midiFile.addTempo(0, 0, bpm)

tiempo = 0
duration = utilities.getDurationFromNotation(rate)

for i in range(numNotas):
	utilities.addNote(midiFile, notas[i], 127, tiempo, duration)
	tiempo += duration	

################################################# GENERATE MIDI #################################################
with open("Arp.mid", "wb") as myOutputMIDIClip:
    midiFile.writeFile(myOutputMIDIClip)

print("-------------------")
print("Archivo MIDI generado")
print("-------------------")