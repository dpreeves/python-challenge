#Import

import os
import csv
import Counter

# File Location

csvpath = os.path.join("election_data.csv")

#Default Read mode

with open(csvpath,newline="", encoding="utf-8") as election:

# Store contents

    csvreader = csv.reader(election,delimiter=",")

#Skip Header

    header = next(csvreader)

##Empty List
#
#    total_votes = []    
#    candidates = []
#    candidate_votes = []
##    winning_candidate = []
#
##Store file contents
#    
#    for row in csvreader:
#
##Append votes 

# Voter ID,County,Candidate