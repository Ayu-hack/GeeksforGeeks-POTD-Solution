import librosa
import librosa.display
import numpy as np
import matplotlib.pyplot as plt

# Load an audio file
audio_path = 'TESS Toronto emotional speech set data/OAF_angry/OAF_back_angry.wav'  # Replace with the path to your audio file
y, sr = librosa.load(audio_path)

# Extract MFCCs
mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=20)

# Print the shape of the MFCCs
print("MFCCs shape:", mfccs.shape)

# Plot the MFCCs
plt.figure(figsize=(10, 6))
librosa.display.specshow(mfccs, x_axis='time')
plt.colorbar()
plt.title('Mel-Frequency Cepstral Coefficients')
plt.tight_layout()
plt.show()
