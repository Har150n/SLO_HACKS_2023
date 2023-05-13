import tkinter as tk
import upload
def create_game_window(root_home):
    # Hide the current window
    root_home.withdraw()
    
    # Create a new window
    game_window = tk.Toplevel(root_home)
    game_window.title("EMO Quest -- Game")
    game_window.geometry("1000x900")
    
    # Add a back arrow button to the new window
    back_button = tk.Button(game_window, text="Home", command=lambda: [game_window.destroy(), root_home.deiconify()])
    back_button.pack(pady=10, side=tk.TOP,anchor=tk.NW)
    
    # Add widgets to the new window
    label = tk.Label(game_window, text="This is the new window!")
    label.pack(pady=10)

def create_photos_window(root_home):
    images = upload.prompt_upload()
    # Hide the current window
    root_home.withdraw()
    
    # Create a new window
    photos_window = tk.Toplevel(root_home)
    photos_window.title("EMO Quest -- Photos")
    photos_window.geometry("1000x900")
    
    # Add a back arrow button to the new window
    back_button = tk.Button(photos_window, text="Home", command=lambda: [photos_window.destroy(), root_home.deiconify()])
    back_button.pack(pady=10, side=tk.TOP,anchor=tk.NW)
    
    # Add widgets to the new window
    label = tk.Label(photos_window, text="This is the new photo window!")
    label.pack(pady=10)