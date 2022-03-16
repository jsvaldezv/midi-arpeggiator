#################################################### IMPORTS ################################################
from midiutil import MIDIFile
import utilities

print("------------")
print("Arpeggiator")

#################################################### USER DATA ################################################
print("-------------------")
numNotas = int(input("Número de notas: "))
notas = []
for i in range(numNotas):
	nota = input("Nota "+ str(i+1) + " (en notación musical): ")
	notas.append(utilities.getMidiFromNote(nota))

print(notas)
print("------------")