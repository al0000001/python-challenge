 #Average change   

import os

import csv

csvpath = os.path.join("D:\\","Boot Camp","Github Material","python-challenge","PyBank","Resources","budget_data.csv")

with open(csvpath) as csvfile:
    
    csvreader = csv.DictReader(csvfile, delimiter=',')

    csv_header = next(csvreader)
    p_l=0
    p_l =p_l + float(row(1))
    date = []
    p_change = []

    # in this loop I did sum of column 1 which is revenue in csv file and counted total months which is column 0 
    for row in csvreader:

        p_l.append(float(row[1]))
        date.append(row[0])

    print("Financial Analysis")
    print("-----------------------------------")
    print("Total Months:", len(date))
    print("Total Revenue: $", round(sum(p_l)))


    #in this loop I did total of difference between all row of column "Revenue" and found total revnue change. Also found out max revenue change and min revenue change. 
    for i in range(1,len(p_l)):

        p_change.append(p_l[i] - p_l[i-1])   
    
        avg_p_change = sum(p_change)/len(p_change)

        max_p_change = max(p_change)

        min_p_change = min(p_change)

        max_p_change_date = str(date[p_change.index(max(p_change))])
        min_p_change_date = str(date[p_change.index(min(p_change))])


    print("Avereage Change: $", round(avg_p_change))
    print("Greatest Increase in Profit:", max_p_change_date,"($", round(max_p_change),")")
    print("Greatest Decrease in Profit:", min_p_change_date,"($", round(min_p_change),")")
