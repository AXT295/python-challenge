# Importing file
import os, csv
from pathlib import Path 

# Locating file through pathlib
input_file = os.path.join(os.path.dirname(__file__), "Resources\\budget_data.csv")

# For the following variables, create an empty lists that can be repeated in a specific row
total_months = []
total_profit = []
monthly_profit_change = []
 
# Using the context manager to open a csv in a default reading mode
with open(input_file,newline="", encoding="utf-8") as budget:

     # Using this variable to store the data of budget_data.csv
    csvreader = csv.reader(budget,delimiter=",") 

    # Using a context manager to open a csv in a default reading mode
    header = next(csvreader)  

    for row in csvreader: 

        # In their respective lists, adding the total months and full profits
        total_months.append(row[0])
        total_profit.append(int(row[1]))

    # In order to obtain the monthly change in profits, have to go through the profits again
    for i in range(len(total_profit)-1):
        
        # For the difference between two months, add a monthly change in profit
        monthly_profit_change.append(total_profit[i+1]-total_profit[i])
        
# Getting the monthly change in profit list for maximum and minimum
max_increase_value = max(monthly_profit_change)
max_decrease_value = min(monthly_profit_change)

# Using a list of months and an index from max and min, compute maximum and minimum to the correct month
# Since the month associated with the change is +1 month or the next month, had to use the plus 1 at the end of each month
max_increase_month = monthly_profit_change.index(max(monthly_profit_change)) + 1
max_decrease_month = monthly_profit_change.index(min(monthly_profit_change)) + 1 

# Print Statements

print("Financial Analysis")
print()
print("----------------------------")
print()
print(f"Total Months: {len(total_months)}")
print()
print(f"Total: ${sum(total_profit)}")
print()
print(f"Average Change: {round(sum(monthly_profit_change)/len(monthly_profit_change),2)}")
print()
print(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase_value))})")
print()
print(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease_value))})")


# Outputing files
output_file = os.path.join(os.path.dirname(__file__), "Analysis\\Financial_Analysis_Summary.txt")

with open(output_file,"w") as file:
    
# Creating a print method for Financial_Analysis_Summary 
    file.write("Financial Analysis")
    file.write("\n")
    file.write("----------------------------")
    file.write("\n")
    file.write(f"Total Months: {len(total_months)}")
    file.write("\n")
    file.write(f"Total: ${sum(total_profit)}")
    file.write("\n")
    file.write(f"Average Change: {round(sum(monthly_profit_change)/len(monthly_profit_change),2)}")
    file.write("\n")
    file.write(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase_value))})")
    file.write("\n")
    file.write(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease_value))})")