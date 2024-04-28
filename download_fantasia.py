from pathlib import Path

import wfdb

dl_dir = Path('dataset/fantasia')
wfdb.dl_database('fantasia', str(dl_dir))
