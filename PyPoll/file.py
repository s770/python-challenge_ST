import csv

file = "election_data.csv"

with open(file) as data:
    read = csv.reader(data, delimiter=',')
    next(read)

    votecount = 0

    for row in read:
        votecount += 1
            
    print(votecount)

#A complete list of candidates who received votes
#candidate = ["Khan", "Correy", "Li", "O'Tooley"]
#Run through row 3 and list unique canidates

#The total number of votes each candidate won
#With your unique candidates, loop through file and count votes for each candidate

#The percentage of votes each candidate won
#Count the number to votes for each candidate and divide by votecount and multiple by 100

#The winner of the election based on popular vote.
#Set percentage to max to print winner

##Write an f string to print the final analysis to the terminal and export a text file with the results
#:(