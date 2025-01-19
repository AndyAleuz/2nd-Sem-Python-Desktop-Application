import tkinter as tk
from tkinter import messagebox
import styles_musikana
import albums
import tracks
import artist

class MUSIKANA(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("MUSIKANA")
        self.geometry("1400x800")
        self.configure(bg=styles_musikana.MAIN_BG)

        self.create_sidebar()
        self.create_content_area()

        self.show_content("albums")

    def create_sidebar(self):
        """ Create the sidebar with a label and menu buttons """
        sidebar_frame = tk.Frame(self, bg=styles_musikana.SIDEBAR_BG, width=300)
        sidebar_frame.pack(fill="y", side="left")

        # MUSIKANA label at the top
        musikana_label = tk.Label(
            sidebar_frame,
            text="MUSIKANA",
            font=("Arial", 24, "bold"),
            fg="white",
            bg=styles_musikana.SIDEBAR_BG
        )
        musikana_label.pack(padx=20, pady=30)

        # Menu label
        menu_label = tk.Label(
            sidebar_frame,
            text="Menu",
            font=("Arial", 16, "bold"),
            bg=styles_musikana.SIDEBAR_BG,
            fg="white"
        )
        menu_label.pack(fill="x", padx=20, pady=(10, 20))

        # Menu buttons
        self.create_sidebar_button(sidebar_frame, "Albums", lambda: self.show_content("albums"))
        self.create_sidebar_button(sidebar_frame, "Tracks", lambda: self.show_content("tracks"))
        self.create_sidebar_button(sidebar_frame, "Artist", lambda: self.show_content("artists"))

    def create_sidebar_button(self, parent, text, command):
        """ Helper function to create a sidebar button """
        button = styles_musikana.create_button(parent, text, command)
        button.pack(fill="x", padx=10, pady=5)

    def create_content_area(self):
        """ Create the right content area where content will be displayed """
        content_frame = tk.Frame(self, bg=styles_musikana.MAIN_BG)
        content_frame.pack(fill="both", expand=True, side="right")

        #scrolling
        self.canvas = tk.Canvas(content_frame, bg=styles_musikana.MAIN_BG, highlightthickness=0)
        self.canvas.pack(side="left", fill="both", expand=True)

        # Scrollbar
        scrollbar = tk.Scrollbar(content_frame, command=self.canvas.yview)
        scrollbar.pack(side="right", fill="y")

        self.canvas.configure(yscrollcommand=scrollbar.set)

        #scrollable frame inside the canvas
        self.scrollable_frame = tk.Frame(self.canvas, bg=styles_musikana.MAIN_BG)
        self.scrollable_window = self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        self.scrollable_frame.bind(
            "<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )

    def show_content(self, content_type):
        self.clear_content_area()

        #API function to call which API to call cause I have three API
        if content_type == "albums":
            content_data = albums.fetch_albums_from_api()
        elif content_type == "tracks":
            content_data = tracks.fetch_tracks_from_api()
        elif content_type == "artists":
            content_data = artist.fetch_artist_from_api()

        if not content_data:
            messagebox.showerror("Error", f"Failed to fetch {content_type}.")
            return

        row = 0
        col = 0
        max_columns = 3

        for item in content_data:
            image = item.get("strAlbumThumb") if content_type == "albums" else item.get("strTrackThumb") if content_type == "tracks" else item.get("strArtistThumb")
            title = item.get("strAlbum") if content_type == "albums" else item.get("strTrack") if content_type == "tracks" else item.get("strArtist")

            #button for each item (album, track, or artist)
            content_button = styles_musikana.create_content_button(self.scrollable_frame, title, image, lambda item=item: self.show_details(item, content_type))

            # Grid placement
            content_button.grid(row=row, column=col, padx=10, pady=10, sticky="nsew")


            col += 1
            if col >= max_columns:
                col = 0
                row += 1

        for col in range(max_columns):
            self.scrollable_frame.grid_columnconfigure(col, weight=1)
        for row in range((len(content_data) // max_columns) + 1):
            self.scrollable_frame.grid_rowconfigure(row, weight=1)

    def show_details(self, item, content_type):
        self.clear_content_area()

        if content_type == "albums":
            album_name = item.get("strAlbum", "Unknown Album")
            album_artist = item.get("strArtist", "Unknown Artist")
            album_year = item.get("intYearReleased", "Unknown Year")
            album_genre = item.get("strGenre", "Unknown Genre")
            album_style = item.get("strStyle", "Unknown Style")
            album_label = item.get("strLabel", "Unknown Label")
            album_desc = item.get("strDescriptionEN", "No description available.")
            album_thumb_url = item.get("strAlbumThumb", "")
            album_mood = item.get("strMood", "Unknown Mood")

            # Album information below the image
            info_text = f"{album_name} by {album_artist}\nYear: {album_year}\nGenre: {album_genre}\nStyle: {album_style}\nLabel: {album_label}\nMood: {album_mood}\n\n{album_desc}"
            tk.Label(self.scrollable_frame, text=info_text, font=("Arial", 12), bg=styles_musikana.MAIN_BG, fg=styles_musikana.BUTTON_FG, wraplength=700).pack(pady=10)

        elif content_type == "tracks":
            track_name = item.get("strTrack", "Unknown Track")
            track_artist = item.get("strArtist", "Unknown Artist")
            track_album = item.get("strAlbum", "Unknown Album")
            track_number = item.get("intTrackNumber", "Unknown Track Number")
            track_genre = item.get("strGenre", "Unknown Genre")
            track_desc = item.get("strDescriptionEN", "No description available.")
            track_lyrics = item.get("strLyrics", "Lyrics not available.")
            track_thumb_url = item.get("strTrackThumb", "")
            track_duration = item.get("intDuration", "Unknown Duration")


            info_text = f"{track_name} by {track_artist}\nAlbum: {track_album}\nTrack Number: {track_number}\nGenre: {track_genre}\nDuration: {track_duration} seconds\n\nDescription: {track_desc}\n\nLyrics: {track_lyrics}"
            tk.Label(self.scrollable_frame, text=info_text, font=("Arial", 12), bg=styles_musikana.MAIN_BG, fg=styles_musikana.BUTTON_FG, wraplength=700).pack(pady=10)


        elif content_type == "artists":
            artist_name = item.get("strArtist", "Unknown Artist")
            artist_bio = item.get("strBiographyEN", "No biography available.")
            artist_image_url = item.get("strArtistJpeg", "")
            artist_genre = item.get("strGenre", "Unknown Genre")
            artist_style = item.get("strStyle", "Unknown Style")
            artist_mood = item.get("strMood", "Unknown Mood")
            artist_label = item.get("strLabel", "Unknown Label")
            
            info_text = f"{artist_name}\nGenre: {artist_genre}\nStyle: {artist_style}\nMood: {artist_mood}\nLabel: {artist_label}\n\nBiography:\n{artist_bio}"
            tk.Label(self.scrollable_frame, text=info_text, font=("Arial", 12), bg=styles_musikana.MAIN_BG, fg=styles_musikana.BUTTON_FG, wraplength=700).pack(pady=10)

    def clear_content_area(self):
        """ Clear the content area before loading new content """
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    app = MUSIKANA()
    app.mainloop()
