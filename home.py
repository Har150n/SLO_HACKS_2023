import tkinter as tk
from functions import create_game_window
from functions import create_photos_window

windows = {}

# Create home path
root_home = tk.Tk()
root_home.title("EMO Quest")
root_home.geometry("1000x900")
windows["root_home"] = root_home

# Create a frame for the navigation bar
navbar_frame = tk.Frame(root_home, bg="lightblue", height=30)
navbar_frame.pack(side=tk.TOP, fill=tk.X, anchor=tk.NE)

# Add a home button
button_home = tk.Button(navbar_frame, text="Home", bg="blue", font=("Times", 20))
button_home.pack(side=tk.LEFT)

# Add a upload photos button
button_photos = tk.Button(navbar_frame, text="Upload Photos", bg="darkblue", font=("Times", 20), command=lambda:create_photos_window(root_home, windows))
button_photos.pack(side=tk.RIGHT)

# Add a play Game button
button_game = tk.Button(navbar_frame, text="Play Game", bg="darkblue", font=("Times", 20), command=lambda:create_game_window(root_home, windows))
button_game.pack(side=tk.RIGHT)

# Hold contents of home page
main_frame = tk.Frame(root_home)
main_frame.pack(fill=tk.BOTH, expand=True)

# Add a label for the heading
heading_label = tk.Label(main_frame, text="Welcome to EMO Quest", font=("Times", 60))
heading_label.pack()

root_home.mainloop()
