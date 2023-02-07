import csv
from datetime import datetime
import os
import re

filesList = os.listdir() # seems like the most appropriate scope


def calculate_costs(filename = 'data.csv'):
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        data = list(reader)


    spent = 0
    for row in data:
        trans_value = float (row["Transaction Value"])
        if (row["Transaction Type"] == "CSC Fare Product checkout") or (row["Transaction Type"] == "CSC Fare Product checkin"):
            spent -= trans_value
        elif (row["Transaction Type"] == "CSC tPurse Product Reload") and (trans_value == 14): #discount is always R14
            spent -= trans_value
            
    
    try:        
        print("Calculated using file:",filename,"\nTimeline:", data[-1]["TransactionÂ\xa0Date"], " - ", data[0]["TransactionÂ\xa0Date"], "\nSpent: R", spent, "\n")
    except: 
        print( "File: ", filename, "\nSpent: ",spent)
    return spent

if __name__ == "__main__":

    for file in filesList:
        if bool(re.search(r"^[0-9A-Za-z)\s$(+*'\"_\-]+\.csv$", file)): #any file with ".csv" at the end, and at least 1 character as it's name. Using '[.]' isn't working, so missing some legal special characters
            try:
                calculate_costs(file)
            except: 
                print("Invalid CSV file:", file)