import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Dense
from tensorflow.keras.optimizers import Adam

# Assuming ecg_data is a preprocessed dataset where each sample is a 1D numpy array
# For the sake of example, let's generate some random data as a placeholder
ecg_data = np.random.randn(1000, 256)  # 1000 samples, 256 timesteps each

# Normalizing the data (ensure this matches your preprocessing needs)
ecg_data = (ecg_data - np.mean(ecg_data)) / np.std(ecg_data)

# Parameters
input_dim = ecg_data.shape[1]  # number of timesteps in each sample
encoding_dim = 32  # Size of the encoding

# Define the encoder
input_layer = Input(shape=(input_dim,))
encoder = Dense(128, activation='relu')(input_layer)
encoder = Dense(64, activation='relu')(encoder)
encoder = Dense(encoding_dim, activation='relu')(encoder)

# Define the decoder
decoder = Dense(64, activation='relu')(encoder)
decoder = Dense(128, activation='relu')(decoder)
decoder_output = Dense(input_dim, activation='sigmoid')(decoder)

# Build the autoencoder model
autoencoder = Model(inputs=input_layer, outputs=decoder_output)
autoencoder.compile(optimizer='adam', loss='mean_squared_error')

# Print the model summary to check the architecture
autoencoder.summary()

# Training the autoencoder
autoencoder.fit(ecg_data, ecg_data, epochs=50, batch_size=256, shuffle=True, validation_split=0.2)
