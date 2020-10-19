import pytube

link = input("Enter Playlist Link You Want to Download : ")

try:
    print("--Starting Download--")
    yt = pytube.Playlist(link).download_all("D:/")
    print("--Download Failed --")
except:
    print("Download Failed")

    
