import os
import csv

#list
total_months = 0
month_of_change = []
net_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", 999999]
total_net = 0


#path
budget_csv = os.path.join("budget_data.csv")

#open csv
with open(budget_csv) as csvfile:
    budget_reader = csv.reader(csvfile, delimiter=",")

    #skip the header 
    next(budget_reader)
    first_row = next(budget_reader)
    total_months +=1
    total_net += int(first_row[1])
    previous_net = int(first_row[1])
    
    

    #loop 
    for row in budget_reader:

       
        total_months +=1
        
        total_net += int(row[1])
        
        net_change = int(row[1]) - previous_net
        
        previous_net = int(row[1])
        
        net_list += [net_change]
        
        month_of_change += [row[0]]
        
        if net_change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase [1] = net_change
        if net_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease [1] = net_change
            
net_monthly_average = sum(net_list)/len(net_list)

            
        
        
        



#f string
final_totals = (f'''Financial Analysis
----------------------------------
Total Months: {total_months}
Total: ${total_net}
Average Change: ${net_monthly_average:.2f}
Greatest Increase in Profits: {greatest_increase} (${greatest_increase})
Greatest Decrease in Profits: {greatest_decrease} (${greatest_decrease})''')

#print analysis
print(final_totals)

#.txt file 
analysis = open("final_totals.txt", "w")

analysis.write(final_totals)

analysis.close()
