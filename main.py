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
tonalidad = input("Indica mayor o menor: ")
reversa = input('Elige up o down para el arpeggiador: ')
distance = int(input("Distance (en semitonos): ")) 
numNotas = int(input("Número de notas: "))

notas = []
for i in range(numNotas):
	nota = input("Nota "+ str(i+1) + " (en notación musical): ")
	notas.append(utilities.getMidiFromNote(nota))

#################################################### MIDI PROCESSING ##########################################
midiFile = MIDIFile(1)
midiFile.addTempo(0, 0, bpm)

# CALCULATE NOTES NUMBER PER COMPAS
tiempo = 0
duration = utilities.getDurationFromNotation(rate)
intervalTimes = 4/duration

# GET FULL MIDI SCALE
fundamentalMidi = utilities.getMidiFromNote(key + "-1")
scale = utilities.createScaleArray(tonalidad, fundamentalMidi)
# GET SUM FOR UP OR DOWN
distance *= utilities.getDistanciaSign(reversa)

# GENERATE MIDI DATA
for i in range(numNotas):
	nota = notas[i]
	inicio = scale.index(nota)
	index = inicio
	for j in range(int(intervalTimes)):
		utilities.addNote(midiFile, scale[index], utilities.randomVelocity(1), tiempo, duration)
		tiempo += duration
		index += distance

################################################# GENERATE MIDI ###############################################
with open("Arp.mid", "wb") as myOutputMIDIClip:
    midiFile.writeFile(myOutputMIDIClip)

print("-------------------")
print("Archivo MIDI generado")
print("-------------------")