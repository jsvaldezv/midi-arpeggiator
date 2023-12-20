from midiutil import MIDIFile
import utilities
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

print("-------------------")
print("Arpeggiator")


class Main(QMainWindow, QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500, 530)

        self.notas = []
        self.octavas = []
        self.notasEnMidi = []

        self.createComponents()

    def createComponents(self):
        # BPM
        self.bpmLabel = QLabel(self)
        self.bpmLabel.setText("BPM")
        self.bpmLabel.setGeometry(15, 10, 110, 30)

        self.bpm = QSpinBox(self)
        self.bpm.setGeometry(15, 35, 110, 30)
        self.bpm.setValue(85)
        self.bpm.setRange(60, 210)

        # Key
        self.keyLabel = QLabel(self)
        self.keyLabel.setText("Key")
        self.keyLabel.setGeometry(15, 70, 110, 30)

        self.keyCombo = QComboBox(self)
        self.keyCombo.setGeometry(10, 95, 110, 30)

        for key in utilities.keys:
            self.keyCombo.addItem(key)

        # Mode
        self.modoLabel = QLabel(self)
        self.modoLabel.setText("Mode")
        self.modoLabel.setGeometry(15, 125, 110, 30)

        self.modoCombo = QComboBox(self)
        self.modoCombo.setGeometry(10, 150, 110, 30)

        for modo in utilities.modos:
            self.modoCombo.addItem(modo)

        # Order
        self.orderLabel = QLabel(self)
        self.orderLabel.setText("Style")
        self.orderLabel.setGeometry(15, 180, 110, 30)

        self.orderCombo = QComboBox(self)
        self.orderCombo.setGeometry(10, 205, 110, 30)

        for order in utilities.orders:
            self.orderCombo.addItem(order)

        # Distance
        self.distanceLabel = QLabel(self)
        self.distanceLabel.setText("Distance")
        self.distanceLabel.setGeometry(15, 235, 110, 30)

        self.distanceCombo = QSpinBox(self)
        self.distanceCombo.setGeometry(15, 260, 110, 30)
        self.distanceCombo.setValue(2)
        self.distanceCombo.setRange(-12, 12)

        # Rate
        self.rateLabel = QLabel(self)
        self.rateLabel.setText("Rate")
        self.rateLabel.setGeometry(15, 290, 110, 30)

        self.rateCombo = QComboBox(self)
        self.rateCombo.setGeometry(10, 315, 110, 30)

        for duration in utilities.durations:
            self.rateCombo.addItem(duration)

        # Steps
        self.stepsLabel = QLabel(self)
        self.stepsLabel.setText("Steps")
        self.stepsLabel.setGeometry(15, 345, 110, 30)

        self.stepsCombo = QSpinBox(self)
        self.stepsCombo.setGeometry(15, 370, 110, 30)
        self.stepsCombo.setValue(2)
        self.stepsCombo.setRange(1, 20)

        # Notes number
        self.numNotasLabel = QLabel(self)
        self.numNotasLabel.setText("Notes number")
        self.numNotasLabel.setGeometry(15, 405, 110, 30)

        self.numNotasCombo = QSpinBox(self)
        self.numNotasCombo.setGeometry(15, 430, 110, 30)
        self.numNotasCombo.setValue(2)
        self.numNotasCombo.setRange(1, 20)

        # Bar number
        self.numCompasesLabel = QLabel(self)
        self.numCompasesLabel.setText("Bar number")
        self.numCompasesLabel.setGeometry(15, 465, 110, 30)

        self.numCompasesCombo = QSpinBox(self)
        self.numCompasesCombo.setGeometry(15, 490, 120, 30)
        self.numCompasesCombo.setValue(2)
        self.numCompasesCombo.setRange(1, 20)

        # Ready
        self.btnReady = QPushButton("Ready", self)
        self.btnReady.setGeometry(140, 10, 100, 45)
        self.btnReady.clicked.connect(lambda: self.inputNotes())

        self.userNotification = QLabel(self)
        self.userNotification.setText("Some notes are not part")
        self.userNotification.setGeometry(310, 50, 200, 30)
        self.userNotification.hide()
        self.userNotificationTwo = QLabel(self)
        self.userNotificationTwo.setText("of the scale")
        self.userNotificationTwo.setGeometry(310, 70, 200, 30)
        self.userNotificationTwo.hide()

    def clear(self):
        for object in self.notas:
            object.hide()
        for object in self.octavas:
            object.hide()

        self.notas.clear()
        self.octavas.clear()

    def inputNotes(self):
        self.userNotification.hide()
        self.userNotificationTwo.hide()

        self.clear()
        yInitChecBox = 130

        self.notasLabel = QLabel(self)
        self.notasLabel.setText("Root notes")
        self.notasLabel.setGeometry(150, 70, 140, 30)
        self.notasLabel.show()

        self.notaLabel = QLabel(self)
        self.notaLabel.setText("Note")
        self.notaLabel.setGeometry(150, 105, 50, 30)
        self.notaLabel.show()

        self.octavaLabel = QLabel(self)
        self.octavaLabel.setText("Octave")
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
            yInitChecBox += 30

        self.btnCreate = QPushButton("Create", self)
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

        # Calculate note numbers per compas
        tiempo = 0
        duration = utilities.getDurationFromNotation(self.rateCombo.currentText())

        # Note numbers per bar
        intervalTimes = 4 / duration

        # Get full midi scale
        # Get lowest root MIDI note (C-1)
        fundamentalMidi = utilities.getMidiFromNote(self.keyCombo.currentText() + "-1")

        # Create major or minor scale
        scale = utilities.createScaleArray(
            self.modoCombo.currentText(), fundamentalMidi
        )

        # Get sum for up or down
        distance *= utilities.getDistanciaSign(self.orderCombo.currentText())

        # Flag for midi file
        midiFileIsDone = False
        inicio = 0

        # Generate MIDI data
        for i in range(int(self.numNotasCombo.value())):
            nota = self.notasEnMidi[i]

            try:
                inicio = scale.index(nota)
                midiFileIsDone = True
            except:
                print("Some notes are not part of the scale")
                self.userNotification.show()
                self.userNotificationTwo.show()
                midiFileIsDone = False
                break

            index = inicio

            contNota = 0
            for j in range(int(intervalTimes) * int(self.numCompasesCombo.value())):
                utilities.addNote(
                    midiFile,
                    scale[index],
                    utilities.randomVelocity(1),
                    tiempo,
                    duration,
                )
                tiempo += duration
                index += distance
                contNota += 1

                if contNota >= (self.stepsCombo.value() + 1):
                    index = scale.index(nota)
                    contNota = 0

        if midiFileIsDone:
            with open("Midis/Arp.mid", "wb") as myOutputMIDIClip:
                midiFile.writeFile(myOutputMIDIClip)

            print("-------------------")
            print("MIDI file generated")
            print("-------------------")


app = QApplication(sys.argv)
demo = Main()
demo.show()
sys.exit(app.exec_())
