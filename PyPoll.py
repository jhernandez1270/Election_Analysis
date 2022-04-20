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

# Open the election results and read the file
with open(file_to_load) as election_data:
    # To do analysis
    # Read the file object with the csv reader function
    file_reader = csv.reader(election_data)

    #print headers using next()
    headers = next(file_reader)
    print(headers)

    #Print each row for the CSV file
    # for row in file_reader:
    #     print(row)



######## LEARNING SECTION
# import csv
# import os


# Assign a variable for the file to load and the path
   #direct access to file
#file_to_load = 'Resources/election_results.csv'
   #indirect access to file
# file_to_load = os.path.join("Resources","election_results.csv")
# # Create a filename variable with a direct or indirect path to the file
# file_to_save = os.path.join("analysis","election_analysis.txt")

# Open the election results and read the file

# election_data = open(file_to_load,'r')
# with open(file_to_load) as election_data:
#     print(election_data)



# Open file using with
# with open(file_to_save,"w") as txt_file:
#     #write 3 counties to the file
#     txt_file.write("Counties in the election\n")
#     txt_file.write("------------------------\n")
#     txt_file.write("Arapahoe\nDenver\nJefferson")
    # txt_file.write("Denver, ")
    # txt_file.write("Jefferson, ")

# Using the open() function with the "w" mode we will write data to the file
# outfile = open(file_to_save,"w")
# outfile.write("Hello World")


# To do analysis

# Close the file
# outfile.close()

#election_data.close()
