#!/bin/bash

echo "Welcome to Lucifer Instagram Bot Interface"
echo "Please select an option:"
echo "1. Start the bot"
echo "2. Exit"

read -p "Enter your choice: " user_input

if [ "$user_input" == "1" ]; then
    echo "Starting the bot..."
    python lucifer_bot.py
elif [ "$user_input" == "2" ]; then
    echo "Exiting..."
    exit 0
else
    echo "Invalid option. Please try again."
fi
