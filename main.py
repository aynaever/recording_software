import tkinter as tk
import vlc

instance = vlc.Instance()
player = instance.media_player_new()
media = instance.media_new("v4l2:///dev/video0")
player.set_media(media)


def play_video():
    player.play()


def pause_video():
    player.pause();


root = tk.Tk()
root.title("Recording Program")

start_button = tk.Button(root, text="Start", command=play_video)
pause_button = tk.Button(root, text="Pause", command=pause_video)
start_button.pack()
pause_button.pack()

root.mainloop()
player.stop()
