import csv
import os

budget_data_csv = os.path.join("..", "Resources", "budget_data.csv")

def budget_calculations(budget_data_csv):
    total_months = 0
    total_net = 0
    total_avg_change = 0
    previous_amount = None
# Initialize to positive infinity
    greatest_decrease = float('inf')  
    greatest_decrease_row = None
# Initialize to negative infinity
    greatest_increase = float('-inf')  
    greatest_increase_row = None
    with open(budget_data_csv, 'r') as file:
        reader = csv.reader(file)
        header_skipped = False
        for i, row in enumerate(reader):
            if not header_skipped:
                header_skipped = True
            # Skip the header
                continue  
            try:
                # Increment the total count for column 0
                total_months += 1
                # Add the value in column 1 to the total amount
                amount = float(row[1])
                total_net += amount
                # Calculate change from previous amount
                if previous_amount is not None:
                    change = amount - previous_amount
                    total_avg_change += change
                previous_amount = amount
                # Check for maximum and minimum amounts
                if amount > greatest_increase:
                    greatest_increase = amount
                    greatest_increase_row = row
                if amount < greatest_decrease:
                    greatest_decrease = amount
                    greatest_decrease_row = row
            except ValueError:
            # Skip if the value cannot be converted to float
                pass  
    # Calculate the average change
    if total_months > 1:
        average_change = total_avg_change / (total_months - 1)
    else:
    # Avoid division by zero if there's only one value
        average_change = 0  
    return total_months, total_net, average_change, greatest_decrease, greatest_decrease_row, greatest_increase, greatest_increase_row

# Exporting script on text file 
f = open('budget_data.txt', 'w')

total_months, total_net, average_change, greatest_decrease, greatest_decrease_row, greatest_increase, greatest_increase_row = budget_calculations(budget_data_csv)
print("(FINANCIAL ANALYSIS)", file=f)
print("----------------------------------", file=f)
print("Total Months:", total_months, file=f)
print("Total Net Profit/Losses: $" + str(total_net), file=f)
print("Average Change:", average_change, file=f)
print("Greatest Increase:", greatest_increase_row, file=f)
print("Greatest Decrease:", greatest_decrease_row, file=f)

# Exporting script on text file 
f.close()