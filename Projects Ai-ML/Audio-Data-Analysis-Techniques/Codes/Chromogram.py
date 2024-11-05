# importing necessary libraries
import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np

# Load the audio file
audio_file = 'TESS Toronto emotional speech set data/OAF_angry/OAF_back_angry.wav'
data, sr = librosa.load(audio_file)
chroma = librosa.feature.chroma_stft(y=data, sr=sr)

# Plot the chromagram
plt.figure(figsize=(10, 4))
librosa.display.specshow(chroma, y_axis='chroma', x_axis='time', sr=sr, cmap='coolwarm')
plt.colorbar()
plt.title('Chromogram')
plt.tight_layout()
plt.show()