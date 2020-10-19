from pytube import YouTube

link = input("Enter Link You Want to Download : ")
yt = YouTube(link)
#To Get itag
#print(yt.streams.all())

dj = yt.streams.first()
print("--Start--")
dj.download("D:/")
print("--End--")
