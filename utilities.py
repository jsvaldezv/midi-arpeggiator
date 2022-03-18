#################################################### IMPORTS ################################################
import random

################################################## GENERAL DATA ################################################
## Note durations
durations = {	"whole note"     			:64,  
				"dotted white note"     	:48,   
				"white note"     			:32, 
				"dotted quarter note"		:24,   
				"quarter note"				:16, 
				"dotted eight note"     	:12,
				"eight note"     			:8,  
				"dotted sixteenth note" 	:6,    
				"sixteenth note" 			:4   
            }

## KEYS 
keys = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
notes = {}
midiNoteNumber = 0

majorScale = [2, 2, 1, 2, 2, 2, 1]
minorScale = [2, 1, 2, 2, 1, 2, 2]

# DICTIONARY WITH MIDI NOTES
for i in range(-1, 10):
    for note in keys:
        if midiNoteNumber <= 127:
            noteKey = "%s%s"%(note, i)
            notes[noteKey] = midiNoteNumber
        midiNoteNumber+=1

################################################## FUNCTIONS ################################################
def addNote(inMidiFile, inMidiNote, inVelocity, start_time, note_duration):
    inMidiFile.addNote(0, 0, inMidiNote, start_time, note_duration, inVelocity)

def randomVelocity(inTrigger):
    if int(inTrigger) == 0:
        return 0
    else:
        return (random.randint(60, 127))

def getMidiFromNote(inNote):
	return int(notes[inNote])

def split(word):
    return [char for char in word]

def getDurationFromNotation(inNotation):
	return durations[inNotation]/16

def getDistanciaSign(inMode):
	if inMode == "up":
		return 1
	else:
		return -1

def createScaleArray(inMode, inFundamentalMidi):
	if inMode == "mayor":
		scaleLocal = majorScale
	else:
		scaleLocal = minorScale
	
	cont = 0
	currentNote = inFundamentalMidi
	scale = []
	for i in range(inFundamentalMidi, 127): 
		if currentNote <= 127:
			currentNote += scaleLocal[cont]
			scale.append(currentNote)
			cont += 1
			if cont >= len(scaleLocal):
				cont = 0

	return scale