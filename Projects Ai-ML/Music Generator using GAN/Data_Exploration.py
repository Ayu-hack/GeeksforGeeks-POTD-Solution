#!/usr/bin/env python
# coding: utf-8

# ## Exploration of Data 

# In[1]:


import librosa
audio_file = r'H:\Deep Learning\Music Generator by Genre\GTZAN Data\genres_original\blues\blues.00000.wav'
signal, sr = librosa.load(audio_file, sr=46050)


# In[2]:


print(signal)


# ### Inspecting audio properties

# In[4]:


duration = librosa.get_duration(y=signal, sr=sr)
print(f"Duration: {duration:.2f} seconds")
if len(signal.shape) == 1:
    print("The audio is MONO.")
else:
    print("The audio is STEREO.")


# ### Visualizing the Audio Data

# In[8]:


import matplotlib.pyplot as plt
import librosa.display
import numpy as np


# In[6]:


plt.figure(figsize=(12, 4))
plt.plot(signal)
plt.title('Waveform')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.show()


# In[9]:


spectrogram = librosa.amplitude_to_db(librosa.stft(signal), ref=np.max)
librosa.display.specshow(spectrogram, sr=sr, x_axis='time', y_axis='log')
plt.colorbar(format='%+2.0f dB')
plt.title('Spectrogram')
plt.show()


# In[10]:


mel_spec = librosa.feature.melspectrogram(y=signal, sr=sr)
librosa.display.specshow(librosa.power_to_db(mel_spec, ref=np.max), sr=sr, x_axis='time', y_axis='mel')
plt.title('Mel-Spectrogram')
plt.show()


# ### Pitch of the Audio

# In[11]:


import librosa

def get_pitch_yin(audio_file):
    # Load audio file
    signal, sr = librosa.load(audio_file, sr=None)

    # Estimate pitch using YIN algorithm
    f0 = librosa.yin(signal, fmin=50, fmax=500)  # Adjust fmin, fmax based on audio

    # Remove NaN values and calculate average pitch
    f0 = f0[f0 > 0]  # Remove unvoiced frames (zeros)
    avg_pitch = f0.mean() if len(f0) > 0 else 0
    print(f"Estimated Pitch (YIN): {avg_pitch:.2f} Hz")


# In[12]:


get_pitch_yin(audio_file=audio_file)


# ### Extract features

# #### Time domain features

# In[13]:


zcr = librosa.feature.zero_crossing_rate(signal)
rms = librosa.feature.rms(y=signal)

print('Zero Crossing Rate: ',zcr)
print('Root Mean Square: ',rms)


# #### Frequency domain features

# In[19]:


centroid = librosa.feature.spectral_centroid(y=signal, sr=sr)
bandwidth = librosa.feature.spectral_bandwidth(y=signal, sr=sr)
mfccs = librosa.feature.mfcc(y=signal, sr=sr, n_mfcc=13)

print('Centroid: ',centroid)
print('Bandwidth: ',bandwidth)
print('MFCCs: ',mfccs)


# In[20]:


print("Mean of MFCCs:", np.mean(mfccs, axis=1))
print("Variance of Spectral Centroid:", np.var(centroid))


# ### Choosing Fixed Lengths

# In[7]:


import os
import librosa
import numpy as np

# Path to dataset
DATA_PATH = r'H:\Deep Learning\Music Generator by Genre\GTZAN Data\genres_original'

# Analyze audio file durations
durations = []

for genre in os.listdir(DATA_PATH):
    genre_path = os.path.join(DATA_PATH, genre)
    for file in os.listdir(genre_path):
        file_path = os.path.join(genre_path, file)
        
        # Use librosa for loading audio
        try:
            audio, sr = librosa.load(file_path, sr=None)
            duration = librosa.get_duration(y=audio, sr=sr)
            durations.append(duration)
        except Exception as e:
            print(f"Error loading {file_path}: {e}")

# Statistical analysis
print(f"Total audio files: {len(durations)}")
print(f"Max duration: {np.max(durations)} seconds")
print(f"Min duration: {np.min(durations)} seconds")
print(f"Mean duration: {np.mean(durations):.2f} seconds")
print(f"Median duration: {np.median(durations):.2f} seconds")


# In[8]:


# Common settings for spectrogram computation
sr = 46050  # Sampling rate
hop_length = 512  # Hop length used in spectrogram calculation

# Convert duration statistics to spectrogram frames
max_frames = int(np.max(durations) * sr / hop_length)
min_frames = int(np.min(durations) * sr / hop_length)
mean_frames = int(np.mean(durations) * sr / hop_length)
median_frames = int(np.median(durations) * sr / hop_length)

print(f"Max frames: {max_frames}")
print(f"Min frames: {min_frames}")
print(f"Mean frames: {mean_frames}")
print(f"Median frames: {median_frames}")


# In[9]:


import matplotlib.pyplot as plt

frame_lengths = [int(d * sr / hop_length) for d in durations]
plt.hist(frame_lengths, bins=30, color='blue', edgecolor='black')
plt.axvline(x=np.median(frame_lengths), color='red', linestyle='--', label='Median')
plt.axvline(x=np.mean(frame_lengths), color='green', linestyle='--', label='Mean')
plt.xlabel("Number of Frames")
plt.ylabel("Frequency")
plt.title("Distribution of Spectrogram Frame Lengths")
plt.legend()
plt.show()


# In[10]:


def process_audio(file_path, fixed_length=1300):
    audio, sr = librosa.load(file_path, sr=46050)
    spectrogram = librosa.feature.melspectrogram(y=audio, sr=sr, hop_length=512)

    # Ensure fixed length
    if spectrogram.shape[1] < fixed_length:
        # Pad if too short
        pad_width = fixed_length - spectrogram.shape[1]
        spectrogram = np.pad(spectrogram, ((0, 0), (0, pad_width)), mode='constant')
    else:
        # Truncate if too long
        spectrogram = spectrogram[:, :fixed_length]

    return spectrogram


# In[ ]:




