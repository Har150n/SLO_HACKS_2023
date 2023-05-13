import tkinter as tk
from functions import create_game_window
from functions import create_photos_window
#from deepface import DeepFace

# Create home path
root_home = tk.Tk()
root_home.title("EMO Quest")
root_home.geometry("1000x900")

# Hold contents of home page
main_frame = tk.Frame(root_home)
main_frame.pack(fill=tk.BOTH, expand=True)

# Add a label for the heading
heading_label = tk.Label(main_frame, text="Welcome to EMO Quest", font=("Arial", 24))
heading_label.pack()

# Add a upload photos button
button_photos = tk.Button(main_frame, text="Upload Photos", command=lambda:create_photos_window(root_home))
button_photos.pack()

# Add a play Game button
button_game = tk.Button(main_frame, text="Play Game", command=lambda:create_game_window(root_home))
button_game.pack()

root_home.mainloop()