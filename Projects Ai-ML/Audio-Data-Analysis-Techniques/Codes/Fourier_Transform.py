import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy.fft import fft, fftfreq

# Load the audio file (replace 'your_audio_file.wav' with the path to your file)
sample_rate, audio_data = wavfile.read('TESS Toronto emotional speech set data/OAF_angry/OAF_back_angry.wav')

# If the audio is stereo, take only one channel
if len(audio_data.shape) > 1:
    audio_data = audio_data[:, 0]

# Calculate the Fourier Transform
N = len(audio_data)  # Number of samples
yf = fft(audio_data)  # Perform the FFT
xf = fftfreq(N, 1 / sample_rate)  # Generate frequency bins

# Only take the positive frequencies and magnitudes (real parts)
xf = xf[:N // 2]
yf = np.abs(yf[:N // 2])

# Plot the frequency spectrum
plt.figure(figsize=(10, 6))
plt.plot(xf, yf)
plt.title("Frequency Spectrum of the Audio File")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.show()
