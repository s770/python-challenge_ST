import csv
with open(r"C:\Users\New User\Desktop\PREWORK_SJT\Module-3\HW 3\PyBank\budget_data.csv") as csvfile:
  reader = csv.DictReader(csvfile)
  rowcount = 0
  total = 0
  
  for row in reader:
      rowcount += 1
      total = total + int(row['Profit/Losses'])

print(rowcount)
print(total)


#The average change in "Profit/Losses" between months over the entire period
#In layman terms, Calculate the difference between a month’s P&L to the next month’s P&L. 
#Then find the average of the differences for all 86 months.

#The greatest increase in profits (date and amount) over the entire period
#Find the month and year that holds the greatest postive difference btw the month before it over the entire 86 months

#The greatest decrease in losses (date and amount) over the entire period
#Find the time that holds the least difference between the month before it over the entire period

#Write an f string to print the final analysis to the terminal and export a text file with the results

#I’m sorry to submit an incomplete assignment.  