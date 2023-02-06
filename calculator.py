import csv
from datetime import datetime

with open('data.csv', 'r') as file:
    reader = csv.DictReader(file)
    data = list(reader)

unfiltered_data = []
for row in data:
    unfiltered_data.append(row)

spent = 0
for row in unfiltered_data:
    trans_value = float (row["Transaction Value"])
    if (row["Transaction Type"] == "CSC Fare Product checkout") or (row["Transaction Type"] == "CSC Fare Product checkin"):
        spent -= trans_value
    elif (row["Transaction Type"] == "CSC tPurse Product Reload") and (trans_value == 14):
        spent -= trans_value
        
        
print("Amount Spent on Transport from ", data[0]["Transaction Date"], " until ", data[-1]["Transaction Date"], ": R", spent)

 