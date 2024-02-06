import tkinter as tk
import vlc
import os

# vlc, media, player instances
instance = vlc.Instance()
player = instance.media_player_new()
media = instance.media_new("v4l2:///dev/video0")
player.set_media(media)

# Set options for recording
options = ":sout=#transcode{vcodec=h264}:std{access=file,mux=mp4,dst=output.mp4}"

# Add options to media
media.add_option(options)


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
    dir_path = "./recordings/"
    try:
        os.mkdir(dir_path)
        print(f"Directory '{dir_path}' created successfully!")
    except FileExistsError:
        print(f"Error: Directory '{dir_path}' already exists.")


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

root.mainloop()
create_recording_dir()
player.stop()
