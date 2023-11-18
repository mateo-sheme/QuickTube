from pytube import YouTube
import os

print("Welcome! This is a YouTube script downloader. You can insert as many links as you want,\nmake sure to have the correct path if you want a specific directory\nand make sure to copy the entire YouTube link with the id in it not the short version :)")

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

        else:
            print("The number you enterd is incorrect, please make sure you enter either 1 or 2.")

        print(yt.title + " has been successfully downloaded!")
        
    except Exception as e:
        print("Error, something went wrong with " + yt.title + " Try again!", str(e))


links = []
print("\nPlease enter your url that want to download, after each url press enter so that it gets inserted \nonce you are finished you can type 'end' (without the quotation marks, all lower case) to contiune with downloading : ")

while True: 
    link = input("-")
    if link.lower() == "end":
        break
    links.append(link)

destination = input("\nEnter your destination as well where you wanted it saved \nPress enter if you want on the current directory : ")

destination = destination.strip()
if not destination:
    destination = '.'
            
video_type = int(input("\nPlease enter either one of the digits \n1) MP3 \n2) MP4 \n"))

for url in links :
    download_video(url, destination, video_type)
