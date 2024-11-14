from datetime import datetime

def log(entry):
    print(f'{datetime.now()} {entry}', flush=True)

def lug(entry):
    print(f'{datetime.now()} {entry}', end=' ', flush=True)

def leg(entry):
    print(f'{entry}', flush=True)
