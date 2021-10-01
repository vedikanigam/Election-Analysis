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

#Iterate through candidate list
for candidate_name in candidate_votes:

    #Retrieve vote count of a candidate
    votes = candidate_votes[candidate_name]

    vote_percentage = float(votes)/float(total_votes) * 100

    #print candidate name and percentage of votes
    print(f"{candidate_name}: received {vote_percentage:.1f}% of the total vote.")

        







        


    
    
   

