## Overview of Election-Audit
In this project, we are helping Colorado Board of Elections employee - Mr. Tom in an election audit. This audit is of the tabulated results for US congressional precinct in Colorado. To automate this audit, we will write a code in a programming language called Python.

### Purpose
The purpose of the analysis is to provide a summary of the election audit. This summary will include total number of votes that were cast in this congressional election, total votes for each candidate and their percentage, and the winner of this election. Furthermore, we will find out which county had the largest number of votes and percentage of votes for each county in the precinct. 

## Election-Audit Results

- **Total votes cast** -
To calculate total vote that were cast in this election we first initialize total votes as zero. Next, we create a loop that iterates through all the rows in election results csv file and increment total votes by 1 each time this loop goes to next row. See image of the code below. 

![Total Votes]https://github.com/vedikanigam/Election-Analysis/blob/main/Resources/Total_votes.png

- **Total votes cast in each county** -
To calculate total number of votes that were cast in each county, we first find out how many counties are there in this precinct. An empty county list is created outside the loop that iterates over all the rows. Then, to get the unique county names from all the rows, an if statement is used within this loop to add each new county to the county list each time the loop comes across a new one. See image of code below. 

![County List]https://github.com/vedikanigam/Election-Analysis/blob/main/Resources/county_list.png

Second, to add total votes in each county we first create a county votes dictionary outside the loop and then increment the value of key (county name) by 1 inside the loop for each row for that county. 

![County Votes]https://github.com/vedikanigam/Election-Analysis/blob/main/Resources/county_votes.png

Third, to calculate the percentage of votes in each county another loop is created that retrieves votes for each county from the county votes dictionary. Finally, by dividing county votes by total number of votes and multiplying by 100 we get the county vote percentage. See image of code below.

![CountyVotePercentage]https://github.com/vedikanigam/ElectionAnalysis/blob/main/Resources/county_votepercentage.png

- **County with largest number of votes** -
To figure out the county with the highest vote count we use an if statement within the loop where we retrieve the county votes and calculate their percentage. We initialize highest vote count as zero in the very beginning. In the if statement, each time it encounters a higher value than the current highest value it updates the current highest value to the encountered value. See image of code below. 

![highest Votecount]https://github.com/vedikanigam/Election-Analysis/blob/main/Resources/highestvotecount_county.png

- **Total votes cast for each candidate** -
The process for finding total votes for each candidate is similar to the one that we used for counties. First, we initialize an empty list of candidates and create a dictionary that contains candidate names as keys and votes they received as values. See image of code below.

![candidate Votes]https://github.com/vedikanigam/Election-Analysis/blob/main/Resources/candidate_votes.png

Second, in the loop that iterates through all the rows we find all unique candidate names using an if statement and add them to the candidate list. In this if statement, we also initialize each candidate votes as zero. Inside the loop we increment the value of key (candidate name) by 1 for each row for that candidate.

Finally, to calculate the percentage of votes for each candidate, another loop is created to retrieve votes for each candidate using get function. This vote count is divided by total vote count and multiplied by 100 to get vote percentage. See image of code below.

![Candidate VotePercentage]https://github.com/vedikanigam/Election-Analysis/blob/main/Resources/candidate_votepercentage.png

- **Winning candidate** -
For finding the winning candidate, at the beginning of this code we initialize vote count for winning candidate as zero and initialize a variable to store winning candidate’s name.  Next, an if statement is used within the loop where we iterate through candidate names in candidate votes dictionary. In the if statement, each time the loop encounter total vote count that is higher than the current highest vote count, it updates the current highest vote count to the encountered value.  See image of code below.

![Winning Candidate]https://github.com/vedikanigam/Election-Analysis/blob/main/Resources/winning_candidate.png

## Summary
As we can see from this process, we modified the code used for calculating summary of votes for candidates to calculate summary of votes for each county. Similarly, we can modify the code to calculate election results where candidates represent parties. 
Furthermore, we can combine local results to obtain state and nationwide results.
