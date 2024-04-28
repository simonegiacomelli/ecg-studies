import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam

# Generate some placeholder data for ecg_data
ecg_data = np.random.randn(1000, 256)
ecg_data = (ecg_data - np.mean(ecg_data)) / np.std(ecg_data)

input_dim = ecg_data.shape[1]
encoding_dim = 32

# Define the encoder and decoder within one Sequential model
autoencoder = Sequential([
    Dense(128, activation='relu', input_shape=(input_dim,)),
    Dense(64, activation='relu'),
    Dense(encoding_dim, activation='relu'),
    Dense(64, activation='relu'),
    Dense(128, activation='relu'),
    Dense(input_dim, activation='sigmoid')
])

autoencoder.compile(optimizer='adam', loss='mean_squared_error')
autoencoder.summary()

# Training the autoencoder
autoencoder.fit(ecg_data, ecg_data, epochs=50, batch_size=256, shuffle=True, validation_split=0.2)
