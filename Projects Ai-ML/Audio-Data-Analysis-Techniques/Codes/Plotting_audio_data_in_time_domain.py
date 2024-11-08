import numpy as np
import librosa, librosa.display
import matplotlib.pyplot as plt

FIG_SIZE = (15,10)

file = "TESS Toronto emotional speech set data/OAF_angry/OAF_back_angry.wav"

#Load audio file the wave
signal, sample_rate = librosa.load(file, sr=22050)

plt.figure(figsize=FIG_SIZE)
librosa.display.waveshow(signal, sr=sample_rate, alpha=0.4)
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.title("Waveform")
plt.show()