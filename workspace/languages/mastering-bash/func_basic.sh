#!/bin/bash

# Initialize a counter. The script will exit when this reaches 10.
var1=1

# Function to display disk usage
disk() {
    clear
    echo "--- Disk Usage (Iteration: $var1) ---"
    df -h
    echo -e "\n"
    # A more robust way to get free space on the root directory
    echo "$(df -H / | awk 'NR==2 {print "Free Space on Root: " $4}')"
    ((var1++))
}

# Function to display system uptime
bigups() {
    clear
    echo "--- System Uptime (Iteration: $var1) ---"
    uptime
    ((var1++))
}

# Function to display system information
sysinfo() {
    clear
    echo "--- System Information (Iteration: $var1) ---"
    uname -a
    ((var1++))
}

# Main menu function
menu() {
    # Loop indefinitely until the user chooses to exit or the counter hits the limit
    while true; do
        # Check if the iteration limit has been reached
        if [ "$var1" -ge 10 ]; then
            clear
            echo "Iteration limit reached. Exiting."
            exit
        fi

        echo "
        Linux SysAdmin Toolkit (Run $var1 of 9)
        **************************************
        1) Disk Usage
        2) System Uptime
        3) System Information
        4) Exit
        "

        read -p "Selection...> " selection

        case $selection in
        1)
            disk
            read -p "Press Enter to return to the menu..."
            clear
            ;;
        2)
            bigups
            read -p "Press Enter to return to the menu..."
            clear
            ;;
        3)
            sysinfo
            read -p "Press Enter to return to the menu..."
            clear
            ;;
        4)
            clear
            echo "Exiting."
            exit
            ;;
        *)
            # Handle invalid input
            clear
            echo "Invalid Selection. Please try again."
            sleep 2 # Pause so the user can read the message
            clear
            ;;
        esac
    done
}

# Initial script execution
clear
menu
