#################################################### IMPORTS ##################################################
from midiutil import MIDIFile
import utilities
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from visual_midi import Plotter
from pretty_midi import PrettyMIDI

print("-------------------")
print("Arpeggiator")

class Main(QMainWindow, QWidget):

	def __init__(self):
		super().__init__()
		self.resize(500, 530)

		# VARIABLES GLOBALES #
		self.notas = []
		self.octavas = []
		self.notasEnMidi = []

		self.createComponents()

	def createComponents(self):
		# BPM #
		self.bpmLabel = QLabel(self)
		self.bpmLabel.setText("BPM")
		self.bpmLabel.setGeometry(15, 10, 110, 30)

		self.bpm = QSpinBox(self)
		self.bpm.setGeometry(15, 35, 110, 30)
		self.bpm.setValue(85)
		self.bpm.setRange(60, 210)

		# KEY #
		self.keyLabel = QLabel(self)
		self.keyLabel.setText("Key")
		self.keyLabel.setGeometry(15, 70, 110, 30)
		
		self.keyCombo = QComboBox(self)
		self.keyCombo.setGeometry(10, 95, 110, 30)

		for key in utilities.keys: 
			self.keyCombo.addItem(key)

		# MODO #
		self.modoLabel = QLabel(self)
		self.modoLabel.setText("Modo")
		self.modoLabel.setGeometry(15, 125, 110, 30)
		
		self.modoCombo = QComboBox(self)
		self.modoCombo.setGeometry(10, 150, 110, 30)

		for modo in utilities.modos: 
			self.modoCombo.addItem(modo)

		# ORDER #
		self.orderLabel = QLabel(self)
		self.orderLabel.setText("Style")
		self.orderLabel.setGeometry(15, 180, 110, 30)
		
		self.orderCombo = QComboBox(self)
		self.orderCombo.setGeometry(10, 205, 110, 30)

		for order in utilities.orders: 
			self.orderCombo.addItem(order)

		# DISTANCE #
		self.distanceLabel = QLabel(self)
		self.distanceLabel.setText("Distancia")
		self.distanceLabel.setGeometry(15, 235, 110, 30)
		
		self.distanceCombo = QSpinBox(self)
		self.distanceCombo.setGeometry(15, 260, 110, 30)
		self.distanceCombo.setValue(2)
		self.distanceCombo.setRange(-12, 12)

		# RATE #
		self.rateLabel = QLabel(self)
		self.rateLabel.setText("Rate")
		self.rateLabel.setGeometry(15, 290, 110, 30)
		
		self.rateCombo = QComboBox(self)
		self.rateCombo.setGeometry(10, 315, 110, 30)

		for duration in utilities.durations:
			self.rateCombo.addItem(duration)

		# STEPS #
		self.stepsLabel = QLabel(self)
		self.stepsLabel.setText("Steps")
		self.stepsLabel.setGeometry(15, 345, 110, 30)
		
		self.stepsCombo = QSpinBox(self)
		self.stepsCombo.setGeometry(15, 370, 110, 30)
		self.stepsCombo.setValue(2)
		self.stepsCombo.setRange(1, 20)

		# NUM DE NOTAS #
		self.numNotasLabel = QLabel(self)
		self.numNotasLabel.setText("Num de notas")
		self.numNotasLabel.setGeometry(15, 405, 110, 30)
		
		self.numNotasCombo = QSpinBox(self)
		self.numNotasCombo.setGeometry(15, 430, 110, 30)
		self.numNotasCombo.setValue(2)
		self.numNotasCombo.setRange(1, 20)

		# NUM DE COMPASES #
		self.numCompasesLabel = QLabel(self)
		self.numCompasesLabel.setText("Num de compases")
		self.numCompasesLabel.setGeometry(15, 465, 110, 30)
		
		self.numCompasesCombo = QSpinBox(self)
		self.numCompasesCombo.setGeometry(15, 490, 120, 30)
		self.numCompasesCombo.setValue(2)
		self.numCompasesCombo.setRange(1, 20)

		# READY #
		self.btnReady = QPushButton('Ready', self)
		self.btnReady.setGeometry(140, 10, 100, 45)
		self.btnReady.clicked.connect(lambda: self.inputNotes())

	def clear(self):
		for object in self.notas:
			object.hide()
		for object in self.octavas:
			object.hide()

		self.notas.clear()
		self.octavas.clear()

	def inputNotes(self):
		self.clear()
		yInitChecBox = 130

		self.notasLabel = QLabel(self)
		self.notasLabel.setText("Notas fundamentales")
		self.notasLabel.setGeometry(150, 70, 140, 30)
		self.notasLabel.show()

		self.notaLabel = QLabel(self)
		self.notaLabel.setText("Nota")
		self.notaLabel.setGeometry(150, 105, 50, 30)
		self.notaLabel.show()

		self.octavaLabel = QLabel(self)
		self.octavaLabel.setText("Octava")
		self.octavaLabel.setGeometry(225, 105, 100, 30)
		self.octavaLabel.show()

		for note in range(self.numNotasCombo.value()):
			globals()[f"key_{note}"] = QComboBox(self)
			globals()[f"key_{note}"].setGeometry(140, yInitChecBox, 70, 30)

			for key in utilities.keys: 
				globals()[f"key_{note}"].addItem(key)

			globals()[f"key_{note}"].show()
			
			globals()[f"octave_{note}"] = QSpinBox(self)
			globals()[f"octave_{note}"].setGeometry(225, yInitChecBox, 60, 30)
			globals()[f"octave_{note}"].setValue(4)
			globals()[f"octave_{note}"].setRange(-1, 8)
			globals()[f"octave_{note}"].show()
			
			self.notas.append(globals()[f"key_{note}"])
			self.octavas.append(globals()[f"octave_{note}"])
			yInitChecBox+=30
		
		# READY #
		self.btnCreate = QPushButton('Create', self)
		self.btnCreate.setGeometry(300, 10, 100, 45)
		self.btnCreate.clicked.connect(lambda: self.midiProcessing())
		self.btnCreate.show()

	def getMidiNotesFromGUI(self):
		for i in range(len(self.notas)):
			stringNota = str(self.notas[i].currentText()) + str(self.octavas[i].value())
			self.notasEnMidi.append(utilities.getMidiFromNote(stringNota))

	def midiProcessing(self):
		self.getMidiNotesFromGUI()
		distance = self.distanceCombo.value()

		midiFile = MIDIFile(1)
		midiFile.addTempo(0, 0, self.bpm.value())

		# CALCULATE NOTES NUMBER PER COMPAS
		tiempo = 0
		duration = utilities.getDurationFromNotation(self.rateCombo.currentText())
		intervalTimes = 4/duration

		# GET FULL MIDI SCALE
		fundamentalMidi = utilities.getMidiFromNote(self.keyCombo.currentText() + "-1")
		scale = utilities.createScaleArray(self.modoCombo.currentText(), fundamentalMidi)
		# GET SUM FOR UP OR DOWN
		distance *= utilities.getDistanciaSign(self.orderCombo.currentText())

		# GENERATE MIDI DATA
		for i in range(int(self.numNotasCombo.value())):
			nota = self.notasEnMidi[i]
			inicio = scale.index(nota)
			index = inicio

			contNota = 0
			for j in range(int(intervalTimes) * int(self.numCompasesCombo.value())):
				utilities.addNote(midiFile, scale[index], utilities.randomVelocity(1), tiempo, duration)
				tiempo += duration
				index += distance
				contNota += 1

				if contNota >= (self.stepsCombo.value()+1):
					index = scale.index(nota)
					contNota = 0

			#for j in range(int(self.stepsCombo.value())+1):
				#utilities.addNote(midiFile, scale[index], utilities.randomVelocity(1), tiempo, duration)
				#tiempo += duration
				#index += distance

		with open("MidiArpeggiator/Midis/Arp.mid", "wb") as myOutputMIDIClip:
			midiFile.writeFile(myOutputMIDIClip)

		print("-------------------")
		print("Archivo MIDI generado")
		print("-------------------")

		pm = PrettyMIDI("MidiArpeggiator/Midis/Arp.mid")
		plotter = Plotter()
		plotter.show(pm, "/tmp/example-01.html")

app = QApplication(sys.argv)
demo = Main()
demo.show()
sys.exit(app.exec_())

#################################################### USER DATA ################################################
'''print("-------------------")
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
	notas.append(utilities.getMidiFromNote(nota))'''

#################################################### MIDI PROCESSING ##########################################
'''midiFile = MIDIFile(1)
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
print("-------------------")'''