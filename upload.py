import tkinter as tk
from tkinter import filedialog
import cv2
import matplotlib.pyplot as plt
from deepface import DeepFace


def prompt_upload():
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

        img = cv2.imread(file_path)     #get image
        plt.imshow(img[:, :, :: -1])    #call fn and use plt object
        plt.show()                      #display image

        result = DeepFace.analyze(img, actions=['emotion']) #store in result
        print(result)                                       #print it!

    # Close the Tkinter window
    root.destroy()
    return file_paths