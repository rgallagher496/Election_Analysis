# The data we need to retrieve.
# 1. The total number of votes cast.
# 2. A complete list of candidates who received votes.
# 3. The percentage of votes each candidate won.
# 4. The total number of votes each candidate won.
# 5. The winner of the election based on popular vote. 

import csv
import os

file_to_load = os.path.join("Resources","election_results.csv")

with open(file_to_load) as election_data:

    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
    #Print each row in the CSV file.
    for row in file_reader:
        print(row)
    
    

