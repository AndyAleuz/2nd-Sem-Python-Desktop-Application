import tkinter as tk
from tkinter import messagebox
from main_app import MUSIKANA
import styles_musikana

class LoginWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry(styles_musikana.get_centered_geometry())
        self.title("Login")
        self.configure(bg=styles_musikana.MAIN_BG)

        # Frame to hold everything in Place
        self.main_frame = tk.Frame(self, bg=styles_musikana.MAIN_BG)
        self.main_frame.pack(expand=True, fill="both")

        # Center the "MUSIKANA" label to have a more modern look
        self.musikana_text = tk.Label(self.main_frame, text="MUSIKANA", font=("Arial", 32, "bold"), fg="white", bg=styles_musikana.MAIN_BG)
        self.musikana_text.pack(pady=(50, 20))  # Add top and bottom padding

        # Create a form frame to hold the username, password, and button cause if not it wont be middle
        form_frame = tk.Frame(self.main_frame, bg=styles_musikana.MAIN_BG)
        form_frame.pack(pady=20)

        # Username label and entry field (Make it together show you wont be at loss in your codes)
        self.username_label = tk.Label(form_frame, text="Username:", bg=styles_musikana.MAIN_BG, fg="white")
        self.username_label.pack(padx=5, pady=5, anchor="e", fill="x")
        self.username_entry = tk.Entry(form_frame, width=40)
        self.username_entry.pack(padx=5, pady=5)

        # Password label and entry field (Make it together show you wont be at loss in your codes)
        self.password_label = tk.Label(form_frame, text="Password:", bg=styles_musikana.MAIN_BG, fg="white")
        self.password_label.pack(padx=5, pady=5, anchor="e", fill="x")
        self.password_entry = tk.Entry(form_frame, show="*", width=40)
        self.password_entry.pack(padx=5, pady=5)

        # Show/Hide password toggle button (Extra Effect for Visuals #More Grades :))
        self.show_password_var = tk.BooleanVar()
        self.show_password_check = tk.Checkbutton(
            form_frame,
            text="Show Password",
            variable=self.show_password_var,
            bg=styles_musikana.MAIN_BG,
            fg="white",
            activebackground=styles_musikana.MAIN_BG,
            activeforeground="white",
            command=self.toggle_password_visibility
        )
        self.show_password_check.pack(pady=5)

        # Login button
        self.login_button = styles_musikana.create_button(form_frame, "Login", self.validate_login)
        self.login_button.pack(pady=10)

    def toggle_password_visibility(self):
        """Toggle the visibility of the password entry field."""
        if self.show_password_var.get():
            self.password_entry.config(show="")
        else:
            self.password_entry.config(show="*")

    def validate_login(self):
        username = self.username_entry.get().strip().lower()
        password = self.password_entry.get()

        if not username or not password:
            messagebox.showerror("Login Failed", "Username and Password cannot be empty.")
            return

        if username == "andy_aleuz" and password == "password":
            messagebox.showinfo("Login Successful", "Welcome to MUSIKANA!")
            self.destroy()  # Close the login screen
        else:
            messagebox.showerror("Login Failed", "Incorrect username or password.")

    def highlight_invalid_fields(self):
        """Highlight invalid input fields."""
        self.username_entry.config(highlightbackground="red", highlightthickness=2)
        self.password_entry.config(highlightbackground="red", highlightthickness=2)

    def open_main_app(self):
        """Open the main application window"""
        self.destroy()  # Close the login screen
        MUSIKANA().mainloop()  # Start the main application


if __name__ == "__main__":
    login_window = LoginWindow()
    login_window.mainloop()
