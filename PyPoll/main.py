# PyPoll solution code's basic method has been copied from below link, but changes made to the details 
# https://github.com/Angienoelhaverly/Election_Analysis/blob/main/PyPoll.py

import csv
import os

total_votes = 0

candidate_list = []
candidate_votes_Dict = {}
candidate_win = ""
count_win = 0
percentage_win = 0

#Open & Write the file and Skip header
csvpath = os.path.join("D:\\","Boot Camp","Github Material","python-challenge","PyPoll","Resources","election_data.csv")
outputtxtpath = os.path.join("D:\\","Boot Camp","Github Material","python-challenge","PyPoll","analysis","election_data.txt")

with open(csvpath) as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)
    #Find total vote by total = total +1
    for row in csvreader:
        
        total_votes += 1     
        #Summarize full candidate list + candidate's vote number.
        candidate_name = row[2]
        
        if candidate_name not in candidate_list: 
             
           candidate_list.append(candidate_name)
            
           candidate_votes_Dict[candidate_name] = 0
         #If candidate existing in the dict, then outside loop + 1 for repeating      
        candidate_votes_Dict[candidate_name] += 1
#Print tout to textfile           
with open(outputtxtpath, 'w') as txt_file:
    
    election_results = (
        f"Election Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes}\n"
        f"-------------------------\n")
    print(election_results)
        
    txt_file.write(election_results)

    #find percentage
    for candidate_name in candidate_votes_Dict: 
        #Save vote number into votelist
        votes = candidate_votes_Dict[candidate_name]
        #Calculate the percentage of votes. 
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (f"{candidate_name}: {vote_percentage:.3f}% ({votes})\n")
        
        print(candidate_results)

        txt_file.write(candidate_results)

     

        #Findout winner by comparing max Votes number and max vote percentage
        if (votes > count_win) and (vote_percentage > percentage_win): 
           
            count_win = votes

            percentage_win = vote_percentage
            
            winning_candidate = candidate_name      

    winner= (
        f"-------------------------\n"
        f"\n"
        f"Winner: {winning_candidate}\n"
        f"\n"
        f"-------------------------\n")
    print(winner)

    txt_file.write(winner)