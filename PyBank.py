
#%%
#PyBank#
#Financial records analyzation

#Import libraries and dependencies
import csv 
from pathlib import Path

#Set file paths for menu_data.csv and sales_data.csv
budget_filepath = Path('budget_data.csv')
budget_analysis = Path('budget_analysis.txt')

#Initialize list objects to hold our data
data = []
total_months = 1
monthly_profit = []
total_profit = 0
net_change = 0
greatest_decrease = ["", 99999999999]
greatest_increase = ["", 0]


# Read in the menu data into the menu list
with open(budget_filepath) as budget_data:
    # Pass in the csv file to the csv.reader() function
    # (with ',' as the delmiter/separator) and return the csvreader object
    budget_reader = csv.reader(budget_data, delimiter=',')
    header = next(budget_reader)

    #Iterate through rows 
    first_row = next(budget_reader)
    prev_month = int(first_row[1])
    total_profit = int(first_row[1])
    
    for data in budget_reader:
        total_months += 1
        total_profit += int(data[1]) 
        net_change = int(data[1]) - prev_month
        monthly_profit.append(net_change)
        prev_month = int(data[1])
       
   #calculate the greates income
        if (net_change > greatest_increase[1]):
            greatest_increase[0] = data[0]
            greatest_increase[1] = net_change
            
        elif (net_change < greatest_decrease[1]):
            greatest_decrease[0] = data[0]
            greatest_decrease[1] = net_change
# Correlate max and min to the proper month using month list and index from max and min
    #max_increase_month = monthly_profit_change.index(max(monthly_profit_change)) + 1
    #max_decrease_month = monthly_profit_change.index(min(monthly_profit_change)) + 1 

##Is this the best way to do it? bette with a Else if statement? 

#Print results
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_profit}")
print(f"Average Change:, ${round(sum(monthly_profit)/ len(monthly_profit),2)}")
print(f"Greatest Increase in Profits: ${greatest_increase[1]} {str(greatest_increase[0])}")
print(f"Greatest Decrease in Profits: ${greatest_decrease[1]} {str(greatest_decrease[0])}")

## How do I add commos in the print fumction here? 


#%%
#Obtain the max and min of the the montly profit change list
max_increase_value = max(monthly_profit_change)
max_decrease_value = min(monthly_profit_change)

# Correlate max and min to the proper month using month list and index from max and min
max_increase_month = monthly_profit_change.index(max(monthly_profit_change)) + 1
max_decrease_month = monthly_profit_change.index(min(monthly_profit_change)) + 1 

##Is this the best way to do it? bette with a Else if statement? 

#Print results
print("Financial Analysis\n")
print("----------------------------\n")
print(f"Total Months: {len(data)}\n")
print(f"Total: ${sum(total_profit)}\n")
print(f"Average Change:, ${round(sum(monthly_profit_change)/len(monthly_profit_change),2)}")
print(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase_value))})")
print(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease_value))})")

## How do I add commos in the print fumction here? 


#%%



