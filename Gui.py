
import customtkinter as ctk
import tkinter as tk

w = ctk.CTk()

ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('blue')


w.geometry('500x680')

frame = ctk.CTkFrame(master=w, border_color='#F2696A', border_width=1.5, fg_color='#181620' )
frame.pack(pady=20, padx=40, fill='both', expand=True)

quicktube = ctk.CTkLabel(master=frame, text='QuickTube', 
anchor='center', font=('Cocon-Regular', 70), text_color='#F2696A')
quicktube.pack(pady=42, padx=10)

dropdat = ctk.CTkLabel(master=frame, text='Drop those links here...',
anchor='center', font=('Cocon-Regular', 25), text_color='#F2696A', )
dropdat.pack( padx=10)

link_textbox = ctk.CTkTextbox(master=frame, width=350, height= 100, 
font=('Helvetica', 15), fg_color=('#FFF5E1'), text_color='#2B2B2B',)
link_textbox.pack(pady=15, padx=10)
link_textbox.focus()

whereto = ctk.CTkLabel(master=frame, text='Where to champ?',
anchor='center', font=('Cocon-Regular', 25), text_color='#F2696A')
whereto.pack(pady=5, padx=10)

location = ctk.CTkEntry(master=frame, width=350, height=40, font=('Helvetica', 15),
fg_color=('#FFF5E1'), text_color='#2B2B2B')
location.pack(pady=5, padx=10)

button_frame = ctk.CTkFrame(master=frame, fg_color='transparent')
button_frame.pack(pady=10)

howefeelin = ctk.CTkLabel(master=button_frame, text='How we feelin today?',
anchor='center', font=('Cocon-Regular', 25), text_color='#F2696A')
howefeelin.pack(padx=10)

mp3 = ctk.CTkButton(master=button_frame, width=100, height=40, text="MP3", 
hover=True, fg_color='#FFF5E1', text_color='#2B2B2B', 
hover_color='#F2696A', font=('Cocon-Regular', 25))
mp3.pack(side='left', padx=10)

orr = ctk.CTkLabel(master=button_frame, text='or',
font=('Cocon-Regular', 25), text_color='#FFF5E1')
orr.pack(side='left', padx=10)

mp4 = ctk.CTkButton(master=button_frame, width=100, height=40, text="MP4", 
hover=True, fg_color='#FFF5E1', text_color='#2B2B2B', 
hover_color='#F2696A', font=('Cocon-Regular', 25))
mp4.pack(side='left', padx=10)

# ready = ctk.CTkLabel(master=frame, text='Ready?',
# anchor='center', font=('Cocon-Regular', 25), text_color='#F2696A')
# ready.pack(pady=10, padx=10)

# start = ctk.CTkButton(master=frame, width=100, height=40, text="Start", 
# hover=True, fg_color='#FFF5E1', text_color='#2B2B2B', 
# hover_color='#F2696A', font=('Cocon-Regular', 25))
# start.pack( padx=10)

w.mainloop()