from pytube import YouTube
import os
import customtkinter as ctk
import tkinter as tk

w = ctk.CTk()



def mp3_video():
    urls = link_extraction()
    video_type = 1
    for url in urls:
        download_video(video_type, url, destination)

def mp4_video():
    url = link_extraction()
    video_type = 2
    download_video(video_type, url, destination)

def download_video(video_type, url, destination):

    if url == "":
        print("erdhi deri ktu ---------------------------------------------------------------------------")

        return False

    try :
        print("erdhi deri ktu ========================================================================================")
        print(type(url))
        print("erdhi deri ktu ========================================================================================")

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

        else:
            print("The number you enterd is incorrect, please make sure you enter either 1 or 2.")

        print(yt.title + " has been successfully downloaded!")
        
    except Exception as e:
        messagebox = tk.messagebox.Message(str(e), title="My Message Box", message="Error, something went wrong with " + yt.title + " Try again!")
        messagebox.showinfo()


def link_extraction():
    # link_var = tk.Text
    link_arr = link_textbox.get("0.0", "end")
    link_textbox.insert("0.0", "wubba lubba dub dub")
    return link_arr

# links = []
# link_var = tk.Text

# def link_get():
#     links.cget('1.0', END)

# def link_add():
#     links.append(link_var)


destination = ctk.StringVar()
def destination_input():
    dest = destination.strip()
    if not dest:
        dest = '.'
    
# def start():
#     for url in links:
#         download_video(url, destination)


ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('blue')


w.geometry('500x680')

frame = ctk.CTkFrame(master=w, border_color='#F2696A', border_width=1.5, fg_color='#181620' )
frame.pack(pady=20, padx=40, fill='both', 
expand=True)

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

button_frame = ctk.CTkFrame(master=frame, fg_color='transparent')
button_frame.pack(pady=10)

mp3 = ctk.CTkButton(master=button_frame, width=100, height=40, text="MP3", 
hover=True, fg_color='#FFF5E1', text_color='#2B2B2B', 
hover_color='#F2696A', font=('Cocon-Regular', 25), command=mp3_video())
mp3.pack(side='left', padx=10)

orr = ctk.CTkLabel(master=button_frame, text='or',
font=('Cocon-Regular', 25), text_color='#FFF5E1')
orr.pack(side='left', padx=10)

mp4 = ctk.CTkButton(master=button_frame, width=100, height=40, text="MP4", 
hover=True, fg_color='#FFF5E1', text_color='#2B2B2B', 
hover_color='#F2696A', font=('Cocon-Regular', 25), command=mp4_video())
mp4.pack(side='left', padx=10)


howefeelin = ctk.CTkLabel(master=frame, text='How we feelin today?',
anchor='center', font=('Cocon-Regular', 25), text_color='#F2696A')
howefeelin.pack(padx=10)


whereto = ctk.CTkLabel(master=frame, text='Where to champ?',
anchor='center', font=('Cocon-Regular', 25), text_color='#F2696A')
whereto.pack(pady=5, padx=10)

location = ctk.CTkEntry(master=frame, width=350, height=40, font=('Helvetica', 15),
fg_color=('#FFF5E1'), text_color='#2B2B2B', command=destination_input())
location.pack(pady=5, padx=10)

ready = ctk.CTkLabel(master=frame, text='Ready?',
anchor='center', font=('Cocon-Regular', 25), text_color='#F2696A')
ready.pack(pady=10, padx=10)

# start = ctk.CTkButton(master=frame, width=100, height=40, text="Start", 
# hover=True, fg_color='#FFF5E1', text_color='#2B2B2B', 
# hover_color='#F2696A', font=('Cocon-Regular', 25), command=start())
# start.pack( padx=10)

w.mainloop()