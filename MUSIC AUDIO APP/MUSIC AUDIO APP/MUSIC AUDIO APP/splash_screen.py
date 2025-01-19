import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import styles_musikana
import os

# I made a different modules for each Screen cause it slow down if only made it in one file, 
# Its smarter to do so.. If I can the splash screen without error then thats good for me; 

class SplashScreenMUSIKANA(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry(styles_musikana.get_centered_geometry())
        self.title("MUSIKANA INTRO")
        self.configure(bg=styles_musikana.MAIN_BG)

        img_path = os.path.join("Images", "cc716da5427b999ca61a0f5af5457bbb.jpg")
        full_img_path = os.path.abspath(os.path.join(os.path.dirname(__file__), img_path))

        try:
            # Load the background image hehehhe
            self.bg_image = Image.open(full_img_path)
            self.bg_image = self.bg_image.resize((styles_musikana.WINDOW_WIDTH, styles_musikana.WINDOW_HEIGHT), Image.Resampling.LANCZOS)
            self.bg_photo = ImageTk.PhotoImage(self.bg_image)

            # Create a canvas to display the image for the background
            self.canvas = tk.Canvas(self, width=styles_musikana.WINDOW_WIDTH, height=styles_musikana.WINDOW_HEIGHT)
            self.canvas.pack()
            self.canvas.create_image(0, 0, anchor=tk.NW, image=self.bg_photo)

        except Exception as e:
            messagebox.showerror("Error", f"Error loading background image: {e}")
            # Fallback in case image loading fails (Extra precautions just in case)
            self.configure(bg="black")
            self.canvas = tk.Canvas(self, width=styles_musikana.WINDOW_WIDTH, height=styles_musikana.WINDOW_HEIGHT, bg="black")
            self.canvas.pack()

        # Add "MUSIKANA" text on top of the image or background for label so it means its still musikana
        self.musikana_text = self.canvas.create_text(
            styles_musikana.WINDOW_WIDTH // 2,
            styles_musikana.WINDOW_HEIGHT // 2,
            text="MUSIKANA",
            font=("Arial", 50, "bold"),
            fill="white"
        )

        # Start splash screen animation
        self.fade_in()

    def fade_in(self):
        """Fade in the splash screen."""
        self.attributes("-alpha", 0.0) 
        self.after(100, self._fade_in)

    def _fade_in(self):
        current_alpha = self.attributes("-alpha")
        if current_alpha < 1.0:
            new_alpha = current_alpha + 0.1
            self.attributes("-alpha", new_alpha)
            self.after(50, self._fade_in)  
        else:
            self.after(3000, self.fade_out)

    def fade_out(self):
        """Fade out the splash screen."""
        self.after(100, self._fade_out)

    def _fade_out(self):
        current_alpha = self.attributes("-alpha")
        if current_alpha > 0.0:
            new_alpha = current_alpha - 0.1
            self.attributes("-alpha", new_alpha)
            self.after(50, self._fade_out)
        else:
            self.destroy()

    def run(self):
        """Run the splash screen."""
        self.mainloop()

if __name__ == "__main__":
    splash = SplashScreenMUSIKANA()
    splash.run()
