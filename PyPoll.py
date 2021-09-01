# The data we need to retrieve.
# 1. The total number of votes cast.
# 2. A complete list of candidates who received votes.
# 3. The percentage of votes each candidate won.
# 4. The total number of votes each candidate won.
# 5. The winner of the election based on popular vote. 

#add dependencies
import csv
import os

#Assing a variable to laod a file from a path
file_to_load = os.path.join("Resources","election_results.csv")
#Assign a variable to save a file to a path
file_to_save = os.path.join("analysis","election_analysis.txt")
#Initializing a variable to count total votes
total_votes = 0
#list for candidate names
candidate_options = []
#creating dictionary for Candidate names and vote counts
candidate_votes = {}
#Winning Candidate and Winning Count Trackers
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#reading election_results.csv
with open(file_to_load) as election_data:

    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
    
    #used to skip header row
    headers = next(file_reader)
    
    #reads through remaineder of the csv file after header row
    for row in file_reader:
        #Counts total votes
        total_votes += 1
        #setting variable to hold candidate name
        candidate_name = row[2]
        #adding only unique names to candidate_option list and initates vote counts in candidate_votes dictionary for each unique candidate
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        
        #count votes for each candidate and add to candidate_votes dictinary
        candidate_votes[candidate_name] += 1
    # calcuates vote_percentage and sets winning variables defined above
    for candidate_name in candidate_votes:
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes)/float(total_votes)*100
        if (votes > winning_count and vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name

        print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

    print(f"--------------------------\n")
    print(f"Winner: {winning_candidate}\n")
    print(f"Winning Vote Count: {winning_count:,}\n")
    print(f"Winning Percentage: {winning_percentage:.1f}%\n")
    print(f"--------------------------")









    

