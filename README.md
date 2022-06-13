# remote-notification-sender
Send notifications to the person running the server.

# Modules
* socket
* win10toast

Since this is a client-server based program, there will be two files:- `client.py` and `server.py`. The one recieving the notification should run the `server.py` file.

`server.py`
```py
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
```

Let us now have a look at the `client.py` file.
```py
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#defining a socket

IP = '192.168.0.102'#ip (to be changed accordingly)
PORT = 1234#must be the same on both the ends

notification = input("Enter your message: ")#input for notification
print("")


if notification == "":
    print("Cant send an empty message!")
    print("")
    quit()


try:
    s.connect((IP,PORT))
except:
    print("Hmm, looks like the receiver is offline. Try again later.")
    quit()

s.send(bytes(notification,'utf-8')) #send the notification details
print("Sent notification successfully!")
```
Note: The `server.py` should be ran before `client.py` is run.

The output would be as follows:
```
Enter your message: This is a notification sent by Shashankh!
``` 

After entering your message, it should reach the reciever in no time!

The user running the `server.py` should see something like this!

![image](https://user-images.githubusercontent.com/72354934/173405302-d83d7122-69cf-449d-a06a-07dae11c9cd5.png)
