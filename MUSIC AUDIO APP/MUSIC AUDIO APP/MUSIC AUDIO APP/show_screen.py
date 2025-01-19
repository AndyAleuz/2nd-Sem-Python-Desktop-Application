from splash_screen import SplashScreenMUSIKANA
from login_screen import LoginWindow
from main_app import MUSIKANA

def start_application():
    # Step 1: Show Splash Screen
    splash = SplashScreenMUSIKANA()
    splash.run()

    # Step 2: Show Login Screen
    login = LoginWindow()
    login.mainloop()

    # Step 3: Show Main Application
    app = MUSIKANA()
    app.mainloop()

if __name__ == "__main__":
    start_application()
