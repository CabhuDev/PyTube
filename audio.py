from pytube import  YouTube;



"""
def DownloadAudio(link): # Enlace de YouTube 
    # Variable para trabajar con videos     
    yt = YouTube(link); # Enlace de YouTube entre paréntesis
    video = yt.streams.get_highest_resolution()
    audio = yt.streams.get_audio_only()
    

DownloadAudio("https://www.youtube.com/watch?v=OuG3EyKlwpE&t=16172s")"""

import tkinter as tk
from tkinter import ttk
from pytube import YouTube
import threading
import os

def download_video():
    video_url = entry.get()
    save_path = "/Users/nombre/Downloads/"  # insert path where you want to save the video

    try:
        # Create a YouTube object
        yt = YouTube(video_url)
        # Get the highest resolution stream
        video_stream = yt.streams.get_highest_resolution()

        # Disable the download button
        button.config(state=tk.DISABLED)

        # Create a progress bar and label
        progress_label = tk.Label(window, text="Downloading...")
        progress_label.pack()
        progress_bar = ttk.Progressbar(window, orient=tk.HORIZONTAL, length=300, mode='indeterminate')
        progress_bar.pack()

        # Start the download in a separate thread
        download_thread = threading.Thread(target=perform_download, args=(video_stream, save_path, progress_bar))
        download_thread.start()
    except Exception as e:
        print("Error:", str(e))
        status_label.config(text="Error: " + str(e))

def perform_download(video_stream, save_path, progress_bar):
    # Start the progress bar animation
    progress_bar.start()

    try:
        # Download the video
        video_filename = video_stream.default_filename
        save_location = os.path.join(save_path, video_filename)
        video_stream.download(output_path=save_path, filename=video_filename)
        print("Download completed!")
        status_label.config(text="Download completed!")
    except Exception as e:
        print("Error:", str(e))
        status_label.config(text="Error: " + str(e))

    # Stop the progress bar animation
    progress_bar.stop()

    # Enable the download button
    button.config(state=tk.NORMAL)

# Create the main window
window = tk.Tk()
window.title("YouTube Video Downloader")

# Set the dimensions of the window
window_width = 400
window_height = 250
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x_coordinate = int((screen_width / 2) - (window_width / 2))
y_coordinate = int((screen_height / 2) - (window_height / 2))
window.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")

# Create the input label and entry
label = tk.Label(window, text="Enter YouTube video URL:")
label.pack()
entry = tk.Entry(window)
entry.pack()

# Create the download button
button = tk.Button(window, text="Download", command=download_video)
button.pack()

# Create the status label
status_label = tk.Label(window, text="")
status_label.pack()

# Start the Tkinter event loop
window.mainloop()
    
    


