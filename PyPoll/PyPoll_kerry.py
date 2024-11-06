#PyPoll Data 

# Import modules
import csv
import os

election_data = "Resources/election_data.csv"
file_to_output = "Analysis/file_to_output.txt"

# Define variables to track the financial data
total_votes = 0
dict_votes = {}
#an empty dictionary 

#Code ripped 3.2.8 with Booth help
with open(election_data) as csvfile:

    #CSV reader
    csvreader = csv.reader(csvfile, delimiter=',')

    #Read the header row first 
    #Use a f string 
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    #Read each row of data after the header
    for row in csvreader:
        total_votes += 1
        cand = row[2]
        if cand in dict_votes.keys():
            dict_votes[cand] += 1 #add one to each vote
        else: 
            dict_votes[cand] = 1 #initialize with one vote

    for cand in dict_votes:
        candidate_perc = dict_votes[cand]/total_votes * 100
        

  # Open a text file to save the output
        with open(file_to_output, "w") as new_file:
            new_file.write(f"Election Results\n")
            new_file.write(f"Total Votes: {total_votes}\n")
            new_file.write(f"{cand}: {candidate_perc} {dict_votes[cand]}")
            #Thanks for the syntax help here chat GPT





  

