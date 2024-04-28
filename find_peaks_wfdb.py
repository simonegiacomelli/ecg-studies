import numpy as np
import wfdb
import wfdb.processing

ecg_signal = np.fromfile('./dataset/fantasia_csv/f1o01.csv', sep=',')[0:2000]

fs = 250
rpeaks = wfdb.processing.xqrs_detect(ecg_signal, fs=fs, verbose=False)


fig = wfdb.plot_items(
    ecg_signal,
    [rpeaks],
    fs=fs,
    sig_name=["ECG"],
    sig_units=["mV"],
    time_units="seconds",
    return_fig=True,
    ann_style="o",
)
fig.show()