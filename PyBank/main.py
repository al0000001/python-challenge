# PyBank solution code's basic method has been copied from below link, but changes made to the details
# https://stackoverflow.com/questions/46965192/python-how-can-i-find-difference-between-two-rows-of-same-column-using-loop-in

import os

import csv

csvpath = os.path.join("Resources","budget_data.csv")
outputtxtpath = os.path.join("analysis","budget_data.txt")

with open(csvpath) as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)

    p_l=[]
    date = []
    p_change = []
    p_a_change =[]
    for row in csvreader:

        p_l.append(float(row[1]))
        date.append(row[0])
    
with open(outputtxtpath, 'w') as txt_file:

        summary= (f"Financial Analysis\n"
                  f"\n"
                  f"-----------------------------------\n"
                  f"\n"
                  f"Total Months: {len(date)}\n"
                  f"Total: $ {round(sum(p_l))}\n")
        print(summary)
        
        txt_file.write(summary)

        #Find average in changes
        for x in range(1,len(p_l)):
    
            p_a_change.append(p_l[x] - p_l[x-1])  
        
            avg_p_change = str(round(sum(p_a_change)/(len(p_a_change)),2))

        print("Avereage Change: $", avg_p_change)

        txt_file.write(f"Average Change: {avg_p_change}\n")
       
    
        #Find maximum and minimum 
        for i in range(0,len(p_l)):

            p_change.append(p_l[i] - p_l[i-1])  
        
            max_p_change = round(max(p_change))

            min_p_change = round(min(p_change))

            max_p_change_date = str(date[p_change.index(max(p_change))]) 
        
            min_p_change_date = str(date[p_change.index(min(p_change))]) 
        
        maxminsummary= (f"Greatest Increase in Profits: {max_p_change_date} ($ {max_p_change})\n"
                        f"Greatest Decrease in Profits: {min_p_change_date} ($ {min_p_change})"
                        )

        print(maxminsummary)
        txt_file.write(maxminsummary)
        