'''
Image captioning is a fascinating application of deep learning. In this project, you will use Pythin and the TensorFlow library to create an image caption generator. 
By combining computer vision and natural language . processing techniques, your program will be able to generate descriptive captions for images automatically. 
'''

import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import os

#Load the pre-trained InceptionV3 model
inception_model = tf.keras.applications.InceptionV3(include_top=True, weight='imagenet')

# Load the tokenizer
tokenizer = tf.keras.preprocessing.text.Tokenizer()