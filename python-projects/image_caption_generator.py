'''
Image captioning is a fascinating application of deep learning. In this project, you will use Pythin and the TensorFlow library to create an image caption generator. 
By combining computer vision and natural language . processing techniques, your program will be able to generate descriptive captions for images automatically. 
'''
import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import os

# Load the pre-trained InceptionV3 model
inception_model = tf.keras.applications.InceptionV3(include_top=True, weights='imagenet')

# Load the tokenizer
tokenizer = tf.keras.preprocessing.text.Tokenizer()
tokenizer_path = 'tokenizer.pkl'
tokenizer = tf.keras.preprocessing.text.tokenizer_from_json(tokenizer_path)

# Define the maximum sequence length (number of words) for captions
max_sequence_length = 20

# Load the pre-trained caption generation model
model_path = 'caption_generator_model.h5'
model = tf.keras.models.load_model(model_path)

# Load the word-to-index and index-to-word mappings
word_to_index = tokenizer.word_index
index_to_word = {index: word for word, index in word_to_index.items()}

# Load the pre-trained InceptionV3 model
inception_model = tf.keras.applications.InceptionV3(include_top=True, weights='imagenet')

def preprocess_image(image_path):
    """Preprocess the image for input to the InceptionV3 model."""
    img = Image.open(image_path)
    img = img.resize((299, 299))
    img = np.array(img)
    img = img / 255.0
    img = img.reshape(1, 299, 299, 3)
    return img

def generate_caption(image_path):
    """Generate a caption for the given image."""
    img = preprocess_image(image_path)
    features = inception_model.predict(img)
    features = features.reshape(1, -1)
    
    start_token = tokenizer.word_index['<start>']
    end_token = tokenizer.word_index['<end>']
    
    caption = []
    input_sequence = [start_token]
    for _ in range(max_sequence_length):
        sequence = np.array(input_sequence)
        y_pred = model.predict([features, sequence])
        y_pred = np.argmax(y_pred)
        
        if index_to_word[y_pred] == '<end>':
            break
        
        caption.append(index_to_word[y_pred])
        input_sequence.append(y_pred)
    
    generated_caption = ' '.join(caption)
    return generated_caption

# Path to the image for caption generation
image_path = 'example_image.jpg'

# Generate caption for the image
caption = generate_caption(image_path)
print('Generated Caption:', caption)

# Display the image
img = Image.open(image_path)
plt.imshow(img)
plt.axis('off')
plt.show()