# Gautrain Cost Calculator

Calculating your Gautrain costs made easy! All you need to do is download your travel history from the [Gautrain website](https://www.gautrain.co.za/account/travelhistory) and run the python script. The script will search and process all .csv files within the current directory, and subtract the Gautrain rail user discount from your history and print your total cost. It's like having a financial advisor (disclaimer: not financial advice) for your train trips!

## Features

- Subtracts the Gautrain discount from your travel history csv
- Outputs your total cost

## Future Plans

- I also want to add a prompt for adding boundary days, so you can calculate your costs dynamically, without having to filter the csv manually. (gautrain offers that on their website currently)

## Why?

I created this script to keep track of my transport costs for those sweet, sweet claimbacks. Also, it's pretty nice to have a quick tool to calculate your expenses and make sure you're not spending more than you've planned to on the Gautrain.

## Limitations

Currently, the script only subtracts R14 reload charges from your history and it ignores all other reloads. Because Gautrain csv's don't distinguish between Rail-User Bus discounts and Card Reloads/Top-Ups, and it seems like the discount is always R14.

# License

This project is under the MIT License, so it's free and open-source for everyone. So, if you find any bugs (if it's calculations are completely wrong) just send a pull request or better yet - fork your own Spaghetti Code repo!

# tldr;

This script automates the process of calculating your Gautrain costs for those claims we all appreciate, no more scrolling through long Gautrain slips.
