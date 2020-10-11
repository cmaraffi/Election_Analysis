#Add our dependencies
import csv
import os

#Assign a variable to load a file from a path
file_to_load= os.path.join("Resources","election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")
#using the open() function with the "w" mode we will write data to the file.
    #open(file_to_save,"w")
#create a filename variable to a direct or indirect path to the file.
#file_to_save = os.path.join("analysis","election_analysis.txt")
#using the with statement open the file as a text file.
#with open(file_to_save,"w") as txt_file:
    #write some data to the file.
    #txt_file.write("Counties in the Election\n------------------------\n")
    #txt_file.write("Arapahoe\nDenver\nJefferson")
#close the file
#outfile.close()

#1. Initialize the total Number of votes cast
total_votes = 0
#2. A complete list of the candidates who received votes
candidate_options = []
candidate_votes = {}
#Define winning count
winning_candidate = ""
winning_count = 0
winning_percentage = 0
 #To do:read and analyse the data here.
#Open the election results and read the file.
with open(file_to_load) as election_data:
    #read the file object with the reader function.
    file_reader = csv.reader(election_data)
    #Print the header row.
    headers = next(file_reader)
    #print each row in the CSV file.
    for row in file_reader:
#1a. The total Number of votes cast
        total_votes = total_votes +1
#1b. Print the total votes.
#2a. print the candidate name from each row
        candidate_name = row[2]
#2b. add the candidate name to the candidate list.
        if candidate_name not in candidate_options:
            #add it to the list of candidates.
           candidate_options.append(candidate_name)
            #begin tracking the cadidates vote count.
           candidate_votes[candidate_name] =0
        #add a vote to that candidate's vote count.
        candidate_votes[candidate_name] +=1    

#3a. Iterate the percentage of votes each candidate won through the candidate list
for candidate_name in candidate_votes:
    #3b. retreive vote count of a candidate.
    votes = candidate_votes[candidate_name]
    #3c. calculate the percentage of votes
    vote_percentage = float(votes) / float(total_votes) * 100
#4a. The total number of votes each candidate won
    if(votes > winning_count) and (vote_percentage > winning_percentage):
        #4b. If true then set winning_count = votes and winning_percent = vote_percentage.
        winning_count = votes
        winning_percentage = vote_percentage
        #4c. set the winning_candidate equal to the candidate's name
        winning_candidate = candidate_name
    #to do: print out the winning candidate, vote count and percentage to terminal.
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")    
#5. The winner of the election based on popular vote.
winning_candidate_summary = (
    f"__________________________\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"--------------------------\n")
print(winning_candidate_summary)
