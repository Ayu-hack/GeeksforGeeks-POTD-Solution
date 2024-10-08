# -*- coding: utf-8 -*-
"""Eye Disease Classified RNN

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/#fileId=https%3A//storage.googleapis.com/kaggle-colab-exported-notebooks/eye-disease-classified-rnn-1dad937b-096c-47d8-be51-c6b9a6311c0c.ipynb%3FX-Goog-Algorithm%3DGOOG4-RSA-SHA256%26X-Goog-Credential%3Dgcp-kaggle-com%2540kaggle-161607.iam.gserviceaccount.com/20241007/auto/storage/goog4_request%26X-Goog-Date%3D20241007T192845Z%26X-Goog-Expires%3D259200%26X-Goog-SignedHeaders%3Dhost%26X-Goog-Signature%3D6b7e89c8377d616053435bfd68a29c4b1028871f96409598b7e9048d45ef7b1ef513cb6cd66027348c80cb046cbfbee12accff1e279720a8cb4958c3dcdb89fc1b6ae2e0377daa302d29c333d6daf9a48f58981e389d9bba9cca6ef9f95386d362875f90e9028f575db6dfbaabef369aab2b6a58593f26732d6453f714e7acdf323267b234fef0df89678fe2bc72e473210fc3e3ea231a249bf1932b502a1e16aecb4b4411358596f89b27e5975deac2c861730d22388e1f2228bbe9247e40d2d9b575b10681afe150289ca4111abe541e5bc3dada8689905fe2a624dd9bce7b89ad33cbfb54e40cd6c772a6677432e4e4ab55c8d34f0f5523d31383a5fb7a10
"""

import os
import sys
from tempfile import NamedTemporaryFile
from urllib.request import urlopen
from urllib.parse import unquote, urlparse
from urllib.error import HTTPError
from zipfile import ZipFile
import tarfile
import shutil

CHUNK_SIZE = 40960
DATA_SOURCE_MAPPING = 'eye-diseases-classification:https%3A%2F%2Fstorage.googleapis.com%2Fkaggle-data-sets%2F2440665%2F4130910%2Fbundle%2Farchive.zip%3FX-Goog-Algorithm%3DGOOG4-RSA-SHA256%26X-Goog-Credential%3Dgcp-kaggle-com%2540kaggle-161607.iam.gserviceaccount.com%252F20241007%252Fauto%252Fstorage%252Fgoog4_request%26X-Goog-Date%3D20241007T192845Z%26X-Goog-Expires%3D259200%26X-Goog-SignedHeaders%3Dhost%26X-Goog-Signature%3D54062b04a469efcd2e37a21f247c85201dc03d81917e0500102d7ba0c181dfdbb3fdfc92b86f562865990d234923cdd88f9a2f289fe8447b160ce741b050f4bbe25e897cdc396012f177c27073f4eb53ef8010e8a13470bcc97d272749d56b56cebe152f2966c2db1c74710c21001da5a00fbd2e543617b89dd441c1bbec3a1f3ec27835cb0577e0e7e29ce4e98209e7098259912c4ed30b79e6c275a99806db8bed2baa4bd39a0774c10191223fdddc111ae66f38f5ce8f5c9c88b6c3283c3054cc75a2a7de66e05171b1b47775cc37e233b639c3a38ca4a7dc23d699d0b364b9a99b3627f871dc698cf66557bc1276989acad63f5ae6c03db9e38eca5477c1'

KAGGLE_INPUT_PATH='/kaggle/input'
KAGGLE_WORKING_PATH='/kaggle/working'
KAGGLE_SYMLINK='kaggle'

!umount /kaggle/input/ 2> /dev/null
shutil.rmtree('/kaggle/input', ignore_errors=True)
os.makedirs(KAGGLE_INPUT_PATH, 0o777, exist_ok=True)
os.makedirs(KAGGLE_WORKING_PATH, 0o777, exist_ok=True)

try:
  os.symlink(KAGGLE_INPUT_PATH, os.path.join("..", 'input'), target_is_directory=True)
except FileExistsError:
  pass
try:
  os.symlink(KAGGLE_WORKING_PATH, os.path.join("..", 'working'), target_is_directory=True)
except FileExistsError:
  pass

for data_source_mapping in DATA_SOURCE_MAPPING.split(','):
    directory, download_url_encoded = data_source_mapping.split(':')
    download_url = unquote(download_url_encoded)
    filename = urlparse(download_url).path
    destination_path = os.path.join(KAGGLE_INPUT_PATH, directory)
    try:
        with urlopen(download_url) as fileres, NamedTemporaryFile() as tfile:
            total_length = fileres.headers['content-length']
            print(f'Downloading {directory}, {total_length} bytes compressed')
            dl = 0
            data = fileres.read(CHUNK_SIZE)
            while len(data) > 0:
                dl += len(data)
                tfile.write(data)
                done = int(50 * dl / int(total_length))
                sys.stdout.write(f"\r[{'=' * done}{' ' * (50-done)}] {dl} bytes downloaded")
                sys.stdout.flush()
                data = fileres.read(CHUNK_SIZE)
            if filename.endswith('.zip'):
              with ZipFile(tfile) as zfile:
                zfile.extractall(destination_path)
            else:
              with tarfile.open(tfile.name) as tarfile:
                tarfile.extractall(destination_path)
            print(f'\nDownloaded and uncompressed: {directory}')
    except HTTPError as e:
        print(f'Failed to load (likely expired) {download_url} to path {destination_path}')
        continue
    except OSError as e:
        print(f'Failed to load {download_url} to path {destination_path}')
        continue

print('Data source import complete.')
 # Due to some issue I am unable to add ipynb file

"""<a id="1"></a>
<div id="animated-container" style="position: relative;
            border-radius: 10px;
            padding: 10px;
            font-family: Arial, sans-serif;
            font-size: 36px;
            font-weight: 900;
            color: black;
            display: inline-block;
            text-transform: uppercase;
            box-shadow: 2px 2px 4px #888;
            text-shadow: 2px 2px 4px #888;
            overflow: hidden;
            background-color: #800606 ;
            cursor: pointer;" onclick="toggleAnimation()"> <!-- Added cursor pointer and onclick event -->
    <div style="position: absolute;
                top: 50%;
                right: 0; /* Adjusted to place on the right side */
                transform: translateY(45%);">
        <!-- <img src="https://www.kaggle.com/static/images/tier-animation-transparent.gif" alt="Cartoon Character" style="height: 100px; width: auto;"> -->
    </div>
    <div style="font-weight: bold;"></div>
    <span style="font-style: italic; text-shadow: 2px 2px 4px #888; color: white;">Eye Disease 🦠(RNN)</span>
         <!-- <img src="https://pin.it/6mmgqwOvV" alt="Cartoon Character" style="height: 50px; width: auto;"> -->
</div>

<script>
    function toggleAnimation() {
        var container = document.getElementById('animated-container');
        var animationDiv = container.querySelector('div');
        if (animationDiv.style.animationPlayState === 'paused') {
            animationDiv.style.animationPlayState = 'running';
        } else {
            animationDiv.style.animationPlayState = 'paused';
        }
    }
</script>

<img src="https://www.mississippivision.com/wp-content/uploads/diabetic-retinopathy-1-2048x902.jpeg" style="width:100%">

<a id="1"></a>
<div id="animated-container" style="position: relative;
            border-radius: 10px;
            padding: 10px;
            font-family: Arial, sans-serif;
            font-size: 36px;
            font-weight: 900;
            color: black;
            display: inline-block;
            text-transform: uppercase;
            box-shadow: 2px 2px 4px #888;
            text-shadow: 2px 2px 4px #888;
            overflow: hidden;
            background-color: #800606 ;
            cursor: pointer;" onclick="toggleAnimation()"> <!-- Added cursor pointer and onclick event -->
    <div style="position: absolute;
                top: 50%;
                right: 0; /* Adjusted to place on the right side */
                transform: translateY(45%);">
        <!-- <img src="https://www.kaggle.com/static/images/tier-animation-transparent.gif" alt="Cartoon Character" style="height: 100px; width: auto;"> -->
    </div>
    <div style="font-weight: bold;"></div>
    <span style="font-style: italic; text-shadow: 2px 2px 4px #888; color: white;">About author 👨‍💻 </span>
         <!-- <img src="https://pin.it/6mmgqwOvV" alt="Cartoon Character" style="height: 50px; width: auto;"> -->
</div>

<script>
    function toggleAnimation() {
        var container = document.getElementById('animated-container');
        var animationDiv = container.querySelector('div');
        if (animationDiv.style.animationPlayState === 'paused') {
            animationDiv.style.animationPlayState = 'running';
        } else {
            animationDiv.style.animationPlayState = 'paused';
        }
    }
</script>

<a id="1"></a>
<div id="animated-container" style="position: relative;
            border-radius: 10px;
            padding: 10px;
            font-family: Arial, sans-serif;
            font-size: 36px;
            font-weight: 900;
            color: black;
            display: inline-block;
            text-transform: uppercase;
            box-shadow: 2px 2px 4px #888;
            text-shadow: 2px 2px 4px #888;
            overflow: hidden;
            background-color: #800606 ;
            cursor: pointer;" onclick="toggleAnimation()"> <!-- Added cursor pointer and onclick event -->
    <div style="position: absolute;
                top: 50%;
                right: 0; /* Adjusted to place on the right side */
                transform: translateY(45%);">
        <!-- <img src="https://www.kaggle.com/static/images/tier-animation-transparent.gif" alt="Cartoon Character" style="height: 100px; width: auto;"> -->
    </div>
    <div style="font-weight: bold;"></div>
    <span style="font-style: italic; text-shadow: 2px 2px 4px #888; color: white;">About dataset 📊</span>
         <!-- <img src="https://pin.it/6mmgqwOvV" alt="Cartoon Character" style="height: 50px; width: auto;"> -->
</div>

<script>
    function toggleAnimation() {
        var container = document.getElementById('animated-container');
        var animationDiv = container.querySelector('div');
        if (animationDiv.style.animationPlayState === 'paused') {
            animationDiv.style.animationPlayState = 'running';
        } else {
            animationDiv.style.animationPlayState = 'paused';
        }
    }
</script>

# **Summary**
**Our eyes are one of the most important senses that help us to make contact with each other and allow us to see the beauty and abomination around us. Eyes are susceptible to diseases. Eye diseases include **Glaucoma**, **Diabetic retinopathy**, and **Cataracts**.**Early diagnosis and treatment of eye diseases can preserve eyesight.**

# **Eye Diseases**
- **Glaucoma: Group of eye diseases that can damage the optic nerve. The optic nerve is responsible for transmitting visual information from the eye to the brain. Glaucoma can lead to permanent vision loss and, in some cases, blindness.**

- **Diabetic retinopathy: It's an eye condition that affects people with diabetes. High blood sugar leaves damaged vessels in the retina. The retina is that part of your eyes that can detect light and send signals to the brain. Damage to these blood vessels can lead to vision loss and blindness in some cases.**

- **Cataracts: Cataracts cloud the natural eye lens, leading to blurry vision and difficulty seeing clearly. Aging is one of the main reasons for this disease, but it can also be caused by factors such as injury, genetics, or medication effects. Cataracts can make natural vision blurry, cloudy, and even double it.**

**By better understanding these eye diseases, their causes, and their effects on vision, we can develop insights to aid their early detection and effective management. This notebook tries to classify these diseases from pictures.**

<a id="1"></a>
<div id="animated-container" style="position: relative;
            border-radius: 10px;
            padding: 10px;
            font-family: Arial, sans-serif;
            font-size: 36px;
            font-weight: 900;
            color: black;
            display: inline-block;
            text-transform: uppercase;
            box-shadow: 2px 2px 4px #888;
            text-shadow: 2px 2px 4px #888;
            overflow: hidden;
            background-color: #800606 ;
            cursor: pointer;" onclick="toggleAnimation()"> <!-- Added cursor pointer and onclick event -->
    <div style="position: absolute;
                top: 50%;
                right: 0; /* Adjusted to place on the right side */
                transform: translateY(45%);">
        <!-- <img src="https://www.kaggle.com/static/images/tier-animation-transparent.gif" alt="Cartoon Character" style="height: 100px; width: auto;"> -->
    </div>
    <div style="font-weight: bold;"></div>
    <span style="font-style: italic; text-shadow: 2px 2px 4px #888; color: white;">about model(RNN) 🚀</span>
         <!-- <img src="https://pin.it/6mmgqwOvV" alt="Cartoon Character" style="height: 50px; width: auto;"> -->
</div>

<script>
    function toggleAnimation() {
        var container = document.getElementById('animated-container');
        var animationDiv = container.querySelector('div');
        if (animationDiv.style.animationPlayState === 'paused') {
            animationDiv.style.animationPlayState = 'running';
        } else {
            animationDiv.style.animationPlayState = 'paused';
        }
    }
</script>

# **Recurrent Neural Networks (RNNs) 🔄🧠**

**RNNs are a type of deep learning architecture widely used for processing sequential data. They excel at capturing temporal dependencies and have applications in various domains. 📚🔍**

## **How RNNs Work 🔄**

**RNNs mimic the human brain's ability to process and understand sequential information. They introduce recurrent connections within the network, allowing information to persist and be passed from one step to another within the sequence. 🕒🔁**

**RNNs process sequential data step by step, considering the context of previous steps while analyzing the current step. At each step, the network takes an input and combines it with the hidden state from the previous step to generate an output and update the hidden state for the next step. 🚶‍♂️🔄**

## **Capturing Dependencies and Long-term Context 🧠🔗**

**RNNs are particularly effective at capturing temporal dependencies in sequences. They can model and understand the relationships between elements that appear at different positions within the sequence. This ability enables them to capture long-term dependencies, making them valuable for tasks involving sequential data. 📈🔍**

**However, RNNs can face challenges in maintaining and propagating information over long sequences due to the vanishing gradient problem. To address this limitation, variants of RNNs such as Long Short-Term Memory (LSTM) and Gated Recurrent Unit (GRU) have been developed. These variants introduce gating mechanisms that help the network selectively update and retain information, mitigating the vanishing gradient problem. 📉🔒**

## **Applications of RNNs 🌐📊**

**RNNs find applications in several domains, including:**

- **Natural Language Processing (NLP): RNNs can process and generate human language, making them useful for tasks like language modeling, sentiment analysis, and machine translation. 🗣️✍️🌐**
- **Speech Recognition: RNNs are employed in speech recognition systems to convert spoken language into written text. 🎙️📝**
- **Time Series Analysis: RNNs can analyze and predict patterns in time-dependent data, making them valuable for tasks such as stock market forecasting or weather prediction. ⏰📈🌦️**

<a id="1"></a>
<div id="animated-container" style="position: relative;
            border-radius: 10px;
            padding: 10px;
            font-family: Arial, sans-serif;
            font-size: 36px;
            font-weight: 900;
            color: black;
            display: inline-block;
            text-transform: uppercase;
            box-shadow: 2px 2px 4px #888;
            text-shadow: 2px 2px 4px #888;
            overflow: hidden;
            background-color: #800606 ;
            cursor: pointer;" onclick="toggleAnimation()"> <!-- Added cursor pointer and onclick event -->
    <div style="position: absolute;
                top: 50%;
                right: 0; /* Adjusted to place on the right side */
                transform: translateY(45%);">
        <!-- <img src="https://www.kaggle.com/static/images/tier-animation-transparent.gif" alt="Cartoon Character" style="height: 100px; width: auto;"> -->
    </div>
    <div style="font-weight: bold;"></div>
    <span style="font-style: italic; text-shadow: 2px 2px 4px #888; color: white;">Libraries 📚</span>
         <!-- <img src="https://pin.it/6mmgqwOvV" alt="Cartoon Character" style="height: 50px; width: auto;"> -->
</div>

<script>
    function toggleAnimation() {
        var container = document.getElementById('animated-container');
        var animationDiv = container.querySelector('div');
        if (animationDiv.style.animationPlayState === 'paused') {
            animationDiv.style.animationPlayState = 'running';
        } else {
            animationDiv.style.animationPlayState = 'paused';
        }
    }
</script>
"""

import os
import cv2
import random
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import tensorflow as tf
from PIL import Image
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential
from tensorflow.keras.preprocessing.image import ImageDataGenerator # Corrected import statement
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from tensorflow.keras.callbacks import TensorBoard
from sklearn.metrics import classification_report
import warnings
warnings.filterwarnings('ignore')

"""<a id="1"></a>
<div id="animated-container" style="position: relative;
            border-radius: 10px;
            padding: 10px;
            font-family: Arial, sans-serif;
            font-size: 36px;
            font-weight: 900;
            color: black;
            display: inline-block;
            text-transform: uppercase;
            box-shadow: 2px 2px 4px #888;
            text-shadow: 2px 2px 4px #888;
            overflow: hidden;
            background-color: #800606 ;
            cursor: pointer;" onclick="toggleAnimation()"> <!-- Added cursor pointer and onclick event -->
    <div style="position: absolute;
                top: 50%;
                right: 0; /* Adjusted to place on the right side */
                transform: translateY(45%);">
        <!-- <img src="https://www.kaggle.com/static/images/tier-animation-transparent.gif" alt="Cartoon Character" style="height: 100px; width: auto;"> -->
    </div>
    <div style="font-weight: bold;"></div>
    <span style="font-style: italic; text-shadow: 2px 2px 4px #888; color: white;">Preprocessing 🛠️</span>
         <!-- <img src="https://pin.it/6mmgqwOvV" alt="Cartoon Character" style="height: 50px; width: auto;"> -->
</div>

<script>
    function toggleAnimation() {
        var container = document.getElementById('animated-container');
        var animationDiv = container.querySelector('div');
        if (animationDiv.style.animationPlayState === 'paused') {
            animationDiv.style.animationPlayState = 'running';
        } else {
            animationDiv.style.animationPlayState = 'paused';
        }
    }
</script>

"""

# Define rescaling layer
rescale = tf.keras.layers.Rescaling(1./255)

# Load train dataset
train_ds = tf.keras.utils.image_dataset_from_directory(
    directory='/kaggle/input/eye-diseases-classification/dataset',
    batch_size=32,
    image_size=(256, 256),
    validation_split=0.2,
    subset="training",
    seed=123,
    label_mode='categorical',  # Assuming you have multiple classes
)

# Preprocess train dataset (rescale)
train_ds = train_ds.map(lambda x, y: (rescale(x), y))

# Load validation dataset
validation_ds = tf.keras.utils.image_dataset_from_directory(
    directory='/kaggle/input/eye-diseases-classification/dataset',
    batch_size=32,
    image_size=(256, 256),
    validation_split=0.2,
    subset="validation",
    seed=123,
    label_mode='categorical',  # Assuming you have multiple classes
)

# Preprocess validation dataset (rescale)
validation_ds = validation_ds.map(lambda x, y: (rescale(x), y))

# Load test dataset
test_ds = tf.keras.utils.image_dataset_from_directory(
    directory='/kaggle/input/eye-diseases-classification/dataset',  # Specify the directory for the test dataset
    batch_size=32,
    image_size=(256, 256),
    label_mode='categorical',  # Assuming you have multiple classes
    shuffle=False,
)

# Preprocess test dataset (rescale)
test_ds = test_ds.map(lambda x, y: (rescale(x), y))

"""## **Check Shape After Preprocessing**"""

# Check the first image shape in the training dataset
print("Shape of the first image in the training dataset:", next(iter(train_ds))[0][0].shape)
# Check the first image shape in the validation dataset
print("Shape of the first image in the validation dataset:", next(iter(validation_ds))[0][0].shape)
# Check the first image shape in the test dataset
print("Shape of the first image in the test dataset:", next(iter(test_ds))[0][0].shape)

"""## **Check Pixel Value After Preprocessing**"""

# Initialize variables to store minimum and maximum pixel values
min_pixel_value = float('inf')
max_pixel_value = float('-inf')

# Iterate through the dataset
for images, _ in train_ds:
    # Compute the minimum and maximum pixel values in the current batch of images
    batch_min = tf.reduce_min(images)
    batch_max = tf.reduce_max(images)

    # Update overall minimum and maximum pixel values
    min_pixel_value = tf.minimum(min_pixel_value, batch_min)
    max_pixel_value = tf.maximum(max_pixel_value, batch_max)

# Print the minimum and maximum pixel values
print("Minimum pixel value:", min_pixel_value.numpy())
print("Maximum pixel value:", max_pixel_value.numpy())

"""<a id="1"></a>
<div id="animated-container" style="position: relative;
            border-radius: 10px;
            padding: 10px;
            font-family: Arial, sans-serif;
            font-size: 36px;
            font-weight: 900;
            color: black;
            display: inline-block;
            text-transform: uppercase;
            box-shadow: 2px 2px 4px #888;
            text-shadow: 2px 2px 4px #888;
            overflow: hidden;
            background-color: #800606 ;
            cursor: pointer;" onclick="toggleAnimation()"> <!-- Added cursor pointer and onclick event -->
    <div style="position: absolute;
                top: 50%;
                right: 0; /* Adjusted to place on the right side */
                transform: translateY(45%);">
        <!-- <img src="https://www.kaggle.com/static/images/tier-animation-transparent.gif" alt="Cartoon Character" style="height: 100px; width: auto;"> -->
    </div>
    <div style="font-weight: bold;"></div>
    <span style="font-style: italic; text-shadow: 2px 2px 4px #888; color: white;">Visualization 🕵</span>
         <!-- <img src="https://pin.it/6mmgqwOvV" alt="Cartoon Character" style="height: 50px; width: auto;"> -->
</div>

<script>
    function toggleAnimation() {
        var container = document.getElementById('animated-container');
        var animationDiv = container.querySelector('div');
        if (animationDiv.style.animationPlayState === 'paused') {
            animationDiv.style.animationPlayState = 'running';
        } else {
            animationDiv.style.animationPlayState = 'paused';
        }
    }
</script>

"""

def visualize_images(path, target_size=(256, 256), num_images=5):

    # Get a list of image filenames
    image_filenames = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]

    if not image_filenames:
        raise ValueError("No images found in the specified path")

    # Select random images
    selected_images = random.sample(image_filenames, min(num_images, len(image_filenames)))

    # Create a figure and axes
    fig, axes = plt.subplots(1, num_images, figsize=(15, 3), facecolor='white')

    # Display each image
    for i, image_filename in enumerate(selected_images):
        # Load image and resize
        image_path = os.path.join(path, image_filename)
        image = Image.open(image_path)
        image = image.resize(target_size)

        # Display image
        axes[i].imshow(image)
        axes[i].axis('off')
        axes[i].set_title(image_filename)  # Set image filename as title

    # Adjust layout and display
    plt.tight_layout()
    plt.show()

# Unable to make changes directly so added py file

"""<a id="1"></a>
<div id="animated-container" style="position: relative;
            border-radius: 10px;
            padding: 10px;
            font-family: Arial, sans-serif;
            font-size: 36px;
            font-weight: 900;
            color: black;
            display: inline-block;
            text-transform: uppercase;
            box-shadow: 2px 2px 4px #888;
            text-shadow: 2px 2px 4px #888;
            overflow: hidden;
            background-color: #800606 ;
            cursor: pointer;" onclick="toggleAnimation()"> <!-- Added cursor pointer and onclick event -->
    <div style="position: absolute;
                top: 50%;
                right: 0; /* Adjusted to place on the right side */
                transform: translateY(45%);">
        <!-- <img src="https://www.kaggle.com/static/images/tier-animation-transparent.gif" alt="Cartoon Character" style="height: 100px; width: auto;"> -->
    </div>
    <div style="font-weight: bold;"></div>
    <span style="font-style: italic; text-shadow: 2px 2px 4px #888; color: white;">Cataract 👁️‍🗨️</span>
         <!-- <img src="https://pin.it/6mmgqwOvV" alt="Cartoon Character" style="height: 50px; width: auto;"> -->
</div>

<script>
    function toggleAnimation() {
        var container = document.getElementById('animated-container');
        var animationDiv = container.querySelector('div');
        if (animationDiv.style.animationPlayState === 'paused') {
            animationDiv.style.animationPlayState = 'running';
        } else {
            animationDiv.style.animationPlayState = 'paused';
        }
    }
</script>

"""

# Specify the path containing the images to visualize
path_to_visualize = "/kaggle/input/eye-diseases-classification/dataset/cataract"

# Visualize 5 random images
visualize_images(path_to_visualize, num_images=5)

"""<a id="1"></a>
<div id="animated-container" style="position: relative;
            border-radius: 10px;
            padding: 10px;
            font-family: Arial, sans-serif;
            font-size: 36px;
            font-weight: 900;
            color: black;
            display: inline-block;
            text-transform: uppercase;
            box-shadow: 2px 2px 4px #888;
            text-shadow: 2px 2px 4px #888;
            overflow: hidden;
            background-color: #800606 ;
            cursor: pointer;" onclick="toggleAnimation()"> <!-- Added cursor pointer and onclick event -->
    <div style="position: absolute;
                top: 50%;
                right: 0; /* Adjusted to place on the right side */
                transform: translateY(45%);">
        <!-- <img src="https://www.kaggle.com/static/images/tier-animation-transparent.gif" alt="Cartoon Character" style="height: 100px; width: auto;"> -->
    </div>
    <div style="font-weight: bold;"></div>
    <span style="font-style: italic; text-shadow: 2px 2px 4px #888; color: white;">Diabetic-Retinopathy 🦠</span>
         <!-- <img src="https://pin.it/6mmgqwOvV" alt="Cartoon Character" style="height: 50px; width: auto;"> -->
</div>

<script>
    function toggleAnimation() {
        var container = document.getElementById('animated-container');
        var animationDiv = container.querySelector('div');
        if (animationDiv.style.animationPlayState === 'paused') {
            animationDiv.style.animationPlayState = 'running';
        } else {
            animationDiv.style.animationPlayState = 'paused';
        }
    }
</script>

"""

# Specify the path containing the images to visualize
path_to_visualize = "/kaggle/input/eye-diseases-classification/dataset/diabetic_retinopathy"

# Visualize 5 random images
visualize_images(path_to_visualize, num_images=5)

"""<a id="1"></a>
<div id="animated-container" style="position: relative;
            border-radius: 10px;
            padding: 10px;
            font-family: Arial, sans-serif;
            font-size: 36px;
            font-weight: 900;
            color: black;
            display: inline-block;
            text-transform: uppercase;
            box-shadow: 2px 2px 4px #888;
            text-shadow: 2px 2px 4px #888;
            overflow: hidden;
            background-color: #800606 ;
            cursor: pointer;" onclick="toggleAnimation()"> <!-- Added cursor pointer and onclick event -->
    <div style="position: absolute;
                top: 50%;
                right: 0; /* Adjusted to place on the right side */
                transform: translateY(45%);">
        <!-- <img src="https://www.kaggle.com/static/images/tier-animation-transparent.gif" alt="Cartoon Character" style="height: 100px; width: auto;"> -->
    </div>
    <div style="font-weight: bold;"></div>
    <span style="font-style: italic; text-shadow: 2px 2px 4px #888; color: white;">Glaucoma 🧿</span>
         <!-- <img src="https://pin.it/6mmgqwOvV" alt="Cartoon Character" style="height: 50px; width: auto;"> -->
</div>

<script>
    function toggleAnimation() {
        var container = document.getElementById('animated-container');
        var animationDiv = container.querySelector('div');
        if (animationDiv.style.animationPlayState === 'paused') {
            animationDiv.style.animationPlayState = 'running';
        } else {
            animationDiv.style.animationPlayState = 'paused';
        }
    }
</script>

"""

# Specify the path containing the images to visualize
path_to_visualize = "/kaggle/input/eye-diseases-classification/dataset/glaucoma"

# Visualize 5 random images
visualize_images(path_to_visualize, num_images=5)

"""<a id="1"></a>
<div id="animated-container" style="position: relative;
            border-radius: 10px;
            padding: 10px;
            font-family: Arial, sans-serif;
            font-size: 36px;
            font-weight: 900;
            color: black;
            display: inline-block;
            text-transform: uppercase;
            box-shadow: 2px 2px 4px #888;
            text-shadow: 2px 2px 4px #888;
            overflow: hidden;
            background-color: #800606 ;
            cursor: pointer;" onclick="toggleAnimation()"> <!-- Added cursor pointer and onclick event -->
    <div style="position: absolute;
                top: 50%;
                right: 0; /* Adjusted to place on the right side */
                transform: translateY(45%);">
        <!-- <img src="https://www.kaggle.com/static/images/tier-animation-transparent.gif" alt="Cartoon Character" style="height: 100px; width: auto;"> -->
    </div>
    <div style="font-weight: bold;"></div>
    <span style="font-style: italic; text-shadow: 2px 2px 4px #888; color: white;">Normal 𓆩 👁️ 𓆪</span>
         <!-- <img src="https://pin.it/6mmgqwOvV" alt="Cartoon Character" style="height: 50px; width: auto;"> -->
</div>

<script>
    function toggleAnimation() {
        var container = document.getElementById('animated-container');
        var animationDiv = container.querySelector('div');
        if (animationDiv.style.animationPlayState === 'paused') {
            animationDiv.style.animationPlayState = 'running';
        } else {
            animationDiv.style.animationPlayState = 'paused';
        }
    }
</script>

"""

# Specify the path containing the images to visualize
path_to_visualize = "/kaggle/input/eye-diseases-classification/dataset/normal"

# Visualize 5 random images
visualize_images(path_to_visualize, num_images=5)

"""<a id="1"></a>
<div id="animated-container" style="position: relative;
            border-radius: 10px;
            padding: 10px;
            font-family: Arial, sans-serif;
            font-size: 36px;
            font-weight: 900;
            color: black;
            display: inline-block;
            text-transform: uppercase;
            box-shadow: 2px 2px 4px #888;
            text-shadow: 2px 2px 4px #888;
            overflow: hidden;
            background-color: #800606 ;
            cursor: pointer;" onclick="toggleAnimation()"> <!-- Added cursor pointer and onclick event -->
    <div style="position: absolute;
                top: 50%;
                right: 0; /* Adjusted to place on the right side */
                transform: translateY(45%);">
        <!-- <img src="https://www.kaggle.com/static/images/tier-animation-transparent.gif" alt="Cartoon Character" style="height: 100px; width: auto;"> -->
    </div>
    <div style="font-weight: bold;"></div>
    <span style="font-style: italic; text-shadow: 2px 2px 4px #888; color: white;">Model 🤖</span>
         <!-- <img src="https://pin.it/6mmgqwOvV" alt="Cartoon Character" style="height: 50px; width: auto;"> -->
</div>

<script>
    function toggleAnimation() {
        var container = document.getElementById('animated-container');
        var animationDiv = container.querySelector('div');
        if (animationDiv.style.animationPlayState === 'paused') {
            animationDiv.style.animationPlayState = 'running';
        } else {
            animationDiv.style.animationPlayState = 'paused';
        }
    }
</script>

## **Build Model & Check Summary**
"""

# Define RNN model
model = tf.keras.Sequential([
    tf.keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(256, 256, 3)),
    tf.keras.layers.MaxPooling2D((2, 2)),
    tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
    tf.keras.layers.MaxPooling2D((2, 2)),
    tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
    tf.keras.layers.MaxPooling2D((2, 2)),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Reshape((64, 1)),  # Reshape for RNN input
    tf.keras.layers.SimpleRNN(32),  # Simple RNN layer
    tf.keras.layers.Dense(4, activation='softmax')  # Output layer
])

# Compile the model
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# Print model summary
print(model.summary())

"""## **Fit Model**"""

# Define early stopping callback
from tensorflow.keras.callbacks import EarlyStopping
early_stopping = EarlyStopping(patience=5, restore_best_weights=True)

# Fit the model with callbacks
history = model.fit(train_ds,
                    validation_data=validation_ds,
                    epochs=5,
                    callbacks=[early_stopping])

"""## **Evaluate Model**"""

# Evaluate on test data
test_loss, test_accuracy = model.evaluate(test_ds)
print("Test accuracy:", test_accuracy)

"""## **History Plot**"""

# Define epochs
epochs = range(1, len(history.history['loss']) + 1)

# Plot training & validation loss
plt.plot(epochs, history.history['loss'], label='Training Loss', marker='o')
plt.plot(epochs, history.history['val_loss'], label='Validation Loss', marker='o')
plt.title('Model Loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.legend()
plt.show()

# Plot training & validation accuracy
plt.plot(epochs, history.history['accuracy'], label='Training Accuracy', marker='o')
plt.plot(epochs, history.history['val_accuracy'], label='Validation Accuracy', marker='o')
plt.title('Model Accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.legend()
plt.show()