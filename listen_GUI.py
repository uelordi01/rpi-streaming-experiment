from tkinter import *
import configparser
from streamin_handler import streaming_handler

S_HANDLER = streaming_handler()
class FullScreenApp(object):
    def __init__(self, master, **kwargs):
        self.master = master
        pad = 3
        self._geom = '200x200+0+0'
        master.geometry("{0}x{1}+0+0".format(
            master.winfo_screenwidth() - pad, master.winfo_screenheight() - pad))
        master.bind('<Escape>', self.toggle_geom)

    def toggle_geom(self, event):
        geom = self.master.winfo_geometry()
        print(geom, self._geom)
        self.master.geometry(self._geom)
        self._geom = geom

    def get_window_sizes(self):
        geom = self.master.winfo_geometry()

    def define_start_and_stop_buttons(self, root):
        widht = self.master.winfo_width()
        height = self.master.winfo_height()
        print("finshed")


def start_streaming(event):
    twitch_pre_url = "rtmp://live.twitch.tv/app/"
    start_button.configure(bg="#00ff00")
    stop_button.configure(bg="#eeeeee")
    result = entry.get()
    S_HANDLER.start_streaming()


def stop_streaming(event):
    print("Hello Python", "Hello World")
    stop_button.configure(bg="#ff0000")
    start_button.configure(bg="#eeeeee")
    S_HANDLER.stop_streaming()


def reset_streaming():
    pass


def load_stream_config_file(config_path):
    config = configparser.ConfigParser()
    config.read(config_path)
    config_handler = dict()
    config_handler['stream_config'] = config['stream_config']['stream_key']
    config_handler['input_video_device'] = config['input_device']['input_video_device']
    config_handler['input_audio_device'] = config['input_device']['input_audio_device']
    return config_handler


config_handler = load_stream_config_file("config.ini")
S_HANDLER.configure(config_handler)
print(config_handler)
root = Tk()

root.bind('<Escape>', lambda event: root.state('normal'))
root.bind('<F11>', lambda event: root.state('zoomed'))
app = FullScreenApp(root)

# btn=Button(root, text="START_STREAMING", fg='blue', command= start_streaming())
# btn=Button(root, text="STOP_STREAMING", fg='blue', command= stop_streaming())
# Adjust size

# Specify Grid
Grid.rowconfigure(root, 0, weight=1)
Grid.rowconfigure(root, 1, weight=1)
Grid.columnconfigure(root, 0, weight=1)
Grid.columnconfigure(root, 1, weight=1)

entry = Entry(root, width=100)
entry.delete(0, END)
entry.insert(0, config_handler["stream_config"])
# Posicionarla en la ventana.
# entry.place(x=50, y=50)
entry.grid(row=0, column=1)
# Create Buttons
start_button = Button(root, text="START_STREAMING", fg='black')
start_button.bind("<Button-1>", start_streaming)
# start_button.pack()

stop_button = Button(root, text="STOP_STREAMING", fg='black')
lbl = Label(root, text="streaming url: rtmp://live.twitch.tv/app/", fg='black', font=("Helvetica", 16))
stop_button.bind("<Button-1>", stop_streaming)
# lbl.place(x=60, y=50)
# Set grid
start_button.grid(row=1, column=0, sticky="NSEW", )
stop_button.grid(row=1, column=1, sticky="NSEW")
lbl.grid(row=0, column=0, sticky="NSEW")
root.mainloop()
