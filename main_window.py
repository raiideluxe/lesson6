import cv2
import tkinter as tk
import threading
from PIL import Image, ImageTk
# import io
# import threading
# import os, sys

# class MainWindow:
#     def take_photo():
#         vc = cv2.VideoCapture('test_video.flv')
#         if vc.isOpened():
#             rval, frame = vc.read()
#         else:
#             rval = False
#
#         while rval:
#             rval, frame = vc.read()
#             img = Image.fromarray(frame)
#             img = resize(img)
#             imgtk = ImageTk.PhotoImage(img)
#             lbl.config(image=imgtk)
#             lbl.img = imgtk
#             if stop == True:
#                 vc.release()
#                 break  # stop the loop thus stops updating the label and reading imagge frames
#             cv2.waitKey(1)
#         vc.release()


class VideoPlayer:
    def __init__(self, pl_video=1, master=None, width=100, height=100):
        self.cap = cv2.VideoCapture(pl_video)
        self.master = master
        self.canvas = tk.Canvas(master, height=height, width=width)
        self.delay = int(1000 / self.cap.get(cv2.CAP_PROP_FPS))


    def place(self, x, y):
        self.canvas.place(x=x, y=y)
        self.update()

    def update(self):
        if button_pause['text'] == 'stop':
            ret, frame = self.cap.read()
        else:
            self.master.after(self.delay, self.update)
            return
        if ret:
            if button_pause['text'] == 'stop':
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                self.photo = ImageTk.PhotoImage(image=Image.fromarray(frame))
                self.canvas.create_image(0, 0, image=self.photo, anchor=tk.NW)
            self.master.after(self.delay, self.update)
        else:
            self.cap.release()


def pause_unpause():
    if button_pause['text'] == 'stop':
        button_pause['text'] = 'play'
    else:
        button_pause['text'] = 'stop'

def take_photo():
    photo = cv2.imread("cats_video.mp4")
    photo_window = tk.Tk()
    label = tk.Label(photo_window, image=photo)
    label.pack()

# window = tk.Tk()
# window.geometry('1000x1000')
# button_pause = tk.Button(window, text='stop', command=pause_unpause)
# button_take_photo = tk.Button(window, text='Снимок', command=take_photo)
# # button_save_photo = tk.Button(window, text='Сохранить', command=save_photo)
# # button_save_photo.place()
# button_pause.place(x=0, y=0)
# button_take_photo.place(x=0, y=20)
# video = VideoPlayer('cats_video.mp4', master=window, width=800, height=1000)
# video.place(x=50, y=0)
#
#
# window.mainloop()

