import os
import csv

election_csv = os.path.join("election_data.csv")
output_file = "election_results_SZ.txt"

ballot_ID = []
CCS = []
DD = []
RAD = []

with open(election_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # skip the header row
    header = next(csvreader)

    for row in csvreader:
        # add each ballot ID to a list
        ballot_ID.append(row[0])

        if row[2] == "Charles Casper Stockham":
            CCS.append(row[2])
        elif row[2] == "Diana DeGette":
            DD.append(row[2])
        elif row[2] == "Raymon Anthony Doane":
            RAD.append(row[2])
            
    ballots = len(ballot_ID)
    CCS_votes = len(CCS)
    DD_votes = len(DD)
    RAD_votes = len(RAD)
    CCS_percent = round(CCS_votes / ballots * 100, 3)
    DD_percent = round(DD_votes / ballots * 100, 3)
    RAD_percent = round(RAD_votes / ballots * 100, 3)

    if CCS_votes > DD_votes and CCS_votes > RAD_votes:
        winner = "Charles Casper Stockham"
    elif DD_votes > CCS_votes and DD_votes > RAD_votes:
        winner = "Diana DeGette"
    elif RAD_votes > CCS_votes and RAD_votes > DD_votes:
        winner = "Raymon Anthony Doane"

    print(f"Total Votes: {ballots}")
    print("------------------------------")
    print(f"Charles Casper Stockham: {CCS_percent}% ({CCS_votes})")
    print(f"Diana DeGette: {DD_percent}% ({DD_votes})")
    print(f"Raymon Anthony Doane: {RAD_percent}% ({RAD_votes})")
    print("------------------------------")
    print(f"Winner: {winner}")

# Open the output text file in write mode
# Found the structure for this and txtfile on google
with open(output_file, "w") as txtfile:
    # Write the results to the text file
    # \n tells the code to start a new line
    # is there a different/more efficient way to do this?
    txtfile.write("Election Results\n")
    txtfile.write("---------------------\n")
    txtfile.write(f"Total Votes: {ballots}\n")
    txtfile.write("---------------------\n")
    txtfile.write(f"Charles Casper Stockham: {CCS_percent}% ({CCS_votes})\n")
    txtfile.write(f"Diana DeGette: {DD_percent}% ({DD_votes})\n")
    txtfile.write(f"Raymon Anthony Doane: {RAD_percent}% ({RAD_votes})\n")
    txtfile.write("------------------------------\n")
    txtfile.write(f"Winner: {winner}\n")
    txtfile.write("---------------------\n")