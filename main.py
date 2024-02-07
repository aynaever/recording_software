from datetime import datetime
import tkinter as tk
import vlc
import os
import schedule
import time

# vlc, media, player instances
instance = vlc.Instance()
player = instance.media_player_new()
media = instance.media_new("v4l2:///dev/video0")
player.set_media(media)

# Set options for recording
recordings_path = "./recordings/"
date = datetime.now().strftime("%H-%M_%Y-%m-%d")
options = ":sout=#transcode{vcodec=h264}:std{access=file,mux=mp4,dst="\
        + recordings_path + "recording_" + date + ".mp4}"

# Add options to media
media.add_option(options)

# Start and Stop time of recording
start_time = "08:00"
stop_time = "22:00"


# Play video functions
def play_video():
    player.play()


# Pause video functions
def pause_video():
    player.pause()


# Stop video functions
def stop_video():
    player.stop()


# Create recordings directory
def create_recording_dir():
    try:
        os.mkdir(recordings_path)
        print(f"Directory '{recordings_path}' created successfully!")
    except FileExistsError:
        print(f"Directory '{recordings_path}' already exists.")


create_recording_dir()

root = tk.Tk()
root.title("Recording Program")

# media control buttons
start_button = tk.Button(root, text="Start", command=play_video)
pause_button = tk.Button(root, text="Pause", command=pause_video)
stop_button = tk.Button(root, text="Stop", command=stop_video)

# add buttons to the gui
start_button.pack()
pause_button.pack()
stop_button.pack()

# Schedule starting record and stopping
schedule.every().day.at(start_time).do(play_video)
schedule.every().day.at(stop_time).do(stop_video)

while True:
    schedule.run_pending()
    time.sleep(30)

root.mainloop()
player.stop()
