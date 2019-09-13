
#%%
#PyBank#
#Financial records analyzation

#Import libraries and dependencies
import csv
import pandas as pd
import numpy as np

#path for CSV file
file_path_input = ("budget_data.csv")
file_path_output = ("annalysis.data.csv")

#Read CSV into Panadas and give it a variable name Budget_DF
Budget_df = pd.read_csv(csvpath, parse_dates=True)

#Number of month records in the CSV
Months = Budget_df["Date"].count()

#Total amount of money captured in the data converted to currency
Total_Funds = '${:.0f}'.format(Budget_df["Profit/Losses"].sum())

#Determine the amount of increase or decrease from the previous month
AvgChange = Budget_df["Profit/Losses"].diff()
Budget_df['Amount Changed'] = AvgChange
AvgChange = Budget_df['Amount Changed'][1:86].mean()

#Identify the greatest positive change
Greatest_Increase = '${:.0f}'.format(Budget_df["Amount Changed"].max())
Greatest_Increase_Date = Budget_df.sort_values('Profit/Losses').tail(1).Date

#Identify the greatest negative change
Greatest_Decrease =  '${:.0f}'.format(Budget_df["Amount Changed"].min())
Greatest_Decrease_Date = Budget_df.sort_values('Profit/Losses').head(1).Date


print("Financial Analysis")
print("----------------------------")
print("Total Months: %s" %(Months))
print("Total: %s" %(Total_Funds))
#Average Change:, ${round(sum(monthly_profit_change)/len(monthly_profit_change),2)}")
print("Average Change: %s" %(AvgChange))
print("Greatest Increase in Profits: %s %s" %(Greatest_Increase_Date.to_string(index=False), Greatest_Increase))
print("Greatest Decrease in Profits: %s %s" %(Greatest_Decrease_Date.to_string(index=False), Greatest_Decrease))


#Export the results to text file 
with open(file_to_output, "W") as txt_file:
    txt_file.write("Financial Analysis")
    txt_file.write("----------------------------")
    txt_file.write("Total Months: %s" %(Months))
    txt_file.write("Total: %s" %(Total_Funds))
    txt_file.write("Average Change: %s" %(AvgChange))
    txt_file.write("Greatest Increase in Profits: %s %s" %(Greatest_Increase_Date.to_string(index=False), Greatest_Increase))
    txt_file.write("Greatest Decrease in Profits: %s %s" %(Greatest_Decrease_Date.to_string(index=False), Greatest_Decrease))
    


#%%



#%%



#%%



