import os
import csv

budget_csv = os.path.join("budget_data.csv")
output_file = "my_analysis_results.txt"  # File name for exported text file


#lists to store data
date = []
month = []
day = []
profit_losses = []
# change is how much the profit/loss column changes from one row/month to the next
change = []

# with open(udemy_csv, encoding='utf-8') as csvfile:

with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip the header row
    header = next(csvreader)

    for row in csvreader:
        # add each date
        date.append(row[0])

        # add each value in profit/losses column
        profit_losses.append(int(row[1]))
        
        # split the date into month and day
        split_date = row[0].split("-")
        month.append(split_date[0])
        day.append(split_date[1])

        # determine how many months in the month list
        # calculate the sum of the profit_losses column, which were put in the profit_losses list
        num_of_months = len(month)
        net_total_profit_losses = sum(profit_losses)                    

    # calculate the change of profit/loss from each month to the next
    change = [profit_losses[i] - profit_losses[i - 1] for i in range(1, len(profit_losses))]
    # determine how many changes were just calculated and stored in the change list, need this for average
    num_of_changes = len(change)
    # calc average change
    avg_change = sum(change) / num_of_changes
    # round to 2 decimal places
    avg_change_rounded = round(avg_change, 2)

    # loop through change list to find greatest increase and decrease, found max and min on google
    max_increase = max(change)
    # determine the index for the max increase, will use later to print the date
    max_increase_index = change.index(max(change)) + 1 # + 1 acounts for header row
    max_decrease = min(change)
    # determine index for max decrease
    max_decrease_index = change.index(min(change)) + 1
    # find date for max increase and decrease looking for the index number in the date list
    max_inc_date = date[max_increase_index]
    max_dec_date = date[max_decrease_index]

    output = (
        f"Total Months: {num_of_months}\n"
        f"Total: ${net_total_profit_losses}\n"
        f"Average Change: ${avg_change_rounded}\n"
        f"Greatest Increase in Profits: {max_inc_date} (${max_increase})\n"
        f"Greatest Decrease in Profits: {max_dec_date} (${max_decrease})\n")

    # print(f"Total Months: {num_of_months}")
    # print(f"Total: ${net_total_profit_losses}")
    # print(f"Average Change: ${avg_change_rounded}")
    # print(f"Greatest Increase in Profits: {max_inc_date} (${max_increase})")
    # print(f"Greatest Decrease in Profits: {max_dec_date} (${max_decrease})")

    print(output)

    # Export the results to text file
    # This section provided in Slack by Daniel (Instructor)
with open(output_file, "w") as txt_file:
    txt_file.write(output)

# Open the output text file in write mode
# Found the structure for this and txtfile on google
# with open(output_file, "w") as txtfile:
#     # Write the results to the text file
#     # \n tells the code to start a new line
#     # is there a different/more efficient way to do this?
#     txtfile.write("Financial Analysis\n")
#     txtfile.write("---------------------\n")
#     txtfile.write(f"Total Months: {num_of_months}\n")
#     txtfile.write(f"Total: ${net_total_profit_losses}\n")
#     txtfile.write(f"Average Change: ${avg_change_rounded}\n")
#     txtfile.write(f"Greatest Increase in Profits: {max_inc_date} (${max_increase})\n")
#     txtfile.write(f"Greatest Decrease in Profits: {max_dec_date} (${max_decrease})\n")

# Print a message indicating that the export is complete
# got this idea online
print("........................................... ")
print(f"Results exported to {output_file}")
    






