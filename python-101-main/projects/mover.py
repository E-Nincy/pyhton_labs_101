# Write a script that moves all files with the .png extension
# from one folder to another

# Import pathlib

# Find the path to my Desktop

# Create a new folder

# Filter for screenshots only

# Create a new path for each file

# Move the screenshot there

# Import pathlib
import pathlib

# Find the path to my Desktop
home = pathlib.Path(r"C:\Users\escot\OneDrive\Escritorio")
screenshots = home / "screenshots"

# Create screenshots folder if it doesn't exist
if not screenshots.exists():
    screenshots.mkdir()

# Move screenshots
for filepath in home.iterdir():
    if filepath.is_file() and filepath.suffix.lower() in [".jpg", ".png"]:
        destination = screenshots / filepath.name
        print("Moving:", filepath, "to", destination)
        filepath.replace(destination)
