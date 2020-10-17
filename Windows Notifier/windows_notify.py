from win10toast import ToastNotifier

#Notifier Popup 
def popup(title,content,duration = 50):
    toast = ToastNotifier()
    toast.show_toast(title,content,duration=duration)

#Main
if __name__ == "__main__":
    popup("Python Toast","Hello From Djcodes")
