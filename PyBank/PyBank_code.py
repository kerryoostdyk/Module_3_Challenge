"""PyBank Homework"""
#Thanks to Booth, Reed, and ChatGTP for the help

# Dependencies
import csv
import os

filepath = "Resources/budget_data.csv"
output_file = "analysis/analysis_pybank.txt"

#Define variables to track the financial data
#All start with 0
num_months = 0
profit_sum = 0
#profit by months
last_profit = 0
current_profit = 0 
total_change = 0
#Anaylsis variables 
#min and max month are empty strings
#max and min change start at 0 
max_change = 0
max_month = ""
min_change = 0
min_month = ""

# Cookie Cutter from previous activity 
with open(filepath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
        #print(row)
        num_months += 1
        profit_sum += int(row[1])
        last_profit = int(row[1])
        current_month_profit = int(row[1])
        change = current_profit - last_profit
        total_change += change
            
        #reset the profit change 
        last_profit=current_profit
            
            #see if the change is a new max change
        if change > max_change: 
            max_change = change
            max_month = row[0]
        if change < min_change:
            min_change = change
            min_month = row[0]

#Generate the output summary using an f string
#Create the leaderboard
output = f"""
Financial Analysis
Total Months: {num_months}
Total: {profit_sum}
Average Change: {total_change / (num_months -1)}
Greatest Increase in Profits: {max_month} {max_change}
Greatest Decrease: month and amount {min_month} {min_change}
"""

# Print the output
print(output)

#write to a text file
#thanks starter code
with open(output_file, "w") as txt_file:
    txt_file.write(output)