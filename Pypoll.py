import csv
import os
# Assign variable to load a file from a path
file_to_load = os.path.join("Resources","election_results.csv")

# Assign variable to save the file to a path
file_to_save = os.path.join("analysis","election_analysis2.txt")

# Initialize variable for total votes cast
total_votes=0

# candidate_list
candidate_list = []

#declare a new dictionary
candidate_votes = {}

#track winning candidate, winning vote count and percentage
winning_candidate = ""
winning_votecount = 0
winning_percentage = 0

# Open election results and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

#Read and skip the header row
    headers = next(file_reader)

#Print each row in csv file
    for row in file_reader:
        # Add vote count
        total_votes += 1

        #Print candidate name from each row
        candidate_name = row[2]

        # If the candidate doe not match existing candidate
        if candidate_name not in candidate_list:
        
            #Add candidate's name to the candidate list
            candidate_list.append(candidate_name)

            #track candidate's vote count
            candidate_votes[candidate_name] = 0

        #increment candidate vote count by 1
        candidate_votes[candidate_name] += 1

#save results to text file
with open(file_to_save, "w") as txt_file:

    #print the final vote count
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
        
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)


    #Iterate through candidate list
    for candidate_name in candidate_votes:

        #Retrieve vote count of a candidate
        votes = candidate_votes[candidate_name]

        vote_percentage = float(votes)/float(total_votes) * 100

        #print candidates name, vote count and percentage
        
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)

        #Save the candidate results to text file
        txt_file.write(candidate_results)

        #determine winning candidate, winning vote count and percentage
        if (votes > winning_votecount) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name  

    #print winning candidate's summary
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)

    #Save winning candidates summary to text file
    txt_file.write(winning_candidate_summary)


            
