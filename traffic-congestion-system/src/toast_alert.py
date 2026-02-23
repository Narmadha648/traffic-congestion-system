# toast_alert.py
from win10toast import ToastNotifier

toaster = ToastNotifier()

def send_alert(message):
    toaster.show_toast("Traffic Congestion Alert", message, duration=5)