import socket
from win10toast import ToastNotifier

toaster = ToastNotifier() #defining the notification toaster

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#defining socket
s.bind(('0.0.0.0',1234))#binding ip
s.listen(5)#can accept upto 5 clients

while True:
    cs, address = s.accept()
    
    notification = cs.recv(1024)#recieve the notification message
    notification = notification.decode('utf-8')#decode the message

    toaster.show_toast(f"New Message from {address}",notification)#show the notification
