from datetime import datetime


class measure_time:

    def __init__(self, text: str = None):
        super().__init__()
        self.text = text

    def __enter__(self):
        self.start = datetime.now()
        return self

    def __exit__(self, *args):
        self.end = datetime.now()
        self.interval = self.end - self.start
        if self.text:
            print(f'{self.text} {self.interval}')
