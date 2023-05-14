import tkinter as tk
import game
from game import Game
from PIL import Image, ImageTk

def create_game_window(root_home, windows):
    if Game.populated is False:
        #populate the game images
        game.populateLevels()
        Game.populated = True
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
    center_x = window_width // 2
    center_y = window_height // 2

    game_window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

    game_window.title("EMO Quest -- Game")

    bg = tk.PhotoImage(file="background.png").subsample(2)

    # Show image using label
    label1 = tk.Label(game_window, image=bg)
    label1.place(x=0, y=0)

    # Create a frame for the navigation bar
    navbar_frame = tk.Frame(game_window, bg="lightblue", height=30)
    navbar_frame.pack(side=tk.TOP, fill=tk.X, anchor=tk.NE)

    # Add a play Game button
    button_game = tk.Button(navbar_frame, text="Play Game", font=("Times", 20))
    button_game.pack(side=tk.RIGHT)

    # Add a back arrow button to the new window
    back_button = tk.Button(navbar_frame, text="Home", bg="blue", font=("Times", 20), command=lambda: [game_window.destroy(), root_home.deiconify()])
    back_button.pack(side=tk.RIGHT)

    # Add logo
    image = tk.PhotoImage(file="EMO_logo.png").subsample(2)
    logo_button = tk.Button(game_window, image=image,  highlightthickness=0, pady=0, padx=0)
    logo_button.place(x=center_x, y=center_y-275, anchor=tk.CENTER)




    #add question image
    image_filename =  (Game.levels[Game.level_index]).images[Game.q_index][0]
    game_window.logo_image = tk.PhotoImage(file=image_filename).subsample(2)
    question_image_label = tk.Label(game_window, image=game_window.logo_image)
    question_image_label.place(x=center_x, y=center_y, anchor=tk.CENTER)

    # add level button
    level = tk.Button(game_window, text="Level: " + str(Game.level_index + 1),
                      font=("Arial", 24), borderwidth=0)
    level.place(x=center_x - 100, y=center_y - 180, anchor=tk.CENTER)

    #add score button
    score = tk.Button(game_window, text="Score: " + str(Game.score),
                font=("Arial", 24), borderwidth=0)
    score.place(x=center_x + 100, y=center_y - 180, anchor=tk.CENTER)

    # Create the buttons
    button1 = tk.Button(game_window, text="Happy",
                font=("Arial", 24), command=lambda: game.checkAnswer("happy", root_home, windows))
    button1.place(x=center_x - 75, y=center_y + 200, anchor=tk.CENTER)
    button2 = tk.Button(game_window, text="Angry",
                font=("Arial", 24), command=lambda: game.checkAnswer("angry", root_home, windows))
    button2.place(x=center_x + 75, y=center_y + 200, anchor=tk.CENTER)
    button3 = tk.Button(game_window, text="Fear",
                font=("Arial", 24), command=lambda: game.checkAnswer("fear", root_home, windows))
    button3.place(x=center_x- 75, y=center_y + 250, anchor=tk.CENTER)
    button4 = tk.Button(game_window, text="Disgust",
                font=("Arial", 24), command=lambda: game.checkAnswer("disgust", root_home, windows))
    button4.place(x=center_x + 75, y=center_y + 250, anchor=tk.CENTER)
    button5 = tk.Button(game_window, text="Neutral",
                font=("Arial", 24), command=lambda: game.checkAnswer("neutral", root_home, windows))
    button5.place(x=center_x- 75, y=center_y + 300, anchor=tk.CENTER)
    button6 = tk.Button(game_window, text="Sadness",
                font=("Arial", 24), command=lambda: game.checkAnswer("sad", root_home, windows))
    button6.place(x=center_x+ 75, y=center_y + 300, anchor=tk.CENTER)
    button7 = tk.Button(game_window, text="Surprise",
                        font=("Arial", 24), command=lambda: game.checkAnswer("surprise", root_home, windows))
    button7.place(x=center_x, y=center_y + 350, anchor=tk.CENTER)

    game_window.update()
    game_window.mainloop()



