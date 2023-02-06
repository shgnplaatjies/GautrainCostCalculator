# Gautrain Cost Calculator

Calculating your Gautrain costs made easy! All you need to do is download your travel history from the [Gautrain website](https://www.gautrain.co.za/account/travelhistory), rename the file to "data.csv", and run the python script. The script will subtract the Gautrain discount from your history and give you your total cost. It's like having a financial advisor (disclaimer: not financial advice) for your train trips!

## Features

- Subtracts the Gautrain discount from your travel history csv
- Outputs your total cost

## Future Plans

- In the future, I plan to make the script work with all .csv files in a directory, so you don't have to rename your file every time.
- I also have plans to add a prompt for adding boundary days, so you can calculate your costs without having to filter the csv manually.

## Why?

I created this script to help my BBD colleagues (especially those in the Graduate program) keep track of their transport costs for those sweet, sweet claimbacks. Plus, it's always nice to have a cool tool to calculate your expenses and make sure you're not spending more than you've planned to on the Gautrain!

## Limitations

Currently, the script only subtracts R14 reload charges from your history and ignores all other reloads. This is because the Gautrain csv's don't have a distinguish between Rail-User Bus discounts and Card Reloads/Top-Ups, and it seems like the discount is always R14.

# License

This project is licensed under the MIT License, which means it's free and open-source for everyone to use and contribute to. So, if you find any bugs or have any suggestions, don't hesitate to send a pull request or better yet - fork your own Spaghetti Code repo!

# tldr;

This script simplifies the process of calculating your Gautrain costs for those all-important claimbacks, and eliminates the need to scroll through long and tedious Gautrain slips.
