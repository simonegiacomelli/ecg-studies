import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks, butter, filtfilt

# Load ECG data
ecg_data = np.fromfile('../dataset/fantasia_csv/f1o01.csv', sep=',')[0:500]

# Filter settings
fs = 250  # Sample rate in Hz
lowcut = 0.5
highcut = 45.0
order = 2
nyq = 0.5 * fs
low = lowcut / nyq
high = highcut / nyq
b, a = butter(order, [low, high], btype='band')
filtered_ecg = filtfilt(b, a, ecg_data)


def detect_r_peaks(ecg_signal, fs):
    # Calculate the first derivative of the filtered signal
    derivative = np.diff(ecg_signal)

    # Square the derivatives
    squared_derivative = derivative ** 2

    # Moving average (integration)
    width = int(0.12 * fs)  # Width of the moving window; adjust if necessary
    integrated = np.convolve(squared_derivative, np.ones(width) / width, mode='same')

    # Detect peaks in the integrated signal
    peaks, _ = find_peaks(integrated, distance=fs * 0.2, height=np.max(integrated) * 0.1)
    return peaks, integrated


# Detect R-peaks
peaks, integrated = detect_r_peaks(filtered_ecg, fs)

# Plot results
plt.figure(figsize=(12, 6))
plt.subplot(2, 1, 1)
plt.plot(filtered_ecg, label='Filtered ECG')
plt.plot(peaks, filtered_ecg[peaks], 'ro', label='Detected Peaks')
plt.legend()
plt.title('ECG Signal and Detected R-peaks')

plt.subplot(2, 1, 2)
plt.plot(integrated, label='Integrated Signal')
plt.plot(peaks, integrated[peaks], 'ro', label='Detected Peaks')
plt.legend()
plt.title('Integrated Derivative Signal')
plt.show()
