import tkinter as tk

def create_game_window(root_home, windows):
    # Create a new window
    game_window = tk.Toplevel(root_home)

    # Add to other_windows
    windows["game_window"] = game_window

    # Hide the current window
    for window_name, window in windows.items():
        if window_name != "game_window":
            window.withdraw()

    game_window.title("EMO Quest -- Game")
    game_window.geometry("1000x900")

    # Create a frame for the navigation bar
    navbar_frame = tk.Frame(game_window, bg="lightblue", height=30)
    navbar_frame.pack(side=tk.TOP, fill=tk.X, anchor=tk.NE)

    # Add a back arrow button to the new window
    back_button = tk.Button(navbar_frame, text="Home", bg="blue", font=("Times", 20), command=lambda: [game_window.destroy(), root_home.deiconify()])
    back_button.pack(side=tk.LEFT)

    # Add a upload photos button
    button_photos = tk.Button(navbar_frame, text="Upload Photos", font=("Times", 20), command=lambda:create_photos_window(root_home, windows))
    button_photos.pack(side=tk.RIGHT)

    # Add a play Game button
    button_game = tk.Button(navbar_frame, text="Play Game", font=("Times", 20), command=lambda:create_game_window(root_home, windows))
    button_game.pack(side=tk.RIGHT)

    
    # Add widgets to the new window
    label = tk.Label(game_window, text="This is the new window!")
    label.pack(pady=10)

def create_photos_window(root_home, windows):
    # Create a new window
    photos_window = tk.Toplevel(root_home)

    # Add to other_windows
    windows["photos_window"] = photos_window

    # Hide the current window
    for window_name, window in windows.items():
        if window_name != "photos_window":
            window.withdraw()

    photos_window.title("EMO Quest -- Photos")
    photos_window.geometry("1000x900")

    # Create a frame for the navigation bar
    navbar_frame = tk.Frame(photos_window, bg="lightblue", height=30)
    navbar_frame.pack(side=tk.TOP, fill=tk.X, anchor=tk.NE)

    # Add a back arrow button to the new window
    back_button = tk.Button(navbar_frame, text="Home", bg="blue", font=("Times", 20), command=lambda: [game_window.destroy(), root_home.deiconify()])
    back_button.pack(side=tk.LEFT)

    # Add a upload photos button
    button_photos = tk.Button(navbar_frame, text="Upload Photos", font=("Times", 20), command=lambda:create_photos_window(root_home, windows))
    button_photos.pack(side=tk.RIGHT)

    # Add a play Game button
    button_game = tk.Button(navbar_frame, text="Play Game", font=("Times", 20), command=lambda:create_game_window(root_home, windows))
    button_game.pack(side=tk.RIGHT)
    
    # Add widgets to the new window
    label = tk.Label(photos_window, text="This is the new photo window!")
    label.pack(pady=10)