import numpy as np
import matplotlib.pyplot as plt

def generate_ecg_waveform(duration=10, sampling_rate=256):
    # Time array
    t = np.linspace(0, duration, int(duration * sampling_rate))
    # ECG parameters
    hr = 60  # Heart rate in beats per minute
    hr_period = 60 / hr  # Duration of one heart beat in seconds

    # Generate synthetic ECG using sinusoids
    ecg_signal = 1.2 * np.sin(2 * np.pi * 5.0 * t)  # Basic cardiac frequency component
    ecg_signal += 0.25 * np.sin(2 * np.pi * 10.0 * t)  # Higher frequency component
    ecg_signal += 0.15 * np.sin(2 * np.pi * 20.0 * t)  # Even higher frequency component

    # Adding an artificial spike mimicking the QRS complex
    for i in range(int(duration // hr_period)):
        qrs_start = int((i * hr_period + 0.25 * hr_period) * sampling_rate)
        qrs_end = qrs_start + int(0.1 * sampling_rate)
        ecg_signal[qrs_start:qrs_end] += 12 * np.exp(-((t[qrs_start:qrs_end] - t[qrs_start]) / 0.01)**2)

    return t, ecg_signal

# Generate and plot ECG waveform
t, ecg_signal = generate_ecg_waveform()
plt.plot(t, ecg_signal)
plt.title("Synthetic ECG Signal")
plt.xlabel("Time (seconds)")
plt.ylabel("Amplitude")
plt.show()
