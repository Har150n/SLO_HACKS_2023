import tkinter as tk
from functions import create_game_window
from functions import create_photos_window

def create_homepage():
    windows = {}

    # Create home path
    root_home = tk.Tk()
    root_home.title("EMO Quest")
    windows["root_home"] = root_home

    # Get the screen width and height
    screen_width = root_home.winfo_screenwidth()
    screen_height = root_home.winfo_screenheight()

    # Set the window size and position
    window_width = int(screen_width)
    window_height = int(screen_height)
    window_x = int((screen_width - window_width) / 2)
    window_y = int((screen_height - window_height) / 2)

    root_home.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

    # Create a frame for the navigation bar
    navbar_frame = tk.Frame(root_home, bg="lightblue", height=30)
    navbar_frame.pack(side=tk.TOP, fill=tk.X, anchor=tk.NE)

<<<<<<< Updated upstream
    # Add a home button
    button_home = tk.Button(navbar_frame, text="Home", bg="blue", font=("Times", 20))
    button_home.pack(side=tk.LEFT)

    # Add a upload photos button
    button_photos = tk.Button(navbar_frame, text="Upload Photos", bg="darkblue", font=("Times", 20), command=lambda:create_photos_window(root_home, windows))
    button_photos.pack(side=tk.RIGHT)

    # Add a play Game button
    button_game = tk.Button(navbar_frame, text="Play Game", bg="darkblue", font=("Times", 20), command=lambda:create_game_window(root_home, windows))
    button_game.pack(side=tk.RIGHT)
=======
# Add a play Game button
button_game = tk.Button(navbar_frame, text="Play Game", bg="blue", font=("Times", 20), command=lambda:create_game_window(root_home, windows))
button_game.pack(side=tk.RIGHT)

# Add a upload photos button
button_photos = tk.Button(navbar_frame, text="Upload Photos", bg="blue", font=("Times", 20), command=lambda:create_photos_window(root_home, windows))
button_photos.pack(side=tk.RIGHT)

# Add a home button
button_home = tk.Button(navbar_frame, text="Home", bg="blue", font=("Times", 20))
button_home.pack(side=tk.RIGHT)
>>>>>>> Stashed changes

    # Hold contents of home page
    main_frame = tk.Frame(root_home)
    main_frame.pack(fill=tk.BOTH, expand=True)

<<<<<<< Updated upstream
    # Add empty label for padding
    padding_label = tk.Label(main_frame, height=10)
    padding_label.pack()
=======
# Add empty label for padding
padding_label = tk.Label(main_frame, height=8)
padding_label.pack()
>>>>>>> Stashed changes

    # Add a label for the heading
    heading_label = tk.Label(main_frame, text="Welcome to EMO Quest", font=("Helvetica", 60))
    heading_label.pack()

<<<<<<< Updated upstream
    # Add Logo
    image = tk.PhotoImage(file="EMO_logo.png")
    label = tk.Label(root_home, image=image)
    label.pack()
=======
# Add about section
subheading_label = tk.Label(main_frame, 
    text = """
            Welcome to our game, designed with a heartfelt mission to help autistic 
            individuals better understand and recognize the emotions of those around them. 
            Our game is specifically tailored to improve facial recognition of emotions 
            from close family and friends, providing a safe and engaging environment for 
            self-improvement. We understand the unique challenges faced by individuals on 
            the autism spectrum, and our team is dedicated to creating a game that is both 
            enjoyable and beneficial for their personal growth. With our game, we hope to 
            provide a platform for individuals to enhance their social and emotional 
            understanding, ultimately leading to a more fulfilling and enriched life.""", 
            font=("Arial", 16))

subheading_label.pack()

# Add Logo
image = tk.PhotoImage(file="EMO_logo.png")
label = tk.Label(root_home, image=image)
label.pack()
>>>>>>> Stashed changes

    root_home.mainloop()
