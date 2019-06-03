import csv
from statistics import mean

# Declare variables
file_name = "Resources/budget_data.csv"

pnl_records = []
pnl_changes = []

pnl_prior = 0
pnl_max_change = ["", 0]
pnl_min_change = ["", 0]

# Open csv file and import each row except header
# If csv file does not have a hear csv_header flag needs to be changed to 'False'
with open(file_name, newline='') as csvfile:
    csvreader = csv.reader(csvfile)

    # Change csv_header to 'False' if csv file does not have headers
    csv_header = True
    for row in csvreader:
        if csv_header == False:
            pnl_records.append([row[0], int(row[1])])
        else:
            csv_header = False
            continue

# Calculate the month to month Profit/Loss and assign max and min
# Create a list of each months changes (in future program could be improved to append this to original csv file)
for record in pnl_records:
    pnl_current = record[1]
    if pnl_prior != 0:
        pnl_change = pnl_current - pnl_prior
        if pnl_change > pnl_max_change[1]:
            pnl_max_change = [record[0], pnl_change]
        elif pnl_change < pnl_min_change[1]:
            pnl_min_change = [record[0], pnl_change]
        pnl_prior = pnl_current
        pnl_total = pnl_total + pnl_current
    else:
        pnl_prior = pnl_current
        pnl_total = pnl_current
        continue
    pnl_changes.append(pnl_change)

print("Financial Analysis")
print("----------------------------\n")
print("Total Months: " + str(len(pnl_records)))
print("Total: $" + str(pnl_total))
print("Average  Change: $" + str(round(mean(pnl_changes), 2)))
print("Greatest Increase in Profits: " + pnl_max_change[0] + " ($" + str(round(pnl_max_change[1], 2)) + ")")
print("Greatest Decrease in Profits: " + pnl_min_change[0] + " ($" + str(round(pnl_min_change[1], 2)) + ")")

output_file = "Output/pnl_financial_analysis.txt"
with open(output_file, "w+") as pnl_output:
    pnl_output.write("Financial Analysis\n")
    pnl_output.write("----------------------------\n\n")
    pnl_output.write("Total Months: " + str(len(pnl_records)) + "\n")
    pnl_output.write("Total: $" + str(pnl_total) + "\n")
    pnl_output.write("Average  Change: $" + str(round(mean(pnl_changes), 2)) + "\n")
    pnl_output.write("Greatest Increase in Profits: " + pnl_max_change[0] + " ($" + str(round(pnl_max_change[1], 2)) + ")\n")
    pnl_output.write("Greatest Decrease in Profits: " + pnl_min_change[0] + " ($" + str(round(pnl_min_change[1], 2)) + ")")
