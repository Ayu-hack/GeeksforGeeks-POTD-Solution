
import os
import numpy as np
import pandas as pd
import librosa
import glob
import matplotlib.pyplot as plt

data, sampling_rate = librosa.load('G:/Audio Data Analysis/TESS Toronto emotional speech set data/OAF_angry/OAF_back_angry.wav')

# Plot the waveform using the updated function
plt.figure(figsize=(9, 3))
librosa.display.waveshow(data, sr=sampling_rate)
plt.title('Waveform of the Audio File')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.show()


# Compute the Short-Time Fourier Transform (STFT)
stft = np.abs(librosa.stft(data))

# Convert the amplitude to decibels
db_stft = librosa.amplitude_to_db(stft, ref=np.max)

# Plot the spectrogram
plt.figure(figsize=(12, 6))
librosa.display.specshow(db_stft, sr=sampling_rate, x_axis='time', y_axis='log')
plt.colorbar(format='%+2.0f dB')
plt.title('Spectrogram of the Audio File')
plt.xlabel('Time (s)')
plt.ylabel('Frequency (Hz)')
plt.show()

# Statistical Analysis
mean = np.mean(data)
median = np.median(data)
variance = np.var(data)
print("\n")
print(f"Mean: {mean}\nMedian: {median}\nVariance: {variance}")
print("\n")