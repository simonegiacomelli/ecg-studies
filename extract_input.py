from pathlib import Path

from wfdb import rdrecord, plot_wfdb

directory = Path('dataset/fantasia')
records = sorted([f for f in directory.iterdir() if f.is_file() and f.suffix == '.hea'])

for record_path in records:
    record = rdrecord(str(record_path.with_suffix('')))

    plot_wfdb(record, title="Record - %s" % record.record_name)
    input("Press enter to continue...")
