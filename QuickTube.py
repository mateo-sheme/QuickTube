from pytube import YouTube
import os
import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox

w = ctk.CTk()

links = []

def link_extraction():
    link_arr = link_textbox.get("1.0", "end-1c")
    links = link_arr.splitlines()
    return [link.strip() for link in links if link.strip()]

destination = '.'
def destination_input():
    destination = location.get().strip() or '.'
    return destination

def mp3_video():
    urls = link_extraction()
    destination = destination_input()

    for url in urls:
        download_video(url, destination, video_type=1)

    link_textbox.delete("1.0", tk.END)
    location.delete(0, tk.END)


def mp4_video():
    urls = link_extraction()
    destination = destination_input()

    for url in urls:
        download_video(url, destination, video_type=2)

    link_textbox.delete("1.0", tk.END)
    location.delete(0, tk.END)


def download_video(url, destination, video_type):
    try :
        yt = YouTube(url)

        if video_type == 1:
            video_type = yt.streams.filter(only_audio=True).first()
            path = video_type.download(output_path=destination)

            base, ext = os.path.splitext(path)
            new_file = base + '.mp3'
            os.rename(path, new_file)

        elif video_type == 2:
            video_type = yt.streams.get_highest_resolution()
            video_type.download(output_path=destination)

        messagebox.showinfo("Success", yt.title + " has been successfully downloaded!")

    except Exception as e:
        messagebox.showinfo("Error", "Error downloading " + yt.title + ": " + str(e))

ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('blue')

w.geometry('500x680')

frame = ctk.CTkFrame(master=w, border_color='#F2696A', border_width=1.5, fg_color='#181620' )
frame.pack(pady=20, padx=40, fill='both', expand=True)

quicktube = ctk.CTkLabel(master=frame, text='QuickTube', 
font=('Cocon-Regular', 70), text_color='#F2696A')
quicktube.pack(pady=42, padx=10)

dropdat = ctk.CTkLabel(master=frame, text='Drop those links here...',
font=('Cocon-Regular', 25), text_color='#F2696A', )
dropdat.pack( padx=10)

link_textbox = ctk.CTkTextbox(master=frame, width=350, height= 100, 
font=('Helvetica', 15), fg_color=('#FFF5E1'), text_color='#2B2B2B',)
link_textbox.pack(pady=15, padx=10)

whereto = ctk.CTkLabel(master=frame, text='Where to champ?',
font=('Cocon-Regular', 25), text_color='#F2696A')
whereto.pack(pady=5, padx=10)

location = ctk.CTkEntry(master=frame, width=350, height=40, font=('Helvetica', 15),
fg_color=('#FFF5E1'), text_color='#2B2B2B')
location.pack(pady=5, padx=10)

button_frame = ctk.CTkFrame(master=frame, fg_color='transparent')
button_frame.pack(pady=10)

howefeelin = ctk.CTkLabel(master=button_frame, text='How we feelin today?',
font=('Cocon-Regular', 25), text_color='#F2696A')
howefeelin.pack(padx=10)

mp3 = ctk.CTkButton(master=button_frame, width=100, height=40, text="MP3", 
hover=True, fg_color='#FFF5E1', text_color='#2B2B2B', command=mp3_video,
hover_color='#F2696A', font=('Cocon-Regular', 25))
mp3.pack(side='left', padx=10)

orr = ctk.CTkLabel(master=button_frame, text='or',
font=('Cocon-Regular', 25), text_color='#FFF5E1')
orr.pack(side='left', padx=10)

mp4 = ctk.CTkButton(master=button_frame, width=100, height=40, text="MP4", 
hover=True, fg_color='#FFF5E1', text_color='#2B2B2B', command=mp4_video,
hover_color='#F2696A', font=('Cocon-Regular', 25))
mp4.pack(side='left', padx=10)

w.mainloop()