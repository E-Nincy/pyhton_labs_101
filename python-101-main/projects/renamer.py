# Move and rename all .png files on your Desktop

# Identify all screenshots on your Desktop

# Create a new directory

# Move and rename all screenshots


import pathlib

# Identify all screenshots on your Desktop
screenshots = pathlib.Path(r"C:\Users\escot\OneDrive\Escritorio\screenshots")

# Create a new directory
destination = pathlib.Path(r"C:\Users\escot\OneDrive\Escritorio\renamed_screenshots")
destination.mkdir(exist_ok=True)  # Create the folder if it doesn't exist

# Loop through the files in the screenshots folder
for index, filepath in enumerate(screenshots.iterdir()):
    if filepath.suffix == ".jpg" or filepath.suffix == ".png":
        # Create the new path in the destination folder
        screenshot = destination.joinpath(str(index) + "_" + filepath.name)
        print("Print result:", screenshot)
        # Move and rename the file
        filepath.replace(screenshot)
