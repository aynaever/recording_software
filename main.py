from datetime import datetime
import tkinter as tk
import vlc
import os
import schedule
import time

# vlc, media, player instances
instance = vlc.Instance()
recording_player = instance.media_player_new()
media = instance.media_new("v4l2:///dev/video0")
recording_player.set_media(media)

# Set options for recording
recordings_path = "./recordings/"
date = datetime.now().strftime("%H-%M_%Y-%m-%d")
recording_options = ":sout=#transcode{vcodec=h264}\
        :std{access=file,mux=mp4,dst="\
        + recordings_path + "recording_" + date + ".mp4}"

# Add recording options to media
media.add_options(recording_options)

# Start and Stop time of recording
start_time = "17:19"
stop_time = "17:22"


# Play video functions
def play_video():
    recording_player.play()


# Pause video functions
def pause_video():
    recording_player.pause()


# Stop video functions
def stop_video():
    recording_player.stop()


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
