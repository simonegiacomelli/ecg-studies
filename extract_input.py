from pathlib import Path

from wfdb import rdrecord, plot_wfdb

directory = Path('dataset/fantasia')
records = sorted([f for f in directory.iterdir() if f.is_file() and f.suffix == '.hea'])

directory_csv = Path('dataset/fantasia_csv')
directory_csv.mkdir(exist_ok=True)

for record_path in records:
    record = rdrecord(str(record_path.with_suffix('')),channel_names=['ECG'])
    record1d = record.p_signal.flatten()
    print(record_path.stem + ' len: ' + str(len(record1d)))
    csv_path = directory_csv / (record_path.stem + '.csv')
    # save numpy array to csv file
    record1d.tofile(csv_path, sep=',')