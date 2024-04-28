import neurokit2  # pip install neurokit2
import numpy as np
import wfdb.processing

from measure_time import measure_time

ecg_signal = np.fromfile('./dataset/fantasia_csv/f1o01.csv', sep=',')

fs = 250
with measure_time('neurokit2.ecg_peaks: '):
    _, results = neurokit2.ecg_peaks(ecg_signal, sampling_rate=fs)

rpeaks = results["ECG_R_Peaks"]

samples = 2000
fig = wfdb.plot_items(
    ecg_signal[:samples],
    [rpeaks[rpeaks < samples]],
    fs=fs,
    sig_name=["ECG"],
    sig_units=["mV"],
    time_units="seconds",
    return_fig=True,
    ann_style="o",
)
fig.show()
