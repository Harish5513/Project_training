import csv
import json

import pandas as pd
def conv():
    df = pd.read_csv (r'/home/admin-pc/csv/sample.csv')
    df.to_json (r'/home/admin-pc/json/sample.json')

