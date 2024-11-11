from datetime import datetime

def log(entry):
    print(f'{datetime.now()} {entry}', flush=True)
