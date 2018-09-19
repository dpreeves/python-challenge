#Import

import os
import csv
import collections

# File Location

csvpath = os.path.join("election_data.csv")

#Default Read mode

with open(csvpath,newline="", encoding="utf-8") as election:

# Store contents

    csvreader = csv.reader(election,delimiter=",")

    header = next(csvreader)
    
    candidates = []

    #Define row 3 as candidate

    for row in csvreader:
        candidate = row [2]

        candidates.append(candidate)

    for candidate in candidates
        
