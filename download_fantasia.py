from datetime import datetime
from pathlib import Path

import wfdb

fantasia_dir = 'dataset/fantasia'

start = datetime.now()
wfdb.dl_database('fantasia', fantasia_dir)

download_time = 'Download time: ' + str(datetime.now() - start)

print(download_time)
Path(fantasia_dir + '.done').write_text(download_time)
