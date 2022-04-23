# The data we need to retrieve.
# 1. Total number of votes cast.
# 2. A complete list of candidates who received votes.
# 3. The percentage of votes each candidate won.
# 4. The total number of votes each candidate won.
# 5. The winner of the election based on popular vote.

#import dependencies
import csv
import os

# Assign a variable for the file to load and the path
   #indirect access to file
file_to_load = os.path.join("Resources","election_results.csv")
# Create a filename variable with a direct or indirect path to the file
file_to_save = os.path.join("analysis","election_analysis.txt")

# Initialize a total vote counter
total_votes = 0

#initialize the candidate options
candidate_options = []

# Declare candidate votes dictionary
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file
with open(file_to_load) as election_data:
    # To do analysis
    # Read the file object with the csv reader function
    file_reader = csv.reader(election_data)

    #print headers using next()
    headers = next(file_reader)
    

    #Print each row for the CSV file
    for row in file_reader:
        #Add to total vote count
        total_votes += 1
        candidate_name = row[2]

        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            # add it the options list
            candidate_options.append(candidate_name)

            # Begin tracking current candidates vote count
            candidate_votes[candidate_name] = 0

        # Add a vote to the candidate's count
        candidate_votes[candidate_name] += 1

# Determine the percentage of votes for each candidate by looping through the counts.
# 1. Iterate through the candidate list.
for candidate_name in candidate_votes:
# 2. Retrieve vote count of a candidate.
    votes = candidate_votes[candidate_name]
# 3. Calculate the percentage of votes.
    vote_percentage = float(votes) / float(total_votes) * 100
    # To do: print out each candidate's name, vote count, and percentage of
    # votes to the terminal.
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
    
    # Determine winning vote count and candidate
    # 1. Determine if the votes are greater than the winning count.
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        # 2. If true then set winning_count = votes and winning_percent =
        # vote_percentage.
        winning_count = votes
        winning_percentage = vote_percentage
        # 3. Set the winning_candidate equal to the candidate's name.
        winning_candidate = candidate_name

winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)


# 4. Print the candidate name and percentage of votes.
    # print(f"{candidate_name}: received {vote_percentage}% of the vote.")
    

        
#  print total votes
# print(f'Total Votes: {total_votes}')
# print(f'Candidate Votes: {candidate_votes}')


