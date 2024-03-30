import cv2
import tkinter as tk
import threading
from PIL import Image, ImageTk
import main_window

def open_videoplayer(path="1/vData/cats_video.mp4"):

    window = tk.Tk()
    window.geometry('1000x1000')
    # button_pause = tk.Button(window, text='stop', command=pause_unpause)
    button_take_photo = tk.Button(window, text='Снимок', command=take_photo)
    # # button_save_photo = tk.Button(window, text='Сохранить', command=save_photo)
    # button_save_photo.place()
    # button_pause.place(x=0, y=0)
    button_take_photo.place(x=0, y=20)
    video = main_window.VideoPlayer('cats_video.mp4', master=window, width=800, height=1000)
    video.place(x=50, y=0)

    window.mainloop()
def get_path():
    video_path = path_display.get()
    return video_path
def take_photo():
    photo = cv2.imread("cats_video.mp4")
    photo_window = tk.Tk()
    label = tk.Label(photo_window, image=photo)
    label.pack()

start_window = tk.Tk()
start_window.title("Videoplayer")
start_window.geometry("500x300")
path_display_label=tk.Label(start_window, text="Путь к видео")
path_display_label.grid(row=3, column=2,columnspan=3, padx=10,pady=10)
path_display = tk.Entry(start_window, width=50, borderwidth=5)
path_display.grid(row=5, column=2,columnspan=3, padx=10,pady=10)
button_open_video=tk.Button(start_window, text="Откртыть",command=open_videoplayer)
button_open_video.grid(row=5, column=6,columnspan=3, padx=10,pady=10)
start_window.mainloop()

