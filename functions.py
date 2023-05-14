import tkinter as tk
import game
def create_game_window(root_home, windows):
    #populate the game images
    game.populateLevels()
    # Create a new window
    game_window = tk.Toplevel(root_home)

    # Add to other_windows
    windows["game_window"] = game_window

    # Hide the current window
    for window_name, window in windows.items():
        if window_name != "game_window" and window.winfo_exists():
            window.withdraw()

    screen_width = game_window.winfo_screenwidth()
    screen_height = game_window.winfo_screenheight()

    # Set the window size and position
    window_width = int(screen_width)
    window_height = int(screen_height)
    window_x = int((screen_width - window_width) / 2)
    window_y = int((screen_height - window_height) / 2)

    game_window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

    game_window.title("EMO Quest -- Game")

    # Create a frame for the navigation bar
    navbar_frame = tk.Frame(game_window, bg="lightblue", height=30)
    navbar_frame.pack(side=tk.TOP, fill=tk.X, anchor=tk.NE)

    # Add a play Game button
    button_game = tk.Button(navbar_frame, text="Play Game", font=("Times", 20))
    button_game.pack(side=tk.RIGHT)

    # Add a back arrow button to the new window
    back_button = tk.Button(navbar_frame, text="Home", bg="blue", font=("Times", 20), command=lambda: [game_window.destroy(), root_home.deiconify()])
    back_button.pack(side=tk.RIGHT)
    
    # Add widgets to the new window
    label = tk.Label(game_window, text="Starting the game")
    label.pack(pady=10)

    # Add Logo
    game_window.logo_image = tk.PhotoImage(file="EMO_logo.png").subsample(2)
    label = tk.Label(game_window, image=game_window.logo_image)
    label.place(relx=1.0, rely=1.0, anchor=tk.SE)
