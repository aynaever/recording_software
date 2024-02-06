import tkinter as tk
import vlc

# vlc, media, player instances
instance = vlc.Instance()
player = instance.media_player_new()
media = instance.media_new("v4l2:///dev/video0")
player.set_media(media)


# Play video functions
def play_video():
    player.play()


# Pause video functions
def pause_video():
    player.pause()


# Stop video functions
def stop_video():
    player.stop()


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
player.stop()
