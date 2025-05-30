# Write a script that walks through a nested folder structure 
# and prints out all the Python files it can find.
# Run it in your labs folder and add formatting for nicer viewing.

import os

path = 'C:\\Users\\escot\\Codingnomads'

if not os.path.exists(path):
    print(f"Path does not exist: {path}")
else:
    print(f"Scanning: {path}")
    found = False
    for root, _, files in os.walk(path):
        print(f" {root}")
        for f in files:
            print(f"Found file: {f}")  # Show all files
            if f.endswith('.py'):
                print(f"     Python file: {f}")
                found = True
    if not found:
        print("No Python files found.")
