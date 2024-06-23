# Gautrain Cost Calculator

Calculating your Gautrain costs made simple. You must download your travel history from the [Gautrain website](https://www.gautrain.co.za/account/travelhistory) and run the Python script with a Python interpreter. The script will search and process all .csv files within the current directory, subtract the Gautrain rail user discount from your history, and output your total cost.

## Features

- Subtracts the Gautrain discount from your travel history csv
- Outputs your total cost

## Limitations

Currently, the script only subtracts R14 reload charges from your history and ignores all other reloads.  Gautrain CSV's don't distinguish between Rail-User Bus discounts and Card Reloads/Top-Ups, the discount is always R14. You have to name your file `data.csv`
