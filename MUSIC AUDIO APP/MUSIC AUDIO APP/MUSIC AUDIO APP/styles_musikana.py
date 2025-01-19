import requests
import tkinter as tk
from PIL import Image, ImageTk
from io import BytesIO

# I made a different modules for styles, 
# Its smarter to do so.. If I can call every design from one module; 
# I just need to import the module right to other modules so its smarter and easier.
# ---------- Basic Colors ----------
MAIN_BG = "#202020"
HEADER_BG = "#181818"
SIDEBAR_BG = "#2f2f2f" 

BUTTON_BG = "#A9A9A9" 
BUTTON_FG = "#FFFFFF" 
BUTTON_HOVER_BG = "#1DB954" 
BUTTON_CLICK_BG = "#1AA34A"

SONG_LABEL_BG = "#2A2A2A"
SONG_LABEL_TEXT_FG = "#FFFFFF"

WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 600

def get_centered_geometry():
    screen_width = 1920  
    screen_height = 1080  

    x = (screen_width // 2) - (WINDOW_WIDTH // 2)
    y = (screen_height // 2) - (WINDOW_HEIGHT // 2)

    return f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}+{x}+{y}"

# Function to create normal buttons (A mini Storage for my buttons) (like sidebar or login buttons)
def create_button(parent, text, command, width=25, height=2):
    btn = tk.Button(
        parent,
        text=text,
        bg=BUTTON_BG,
        fg=BUTTON_FG,
        font=("Arial", 12),
        borderwidth=0,
        highlightthickness=0,
        command=command,
        padx=10,
        pady=5,
        width=width,
        height=height,
        wraplength=150,
        justify="center"
    )
    # Hover & click effects
    btn.bind("<Enter>", lambda e: e.widget.config(bg=BUTTON_HOVER_BG, fg="white"))
    btn.bind("<Leave>", lambda e: e.widget.config(bg=BUTTON_BG, fg="white"))
    btn.bind("<ButtonPress-1>", lambda e: e.widget.config(bg=BUTTON_CLICK_BG, fg="white"))
    btn.bind("<ButtonRelease-1>", lambda e: e.widget.config(bg=BUTTON_HOVER_BG, fg="white"))

    return btn

# Function to create buttons for my called content where the image and api title name will be display 
#() (A mini Storage for my buttons) (COntent Area Right Side)
def create_content_button(parent, text, image_url, command):
    """Create a customized button with an image and title."""
    # Create frame with border and fixed size (250x200px)
    frame = tk.Frame(parent, bg="#202020", relief="solid", width=250, height=200)
    frame.pack_propagate(False)  # Prevent frame from resizing automatically

    # Load and display here is the code
    if image_url:
        try:
            response = requests.get(image_url)
            img_data = response.content
            img = Image.open(BytesIO(img_data))  # Open image from bytes
            img = img.resize((140, 140))  # Resize image to 140x140px
            img_tk = ImageTk.PhotoImage(img)  # Convert image for Tkinter

            img_label = tk.Label(frame, image=img_tk, bg="#202020")
            img_label.image = img_tk  # Keep a reference to avoid garbage collection
            img_label.grid(row=0, column=0, padx=10)  # Place image in grid layout

        except requests.exceptions.RequestException as e:
            print(f"Error loading image: {e}")
            img_label = tk.Label(frame, text="Image Not Found", bg="#ffffff")  # Fallback text
            img_label.grid(row=0, column=0, padx=10,pady=10)  # Place fallback text

    title_button = tk.Button(
        frame,
        text=text,
        bg=BUTTON_BG,
        fg=BUTTON_FG,
        font=("Arial", 12),
        borderwidth=0,
        highlightthickness=0,
        command=command,
        padx=10,
        pady=5,
        width=15,
        height=7,
        wraplength=150,
        justify="center"
    )
    # Hover & click effects for styles si it can feel responsive in a way
    title_button.bind("<Enter>", lambda e: e.widget.config(bg=BUTTON_HOVER_BG, fg="white"))
    title_button.bind("<Leave>", lambda e: e.widget.config(bg=BUTTON_BG, fg="white"))
    title_button.bind("<ButtonPress-1>", lambda e: e.widget.config(bg=BUTTON_CLICK_BG, fg="white"))
    title_button.bind("<ButtonRelease-1>", lambda e: e.widget.config(bg=BUTTON_HOVER_BG, fg="white"))
    title_button.grid(row=0, column=1, padx=10)

    return frame
