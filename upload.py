import tkinter as tk
from tkinter import filedialog

# Create a Tkinter window to allow file selection
root = tk.Tk()
root.withdraw()

# Ask the user to select multiple image files
print("Please select the images to process:")
file_paths = filedialog.askopenfilenames()

# Process each selected image
for file_path in file_paths:
    # Read the image using OpenCV
    print(file_path)

# Close the Tkinter window
root.destroy()