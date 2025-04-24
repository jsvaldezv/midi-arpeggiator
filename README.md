# Python MIDI Arpeggiator – Inspired by Ableton Live

<img width="500" alt="Screen Shot 2022-06-14 at 1 12 05 a m" src="https://user-images.githubusercontent.com/47612276/173505945-e2b38ee5-66c1-43cf-99b5-c4ba46c0cde9.png">

This project is a MIDI arpeggiator built with Python, inspired by the functionality of Ableton Live's arpeggiator. It allows users to input MIDI notes and automatically generates arpeggiated patterns.

🎹 Key Features:

- MIDI input handling and pattern generation
- Inspired by Ableton’s arpeggiator logic and behavior
- Customizable settings such as tempo, direction, and rate
- Built using Python and MIDI libraries for real-time MIDI control
- Ideal for music producers, live performers, and generative composition

This tool aims to provide a flexible and lightweight arpeggiator that can be integrated into DAW setups or used in live coding environments.

## Local running

### 1. Create venv
```bash
python3 -m venv venv
source venv/bin/activate
```

### 2. Install dependencies
```bash
(venv) pip install -r requirements.txt
```

### 3. Run main file
```bash
(venv) python main.py
```

## Recommendations

### 1. Run black to format your files with Python coding standards
```bash
(venv) black .
```
