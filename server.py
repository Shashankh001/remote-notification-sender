import socket
from win10toast import ToastNotifier

toaster = ToastNotifier()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0',1234))
s.listen(5)

while True:
    cs, address = s.accept()
    notification = cs.recv(1024)
    notification = notification.decode('utf-8')

    toaster.show_toast(f"New Message from {address}",notification)