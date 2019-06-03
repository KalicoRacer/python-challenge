import csv

# Declare variables
file_name = "Resources/election_data.csv"

vote_records = []
election_results = {"khan": 0, "correy": 0, "li": 0, "otooley": 0}

khan_votes = 0
correy_votes = 0
li_votes = 0
otooley_votes = 0

# Open csv file and import each row except header
# If csv file does not have a hear csv_header flag needs to be changed to 'False'
with open(file_name, newline='') as csvfile:
    csvreader = csv.reader(csvfile)

    # Change csv_header to 'False' if csv file does not have headers
    csv_header = True
    for row in csvreader:
        if csv_header == False:
            vote_records.append([int(row[0]), row[1], row[2]])
        else:
            csv_header = False
            continue

vote_total = len(vote_records)

# Calculate the vote totals for each candidate
for record in vote_records:
    vote_current = record[2]
    if vote_current == "Khan":
        khan_votes += 1
    elif vote_current == "Correy":
        correy_votes += 1
    elif vote_current == "Li":
        li_votes += 1
    elif vote_current == "O'Tooley":
        otooley_votes += 1

# Change the values in the election_results dictionary with totals
election_results["khan"] = khan_votes
election_results["correy"] = correy_votes
election_results["li"] = li_votes
election_results["otooley"] = otooley_votes

winner = max(election_results, key=lambda key: election_results[key])

print("Election Results\n")
print("----------------------------")
print("Total Votes: " + str(vote_total))
print("----------------------------")
print("Khan: " + "{:.3%}".format(khan_votes / vote_total) + " (" + str(election_results["khan"]) + ")")
print("Correy: " + "{:.3%}".format(correy_votes / vote_total) + " (" + str(election_results["correy"]) + ")")
print("Li: " + "{:.3%}".format(li_votes / vote_total) + " (" + str(election_results["li"]) + ")")
print("O'Tooley: " + "{:.3%}".format(otooley_votes / vote_total) + " (" + str(election_results["otooley"]) + ")")
print("\n----------------------------")
print("Winner: " + str(winner.title()))
print("----------------------------")

output_file = "Output/election_results.txt"
with open(output_file, "w+") as vote_output:
    vote_output.write("Election Results\n\n")
    vote_output.write("----------------------------\n")
    vote_output.write("Total Votes: " + str(vote_total) + "\n")
    vote_output.write("----------------------------\n")
    vote_output.write("Khan: " + "{:.3%}".format(khan_votes / vote_total) + " (" + str(election_results["khan"]) + ")\n")
    vote_output.write("Correy: " + "{:.3%}".format(correy_votes / vote_total) + " (" + str(election_results["correy"]) + ")\n")
    vote_output.write("Li: " + "{:.3%}".format(li_votes / vote_total) + " (" + str(election_results["li"]) + ")\n")
    vote_output.write("O'Tooley: " + "{:.3%}".format(otooley_votes / vote_total) + " (" + str(election_results["otooley"]) + ")\n")
    vote_output.write("\n----------------------------\n")
    vote_output.write("Winner: " + str(winner.title()))
    vote_output.write("\n----------------------------")
