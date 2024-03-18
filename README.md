# Advanced Non-Diatonic Ear Training Exercises

In my experience, most ear training exercises on the Internet focus on diatonic melodies and harmonies. The ear training
exercises in this project are not biased towards diatonicism.

The src folder contains three Python scripts that run three distinct ear training exercises in the terminal. The scripts 
use the *mingus* Python module and the *FluidSynth* library. There is a file path in these scripts that must point to a valid soundfont file
on the computer in order for everything to work.

## Exercises

* The **pitch_training.py** exercise tests recognition of individual pitches.
* The **melody_training.py** exercise tests dictation of "melodies," i.e., randomly generated sequences of notes.
* The **harmony_training.py** exercise tests dictation of "chords," i.e., a randomly selected collection of notes all played at the same time.