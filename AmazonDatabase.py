import numpy as np
import pandas as pd

file_name ="amazon.csv"

try:
    df = pd.read_csv(file_name)
except FileNotFoundError:
    print("Error: amazon.csv was not found.")
    print("Place amazon.csv in the same folder as main.py.")
    raise SystemExit

df=head