# Importing files
import os, csv
from pathlib import Path 

# Locating file through pathlib
csv_file_path = os.path.join(os.path.dirname(__file__), "Resources\\election_data.csv")


# Creating list of variables
total_votes = 0 
charles_votes= 0
diana_votes = 0
raymon_votes = 0

# Using the context manager to open a csv in a default reading mode
with open(csv_file_path,newline="", encoding="utf-8") as elections:

    # Storing the data under the csvreader variable
    csvreader = csv.reader(elections,delimiter=",") 

    # Using a context manager to open a csv in a default reading mode
    header = next(csvreader)     

    # Going through each row in the csv
    for row in csvreader: 

        # Using a variable to count the unique voter ID and storing it
        total_votes +=1

        # If the name is found, count the number of times it appears, and store it in the list
        # In a print statement, these values may be used to calculate the percentage of votes cast
        if row[2] == "Charles Casper Stockham": 
            charles_votes +=1
        elif row[2] == "Diana DeGette":
            diana_votes +=1
        elif row[2] == "Raymon Anthony Doane": 
            raymon_votes +=1

 # Need to make a dictionary from the two lists that have been made earlier in order to track down the winner
candidates = ["Charles Casper Stockham", "Diana DeGette", "Raymon Anthony Doane"]
votes = [charles_votes, diana_votes,raymon_votes]

# Must combine the list of candidates and the total number of votes by value
# Use the dictionary's maximum function when returning the winner 
dict_candidates_and_votes = dict(zip(candidates,votes))
key = max(dict_candidates_and_votes, key=dict_candidates_and_votes.get)

# Printing out a summary of the analysis
charles_percent = (charles_votes/total_votes) *100
diana_percent = (diana_votes/total_votes) * 100
raymon_percent = (raymon_votes/total_votes)* 100

# Printing out the summary table
print(f"Election Results")
print()
print(f"----------------------------")
print()
print(f"Total Votes: {total_votes}")
print()
print(f"----------------------------")
print()
print(f"Charles Casper Stockham: {charles_percent:.3f}% ({charles_votes})")
print()
print(f"Diana DeGette: {diana_percent:.3f}% ({diana_votes})")
print()
print(f"Raymon Anthony Doane: {raymon_percent:.3f}% ({raymon_votes})")
print()
print(f"----------------------------")
print()
print(f"Winner: {key}")
print()
print(f"----------------------------")

# Outputing files
# Using the pathlib library to assign the location of the output file
#output_file = Path("python-challenge", "PyPoll", "Election_Results_Summary.txt")
output_file = os.path.join(os.path.dirname(__file__), "Analysis\\Election_Results_Summary.txt")

with open(output_file,"w") as file:

# Creating a methods to print to Elections_Results_Summary 
    file.write(f"Election Results")
    file.write("\n\n")
    file.write(f"----------------------------")
    file.write("\n\n")
    file.write(f"Total Votes: {total_votes}")
    file.write("\n\n")
    file.write(f"----------------------------")
    file.write("\n\n")
    file.write(f"Charles Casper Stockham: {charles_percent:.3f}% ({charles_votes})")
    file.write("\n\n")
    file.write(f"Diana DeGette: {diana_percent:.3f}% ({diana_votes})")
    file.write("\n\n")
    file.write(f"Raymon Anthony Doane: {raymon_percent:.3f}% ({raymon_votes})")
    file.write("\n\n")
    file.write(f"----------------------------")
    file.write("\n\n")
    file.write(f"Winner: {key}")
    file.write("\n\n")
    file.write(f"----------------------------")