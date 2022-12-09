#!/bin/bash

# Get the current date and time in the format "YYYY-MM-DD HH:MM:SS"
timestamp=$(date +"%Y-%m-%d %H:%M:%S")

# Convert the timestamp to letters by replacing each character with its corresponding
# letter of the alphabet (e.g. Y becomes A, B becomes B, etc.)
timestamp_letters=$(echo $timestamp | tr 'A-Za-z' 'N-ZA-Mn-za-m')

# Print the converted timestamp
echo $timestamp_letters